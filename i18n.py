"""Простенькая локализация."""

TRANS = {
    "ru": {
        "app_name": "YouTube Downloader",
        "app_tagline": "Скачивайте видео с YouTube прямо из консоли",
        "first_run": "Выберите язык  •  Choose your language",
        "choose_language": "Выберите язык интерфейса",
        "lang_ru": "🇷🇺  Русский",
        "lang_en": "🇬🇧  English",

        "menu_title": "Главное меню",
        "menu_download": "📥  Скачать видео",
        "menu_settings": "⚙️   Настройки",
        "menu_about": "ℹ️   О программе",
        "menu_exit": "🚪  Выход",

        "download_title": "📥  Скачать видео",
        "prompt_url": "Вставьте ссылку на видео YouTube",
        "err_download_title": "Ошибка загрузки",
        "err_url_empty": "Ссылка не может быть пустой",
        "err_url_invalid": "Это не похоже на ссылку YouTube. Проверьте адрес.",

        "prompt_quality": "Выберите качество",
        "q_360": "360p",
        "q_480": "480p",
        "q_720": "720p · HD",
        "q_1080": "1080p",
        "q_1440": "1440p (2K)",
        "q_2160": "2160p (4K)",
        "q_best": "Лучшее доступное",
        "q_mp3": "Только аудио (MP3)",

        "downloading": "Скачивание",
        "processing": "Обработка (ffmpeg)…",

        "done_title": "Готово!",
        "title_label": "Название",
        "duration_label": "Длительность",
        "saved_to": "Сохранено в",

        "err_generic_title": "Неизвестная ошибка",
        "err_hint_ytdlp": "Совет: YouTube часто меняется — попробуйте `pip install -U yt-dlp`.",
        "err_hint_ffmpeg": "Совет: установите ffmpeg и добавьте его в PATH.",
        "cancel": "Отменено.",
        "press_enter": "Enter — вернуться в меню",

        "settings_title": "Настройки",
        "setting_lang": "🌐  Язык интерфейса",
        "setting_quality": "🎚️   Качество по умолчанию",
        "setting_folder": "📁  Папка для скачивания",
        "back": "← Назад",
        "folder_prompt": "Путь к папке (Tab — автодополнение)",
        "folder_current": "Текущая папка",
        "quality_current": "Качество по умолчанию",
        "lang_current": "Текущий язык",
        "saved": "Сохранено",
        "updated": "Настройка обновлена",

        "about_title": "О программе",
        "about_text": (
            "[bold white]YouTube Downloader[/] — консольное приложение "
            "для скачивания видео и аудио с YouTube.\n\n"
            "[bold magenta]Возможности[/]\n"
            "  • Выбор качества от 360p до 4K\n"
            "  • Извлечение аудио в MP3\n"
            "  • Прогресс-бар в реальном времени\n"
            "  • Русский и английский интерфейс\n"
            "  • Настройки сохраняются между запусками\n\n"
            "[bold magenta]Стек[/]\n"
            "  Python  •  yt-dlp  •  ffmpeg  •  rich  •  questionary\n\n"
            "[bold magenta]Управление[/]\n"
            "  [cyan]↑ ↓[/]    навигация по меню\n"
            "  [cyan]Enter[/]  выбор\n"
            "  [cyan]Tab[/]    автодополнение пути\n"
            "  [cyan]Ctrl+C[/] выход"
        ),
        "goodbye": "До встречи!",
    },

    "en": {
        "app_name": "YouTube Downloader",
        "app_tagline": "Download YouTube videos right from your terminal",
        "first_run": "Выберите язык  •  Choose your language",
        "choose_language": "Choose interface language",
        "lang_ru": "🇷🇺  Русский",
        "lang_en": "🇬🇧  English",

        "menu_title": "Main menu",
        "menu_download": "📥  Download video",
        "menu_settings": "⚙️   Settings",
        "menu_about": "ℹ️   About",
        "menu_exit": "🚪  Exit",

        "download_title": "📥  Download video",
        "prompt_url": "Paste a YouTube video URL",
        "err_download_title": "Download error",
        "err_url_empty": "URL cannot be empty",
        "err_url_invalid": "This doesn't look like a YouTube URL. Check the link.",

        "prompt_quality": "Choose quality",
        "q_360": "360p",
        "q_480": "480p",
        "q_720": "720p  (default)",
        "q_1080": "1080p",
        "q_1440": "1440p (2K)",
        "q_2160": "2160p (4K)",
        "q_best": "Best available",
        "q_mp3": "Audio only (MP3)",

        "downloading": "Downloading",
        "processing": "Processing (ffmpeg)…",

        "done_title": "Done!",
        "title_label": "Title",
        "duration_label": "Duration",
        "saved_to": "Saved to",

        "err_generic_title": "Unknown error",
        "err_hint_ytdlp": "Tip: YouTube changes often — try `pip install -U yt-dlp`.",
        "err_hint_ffmpeg": "Tip: install ffmpeg and add it to PATH.",
        "cancel": "Cancelled.",
        "press_enter": "Press Enter to return to menu",

        "settings_title": "Settings",
        "setting_lang": "🌐  Interface language",
        "setting_quality": "🎚️   Default quality",
        "setting_folder": "📁  Download folder",
        "back": "← Back",
        "folder_prompt": "Folder path (Tab — autocomplete)",
        "folder_current": "Current folder",
        "quality_current": "Default quality",
        "lang_current": "Current language",
        "saved": "Saved",
        "updated": "Setting updated",

        "about_title": "About",
        "about_text": (
            "[bold white]YouTube Downloader[/] — a console app "
            "to download YouTube video & audio.\n\n"
            "[bold magenta]Features[/]\n"
            "  • Quality from 360p to 4K\n"
            "  • Extract audio to MP3\n"
            "  • Real-time progress bar\n"
            "  • Russian and English UI\n"
            "  • Settings persist between runs\n\n"
            "[bold magenta]Stack[/]\n"
            "  Python  •  yt-dlp  •  ffmpeg  •  rich  •  questionary\n\n"
            "[bold magenta]Controls[/]\n"
            "  [cyan]↑ ↓[/]    navigate menu\n"
            "  [cyan]Enter[/]  select\n"
            "  [cyan]Tab[/]    path autocomplete\n"
            "  [cyan]Ctrl+C[/] exit"
        ),
        "goodbye": "See you!",
    },
}

