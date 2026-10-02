#!/usr/bin/env python3
"""YouTube Downloader — консольное приложение."""
import argparse
import sys
from pathlib import Path

import questionary
from rich import box
from rich.align import Align
from rich.console import Console
from rich.panel import Panel
from rich.rule import Rule
from rich.text import Text

import config
from downloader import DownloadFailed, download
from i18n import get_lang, set_lang, t
from runtime import diagnostics
from urls import normalize_url

for stream in (sys.stdout, sys.stderr):
    if hasattr(stream, 'reconfigure'):
        stream.reconfigure(encoding='utf-8', errors='replace')

console = Console()
MENU_STYLE = questionary.Style([
    ('qmark', 'fg:#84efc0 bold'),
    ('question', 'bold'),
    ('answer', 'fg:#84efc0 bold'),
    ('pointer', 'fg:#84efc0 bold'),
    ('highlighted', 'fg:#84efc0 bold'),
    ('selected', 'fg:#84efc0'),
    ('instruction', 'fg:#8c9bae'),
])


def _select(message, **kwargs):
    kwargs.setdefault('instruction', t('select_help'))
    kwargs.setdefault('style', MENU_STYLE)
    return questionary.select(message, **kwargs)


QUALITY_ORDER = ["360", "480", "720", "1080", "1440", "2160", "best", "mp3"]
QUALITY_KEYS = {
    "360": "q_360", "480": "q_480", "720": "q_720",
    "1080": "q_1080", "1440": "q_1440", "2160": "q_2160",
    "best": "q_best", "mp3": "q_mp3",
}


# ─────────────────────────── UI helpers ───────────────────────────

def _banner(subtitle_key: str = "app_tagline") -> None:
    console.clear()
    title = Text()
    title.append("↓  ", style="bold #84efc0")
    title.append(t("app_name"), style="bold white")
    subtitle = Text(t(subtitle_key), style="dim")
    body = Align.center(Text.assemble(title, "\n", subtitle))
    console.print(Panel(
        body,
        box=box.ROUNDED,
        border_style="#84efc0",
        padding=(1, 3),
    ))
    console.print()


def _section(title: str) -> None:
    console.print(Rule(f"[bold]{title}[/]", style="#84efc0"))
    console.print()


def _pause() -> None:
    console.print()
    console.input(f"[dim]{t('press_enter')}…[/] ")


def _success_panel(info: dict, folder: str) -> None:
    title = info.get("title", "video")
    dur_sec = int(info.get("duration") or 0)
    h, rem = divmod(dur_sec, 3600)
    m, s = divmod(rem, 60)
    dur = f"{h}:{m:02d}:{s:02d}" if h else f"{m}:{s:02d}"

    text = Text()
    text.append(f"✔  {t('done_title')}\n\n", style="bold green")
    text.append(f"{t('title_label')}:   ", style="dim")
    text.append(f"{title}\n", style="white")
    text.append(f"{t('duration_label')}: ", style="dim")
    text.append(f"{dur}\n", style="white")
    text.append(f"{t('saved_to')}:      ", style="dim")
    text.append("\n".join(info.get('saved_files', [folder])), style="cyan")

    console.print(Panel(
        text,
        box=box.ROUNDED,
        border_style="green",
        padding=(1, 3),
    ))
    for warning in info.get('warnings', []):
        console.print(Text(warning, style='yellow'))


def _error_panel(title: str, message: str, hint: str | None = None) -> None:
    text = Text()
    text.append(f"✖  {title}\n\n", style="bold red")
    text.append(message[:600].strip(), style="white")
    if hint:
        text.append(f"\n\n{hint}", style="yellow")
    console.print(Panel(
        text,
        box=box.ROUNDED,
        border_style="red",
        padding=(1, 3),
    ))


# ─────────────────────── Идентификация URL ───────────────────────

def _is_youtube(url: str) -> bool:
    try:
        normalize_url(url)
        return True
    except ValueError:
        return False


# ────────────────────────── Диалоги ──────────────────────────

def ask_language() -> str | None:
    answer = _select(
        t("choose_language"),
        choices=[
            questionary.Choice(title=t("lang_ru"), value="ru"),
            questionary.Choice(title=t("lang_en"), value="en"),
        ],
        qmark="›",
        instruction=" ",
    ).unsafe_ask()
    return answer


