"""Validate HTTP(S) links while preserving signed and site-specific URLs."""
import re
from urllib.parse import parse_qs, urlsplit


def normalize_url(value):
    if not isinstance(value, str):
        raise ValueError('Invalid video URL')
    value = value.strip()
    if not value or re.search(r'[\s\x00-\x1f\x7f]', value):
        raise ValueError('Invalid video URL')
    if '://' not in value:
        value = 'https://' + value
    try:
        parsed = urlsplit(value)
        if parsed.scheme not in ('http', 'https') or not parsed.hostname or parsed.username or parsed.password:
            raise ValueError('url')
        parsed.port
        host = (parsed.hostname or '').lower()
        if host == 'youtu.be':
            video_id = parsed.path.strip('/')
        elif host in ('youtube.com', 'www.youtube.com', 'm.youtube.com', 'music.youtube.com', 'www.youtube-nocookie.com', 'youtube-nocookie.com'):
            parts = parsed.path.strip('/').split('/')
            if parsed.path == '/watch':
                video_id = parse_qs(parsed.query).get('v', [''])[0]
            elif len(parts) == 2 and parts[0] in ('shorts', 'live', 'embed'):
                video_id = parts[1]
            else:
                return value
        else:
            return value
        if not re.fullmatch(r'[A-Za-z0-9_-]{11}', video_id):
            raise ValueError('url')
        return 'https://www.youtube.com/watch?v=' + video_id
    except (ValueError, TypeError) as exc:
        raise ValueError('Invalid video URL') from exc
