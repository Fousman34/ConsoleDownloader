"""Single-video downloads with strict height limits and final-file verification."""
import re
import json
import subprocess
import sys
from pathlib import Path
import yt_dlp
from rich.console import Console
from rich.progress import Progress, BarColumn, TextColumn, DownloadColumn, TransferSpeedColumn, TimeRemainingColumn
from config import QUALITIES
from i18n import t
from runtime import tool
from urls import normalize_url

class DownloadFailed(Exception):
    pass

def _build_format(quality):
    if quality not in QUALITIES:
        raise DownloadFailed(t('err_quality'))
    if quality == 'mp3':
        return 'bestaudio/best', [{'key': 'FFmpegExtractAudio', 'preferredcodec': 'mp3',
                                 'preferredquality': '192', 'nopostoverwrites': True}]
    if quality == 'best':
        return 'bv*+ba/b', []
    return f'bv*[height<=?{quality}]+ba/b[height<=?{quality}]', []

def build_options(quality, folder, proxy=None, cookies=None):
    fmt, processors = _build_format(quality)
    ffmpeg, ffprobe = tool('ffmpeg'), tool('ffprobe')
    if not ffmpeg or not ffprobe:
        raise DownloadFailed(t('err_ffmpeg'))
    runtimes = {name: {'path': path} for name in ('deno', 'node') if (path := tool(name))}
    options = {
        'format': fmt, 'outtmpl': str(Path(folder) / ('%(title).150B [%(id)s] [' + quality + '].%(ext)s')),
        'quiet': True, 'noprogress': True, 'noplaylist': True,
        'extract_flat': 'in_playlist', 'playlistend': 1,
        'merge_output_format': 'mkv', 'postprocessors': processors,
        'ffmpeg_location': str(Path(ffmpeg).parent), 'js_runtimes': runtimes,
        'windowsfilenames': True, 'overwrites': False,
        'retries': 3, 'fragment_retries': 3, 'socket_timeout': 20,
        'continuedl': True, 'extractor_retries': 3,
        'concurrent_fragment_downloads': 3,
    }
    if proxy:
        options['proxy'] = proxy
    if cookies:
        cookie_path = Path(cookies).expanduser()
        if not cookie_path.is_file():
            raise DownloadFailed(t('err_cookies'))
        options['cookiefile'] = str(cookie_path)
    return options

class Logger:
    def __init__(self):
        self.warnings = []
    def debug(self, message):
        pass
    def info(self, message):
        pass
    def warning(self, message):
        self.warnings.append(_humanize(message))
    def error(self, message):
        pass

def download(url, quality, folder, proxy=None, cookies=None, console=None):
    console = console or Console()
    try:
        url = normalize_url(url)
    except ValueError as exc:
        raise DownloadFailed(t('err_url_invalid')) from exc
    try:
        folder_path = Path(folder).expanduser().resolve()
        options = build_options(quality, folder_path, proxy, cookies)
        folder_path.mkdir(parents=True, exist_ok=True)
        logger = Logger()
        options['logger'] = logger
        paths = []
        with Progress(TextColumn('{task.description}'), BarColumn(complete_style='#84efc0', finished_style='green'), DownloadColumn(), TransferSpeedColumn(), TimeRemainingColumn(), console=console, refresh_per_second=8) as progress:
            tasks = {}
            status = progress.add_task(t('preparing'), total=None)
            def hook(data):
                key = data.get('filename', 'download')
                if key not in tasks:
                    tasks[key] = progress.add_task(t('downloading'), total=None)
                task = tasks[key]
                total = data.get('total_bytes') or data.get('total_bytes_estimate')
                done = data.get('downloaded_bytes', 0)
                if data['status'] == 'finished':
                    total = total or done
                progress.update(task, total=total, completed=done)
            def post_hook(data):
                progress.update(status, description=t('processing'))
            def final_hook(filename):
                paths.append(Path(filename).resolve())
            options.update(progress_hooks=[hook], postprocessor_hooks=[post_hook], post_hooks=[final_hook])
            with yt_dlp.YoutubeDL(options) as ydl:
                info = ydl.extract_info(url, download=False)
                if not info or info.get('_type') in ('playlist', 'multi_video'):
                    raise DownloadFailed(t('err_collection'))
                if info.get('is_live'):
                    raise DownloadFailed(t('err_live'))
                info = ydl.process_ie_result(info, download=True)
            progress.update(status, description=t('processing'), total=1, completed=1)
        if not info or info.get('_type') in ('playlist', 'multi_video'):
            raise DownloadFailed(t('err_no_file'))
        if not paths and info.get('filepath'):
            paths.append(Path(info['filepath']).resolve())
        files = [str(path) for path in dict.fromkeys(paths) if path.is_file() and path.stat().st_size > 0]
        if not files:
            raise DownloadFailed(t('err_no_file'))
        for filename in files:
            _verify_media(filename, quality)
        info['saved_files'] = files
        info['warnings'] = list(dict.fromkeys(logger.warnings))
        return info
    except DownloadFailed:
        raise
    except (yt_dlp.utils.DownloadError, OSError) as exc:
        raise DownloadFailed(_explain_error(exc)) from exc


def _verify_media(filename, quality):
    """Check actual streams, not just a nonempty file or its extension."""
    try:
        result = subprocess.run([tool('ffprobe'), '-v', 'error', '-show_streams', '-of', 'json', str(filename)],
                                capture_output=True, text=True, timeout=30,
                                creationflags=subprocess.CREATE_NO_WINDOW if sys.platform == 'win32' else 0)
        streams = json.loads(result.stdout).get('streams', []) if result.returncode == 0 else []
    except (OSError, subprocess.TimeoutExpired, ValueError, TypeError) as exc:
        raise DownloadFailed(t('err_media')) from exc
    wanted = 'audio' if quality == 'mp3' else 'video'
    matching = [s for s in streams if s.get('codec_type') == wanted and not s.get('disposition', {}).get('attached_pic')]
    if not matching:
        raise DownloadFailed(t('err_media'))
    if quality.isdigit() and any((s.get('height') or 0) > int(quality) for s in matching):
        raise DownloadFailed(t('err_height'))


def _explain_error(exc):
    message = _humanize(str(exc))
    low = message.lower()
    if isinstance(exc, OSError):
        key = 'err_disk'
    elif 'drm' in low:
        key = 'err_drm'
    elif any(s in low for s in ('unsupported url', 'no video', 'not a video', 'no media')):
        key = 'err_unsupported'
    elif any(s in low for s in ('403', '401', 'login', 'sign in', 'private', 'cookies', 'geo', 'restricted')):
        key = 'err_access'
    elif 'requested format' in low:
        key = 'err_format'
    elif any(s in low for s in ('404', '410', 'removed', 'not available', 'unavailable')):
        key = 'err_unavailable'
    elif any(s in low for s in ('timed out', 'timeout', 'connection', 'resolve', 'network')):
        key = 'err_network'
    else:
        key = 'err_site'
    return t(key) + '\n\n' + t('error_details') + ': ' + message[:350]

def _humanize(message):
    message = re.sub(r'\x1b\[[0-9;]*m', '', message)
    return message.removeprefix('ERROR: ').strip()