def _quality_choices(default: str | None = None):
    items = list(QUALITY_ORDER)
    if default in items:
        items.remove(default)
        items.insert(0, default)
    return [questionary.Choice(t(QUALITY_KEYS[q]), value=q) for q in items]


# ──────────────────────── Основные потоки ────────────────────────

def flow_download(cfg: dict) -> None:
    _banner()
    _section(t("download_title"))

    url = questionary.text(t("prompt_url"), qmark="›").unsafe_ask()
    if url is None:
        return
    url = url.strip()

    if not url:
        _error_panel(t("err_download_title"), t("err_url_empty"))
        return _pause()
    if not _is_youtube(url):
        _error_panel(t("err_download_title"), t("err_url_invalid"))
        return _pause()

    quality = _select(
        t("prompt_quality"),
        choices=_quality_choices(cfg.get("quality")),
        qmark="›",
    ).unsafe_ask()
    if quality is None:
        return

    _banner()
    _section(t("download_title"))

    try:
        info = download(url, quality, cfg["folder"], cfg.get('proxy'), cfg.get('cookies'), console=console)
    except DownloadFailed as e:
        msg = str(e)
        hint = None
        low = msg.lower()
        if "ffmpeg" in low:
            hint = t("err_hint_ffmpeg")
        elif any(k in low for k in ("signature", "unable to extract", "player")):
            hint = t("err_hint_ytdlp")
        _error_panel(t("err_download_title"), msg, hint)
        return _pause()
    except KeyboardInterrupt:
        console.print(f"[yellow]{t('cancel')}[/]")
        return

    _success_panel(info, cfg["folder"])
    _pause()


def flow_settings(cfg: dict) -> dict:
    while True:
        _banner()
        _section(t("settings_title"))

        console.print(Text(f"{t('folder_current')}: {cfg['folder']}", style='cyan'))
        console.print(f"[dim]{t('quality_current')}:[/] [cyan]{cfg['quality']}[/]")
        lang_name = "Русский" if get_lang() == "ru" else "English"
        console.print(f"[dim]{t('lang_current')}:[/] [cyan]{lang_name}[/]")
        console.print()

        action = _select(
            t("settings_title"),
            choices=[
                questionary.Choice(t("setting_lang"), value="lang"),
                questionary.Choice(t("setting_quality"), value="quality"),
                questionary.Choice(t("setting_folder"), value="folder"),
                questionary.Choice(t('setting_proxy'), value='proxy'),
                questionary.Choice(t('setting_cookies'), value='cookies'),
                questionary.Separator(),
                questionary.Choice(t("back"), value="back"),
            ],
            qmark="›",
        ).unsafe_ask()

        if action in (None, "back"):
            return cfg

        if action == "lang":
            new_lang = ask_language()
            if new_lang:
                set_lang(new_lang)
                cfg["lang"] = new_lang
                _save(cfg)

        elif action == "quality":
            q = _select(
                t("prompt_quality"),
                choices=_quality_choices(cfg.get("quality")),
                qmark="›",
            ).unsafe_ask()
            if q:
                cfg["quality"] = q
                _save(cfg)

        elif action == "folder":
            new_folder = questionary.path(
                t("folder_prompt"),
                default=cfg["folder"],
                qmark="›",
            ).unsafe_ask()
            if new_folder:
                cfg["folder"] = str(Path(new_folder).expanduser())
                _save(cfg)
        elif action in ('proxy', 'cookies'):
            answer = questionary.text(t('prompt_' + action), default=cfg.get(action, ''), qmark='›').unsafe_ask()
            if answer is not None:
                cfg[action] = answer.strip()
                _save(cfg)


def flow_about() -> None:
    _banner()
    console.print(Panel(
        Text.from_markup(t("about_text")),
        title=f"[bold magenta]{t('about_title')}[/]",
        title_align="left",
        box=box.ROUNDED,
        border_style="magenta",
        padding=(1, 3),
    ))
    _pause()


# ─────────────────────────── Точка входа ───────────────────────────

def _first_run_language(cfg: dict) -> dict:
    _banner(subtitle_key="first_run")
    lang = ask_language()
    if lang is None:
        return cfg
    cfg["lang"] = lang
    set_lang(lang)
    _save(cfg)
    return cfg