_current = "en"

TRANS['ru'].update({
    'select_help': '(↑/↓ — выбор, Enter — подтвердить)',
    'q_720': '720p',
    'setting_proxy': 'Прокси', 'setting_cookies': 'Файл cookies.txt',
    'prompt_proxy': 'Адрес прокси (пусто — отключить)',
    'prompt_cookies': 'Путь к cookies.txt в формате Netscape (пусто — отключить)',
    'menu_doctor': 'Проверка зависимостей',
    'preparing': 'Получение информации…',
    'err_quality': 'Неподдерживаемое качество.',
    'err_ffmpeg': 'Нужны ffmpeg и ffprobe. Установите их или используйте готовую сборку.',
    'err_js': 'Нужен Node.js 22+ или Deno 2.3+. Используйте готовую сборку или установите среду.',
    'err_cookies': 'Файл cookies.txt не найден.',
    'err_no_file': 'Загрузка не создала итоговый файл. Проверьте предупреждения и обновите yt-dlp.',
    'err_config': 'Ошибка настроек',
    'config_fallback': 'Используются настройки по умолчанию. Исходный файл пока не изменён.',
    'err_terminal': 'Для меню нужен обычный интерактивный терминал. Запустите start.cmd или укажите URL в командной строке.',
    'error_help': 'Проверьте интернет и зависимости (--doctor). При ограничениях сети задайте свой прокси в настройках. Подробнее: README.md.',
})
TRANS['en'].update({
    'select_help': '(↑/↓ to select, Enter to confirm)',
    'q_720': '720p',
    'setting_proxy': 'Proxy', 'setting_cookies': 'Cookies.txt file',
    'prompt_proxy': 'Proxy URL (empty to disable)',
    'prompt_cookies': 'Netscape cookies.txt path (empty to disable)',
    'menu_doctor': 'Check dependencies',
    'preparing': 'Fetching information…',
    'err_quality': 'Unsupported quality.',
    'err_ffmpeg': 'ffmpeg and ffprobe are required. Install them or use the portable build.',
    'err_js': 'Node.js 22+ or Deno 2.3+ is required. Install a runtime or use the portable build.',
    'err_cookies': 'Cookies.txt file was not found.',
    'err_no_file': 'No final file was created. Check warnings and update yt-dlp.',
    'err_config': 'Settings error',
    'config_fallback': 'Using defaults. The original file has not been changed yet.',
    'err_terminal': 'The menu requires an interactive terminal. Run start.cmd or pass a URL on the command line.',
    'error_help': 'Check your connection and dependencies (--doctor). Configure your own proxy if required. See README.md.',
})


def set_lang(code: str) -> None:
    global _current
    if code in TRANS:
        _current = code


def get_lang() -> str:
    return _current


def t(key: str) -> str:
    return TRANS.get(_current, {}).get(key, key)
