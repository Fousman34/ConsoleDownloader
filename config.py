"""Validated settings with atomic writes."""
import json
import os
import tempfile
from pathlib import Path
from i18n import LANGUAGES

CONFIG_PATH = Path(os.environ.get('YTDL_CONFIG', str(Path.home() / '.ytdl_config.json')))
QUALITIES = ('360', '480', '720', '1080', '1440', '2160', 'best', 'mp3')
DEFAULTS = {'lang': None, 'quality': '720', 'folder': str(Path.home() / 'Downloads' / 'Video'), 'proxy': '', 'cookies': ''}

class ConfigError(Exception):
    pass

def validate(data):
    result = dict(DEFAULTS)
    if not isinstance(data, dict):
        return result
    if data.get('lang') in LANGUAGES:
        result['lang'] = data['lang']
    if data.get('quality') in QUALITIES:
        result['quality'] = data['quality']
    for key in ('folder', 'proxy', 'cookies'):
        value = data.get(key)
        if isinstance(value, str) and chr(0) not in value and (key != 'folder' or value.strip()):
            result[key] = value
    return result

def load():
    if not CONFIG_PATH.exists():
        return dict(DEFAULTS)
    try:
        return validate(json.loads(CONFIG_PATH.read_text(encoding='utf-8-sig')))
    except (ValueError, OSError) as exc:
        raise ConfigError(str(exc)) from exc

def save(cfg):
    temporary = None
    try:
        CONFIG_PATH.parent.mkdir(parents=True, exist_ok=True)
        with tempfile.NamedTemporaryFile(mode='w', encoding='utf-8', dir=CONFIG_PATH.parent, delete=False) as file:
            temporary = Path(file.name)
            json.dump(validate(cfg), file, ensure_ascii=False, indent=2)
            file.flush()
            os.fsync(file.fileno())
        os.replace(temporary, CONFIG_PATH)
    except OSError as exc:
        raise ConfigError(str(exc)) from exc
    finally:
        if temporary is not None:
            temporary.unlink(missing_ok=True)