def _save(cfg):
    try:
        config.save(cfg)
        console.print(Text(t('saved'), style='green'))
    except config.ConfigError as exc:
        _error_panel(t('err_config'), str(exc))
        _pause()


def show_diagnostics():
    import yt_dlp.version
    console.print(Text('YouTube Downloader 1.0.1 | yt-dlp ' + yt_dlp.version.__version__))
    result = diagnostics()
    for name, version in result.items():
        console.print(Text(f'{name}: {version}', style='yellow' if version in ('MISSING', 'ERROR') else 'green'))
    console.print(Text(f'Config: {config.CONFIG_PATH}'))
    return 0 if all(result[key] not in ('MISSING', 'ERROR') for key in ('ffmpeg', 'ffprobe')) and any(result[key] not in ('MISSING', 'ERROR') for key in ('node', 'deno')) else 1


def main() -> int:
    parser = argparse.ArgumentParser(description='YouTube Downloader — RU / EN terminal application')
    parser.add_argument('url', nargs='?', help='YouTube video URL (optional)')
    parser.add_argument('--quality', choices=QUALITY_ORDER)
    parser.add_argument('--folder')
    parser.add_argument('--lang', choices=['ru', 'en'])
    parser.add_argument('--proxy')
    parser.add_argument('--cookies', help='Netscape cookies.txt file')
    parser.add_argument('--doctor', action='store_true', help='Check dependencies')
    parser.add_argument('--version', action='version', version='YouTube Downloader 1.0.1')
    args = parser.parse_args()
    set_lang(args.lang or 'ru')
    try:
        cfg = config.load()
    except config.ConfigError as exc:
        _error_panel(t('err_config'), str(exc), t('config_fallback'))
        cfg = dict(config.DEFAULTS)
    set_lang(args.lang or cfg.get('lang') or 'ru')
    if args.doctor:
        return show_diagnostics()
    if args.url:
        try:
            info = download(args.url, args.quality or cfg['quality'], args.folder or cfg['folder'],
                            args.proxy if args.proxy is not None else cfg['proxy'],
                            args.cookies if args.cookies is not None else cfg['cookies'], console=console)
            _success_panel(info, args.folder or cfg['folder'])
            return 0
        except DownloadFailed as exc:
            _error_panel(t('err_download_title'), str(exc), t('error_help'))
            return 1
    if not sys.stdin.isatty() or not sys.stdout.isatty():
        console.print(Text(t('err_terminal'), style='yellow'))
        return 2

    if not cfg.get("lang") and not args.lang:
        cfg = _first_run_language(cfg)
        if not cfg.get('lang'):
            return 0

    set_lang(args.lang or cfg["lang"])

    while True:
        _banner()
        _section(t("menu_title"))
        summary = Text()
        summary.append(f"{t('quality_current')}: ", style='dim')
        summary.append(t(QUALITY_KEYS[cfg['quality']]), style='#84efc0')
        summary.append(f"\n{t('folder_current')}: ", style='dim')
        summary.append(cfg['folder'], style='white')
        console.print(summary)
        console.print()

        choice = _select(
            t("menu_title"),
            choices=[
                questionary.Choice(t("menu_download"), value="download"),
                questionary.Choice(t("menu_settings"), value="settings"),
                questionary.Choice(t("menu_about"), value="about"),
                questionary.Choice(t('menu_doctor'), value='doctor'),
                questionary.Separator(),
                questionary.Choice(t("menu_exit"), value="exit"),
            ],
            qmark="›",
        ).unsafe_ask()

        if choice in (None, "exit"):
            console.print(f"\n[magenta]{t('goodbye')}[/]\n")
            return 0

        if choice == "download":
            flow_download(cfg)
        elif choice == "settings":
            cfg = flow_settings(cfg)
        elif choice == "about":
            flow_about()
        elif choice == 'doctor':
            show_diagnostics()
            _pause()


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (KeyboardInterrupt, EOFError):
        console.print(Text(t('cancel'), style='yellow'))
        sys.exit(130)
    except Exception as exc:
        _error_panel(t('err_generic_title'), str(exc), t('error_help'))
        sys.exit(1)
