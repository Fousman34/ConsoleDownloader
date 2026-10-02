"""Accept individual YouTube videos, never arbitrary hosts or playlists."""
import re
from urllib.parse import parse_qs, urlsplit


def normalize_url(value):
    value = value.strip()
    if '://' not in value:
        value = 'https://' + value
    try:
        parsed = urlsplit(value)
        if parsed.scheme not in ('http', 'https') or parsed.username or parsed.password or parsed.port not in (None, 80, 443):
            raise ValueError('url')
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
                raise ValueError('url')
        else:
            raise ValueError('url')
        if not re.fullmatch(r'[A-Za-z0-9_-]{11}', video_id):
            raise ValueError('url')
        return 'https://www.youtube.com/watch?v=' + video_id
    except (ValueError, TypeError) as exc:
        raise ValueError('Invalid YouTube video URL') from exc
