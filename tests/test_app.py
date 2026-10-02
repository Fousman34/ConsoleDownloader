import io
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import config
import yt_dlp
from downloader import _build_format, build_options, download, DownloadFailed, _explain_error, _verify_media
from i18n import LANGUAGES, TRANS, set_lang, t
from rich.console import Console
from urls import normalize_url


class AppTests(unittest.TestCase):
    def test_web_links_and_youtube_normalization(self):
        for url in ('youtu.be/BaW_jenozKc', 'https://www.youtube.com/watch?v=BaW_jenozKc&list=abc',
                    'https://m.youtube.com/shorts/BaW_jenozKc', 'https://youtube.com/live/BaW_jenozKc'):
            self.assertEqual(normalize_url(url), 'https://www.youtube.com/watch?v=BaW_jenozKc')
        for url in ('https://vkvideo.ru/video-1_2', 'https://rutube.ru/video/abc/',
                    'https://example.org/movie.mp4?token=a%2Fb&expires=123',
                    'http://localhost:8765/movie.mp4', 'https://youtube.com.evil.org/watch?v=abc'):
            self.assertEqual(normalize_url(url), url)
        for url in ('https://youtube.com@evil.org/watch?v=BaW_jenozKc', '',
                    'file://youtube.com/watch?v=BaW_jenozKc', 'https://youtu.be/abc',
                    'https://', 'javascript:alert(1)', 'https://example.org:99999/a',
                    'https://example.org/a\nb', None):
            with self.assertRaises(ValueError):
                normalize_url(url)

    def test_settings_round_trip_and_validation(self):
        with tempfile.TemporaryDirectory() as folder, patch.object(config, 'CONFIG_PATH', Path(folder) / 'settings.json'):
            settings = dict(config.DEFAULTS, lang='ru', folder='C:/Видео [test]')
            config.save(settings)
            self.assertEqual(config.load(), settings)
            config.CONFIG_PATH.write_text('{"quality":"oops", "folder":[], "lang":"xx"}')
            self.assertEqual(config.load(), config.DEFAULTS)
            config.CONFIG_PATH.write_text('broken')
            with self.assertRaises(config.ConfigError):
                config.load()

    def test_save_failure_is_reported(self):
        with tempfile.TemporaryDirectory() as folder, patch.object(config, 'CONFIG_PATH', Path(folder)):
            with self.assertRaises(config.ConfigError):
                config.save(config.DEFAULTS)

    def test_quality_never_exceeds_ceiling(self):
        formats = [dict(format_id=str(h), height=h, ext='mp4', vcodec='h264', acodec='aac',
                        url='https://example.org/video.mp4', protocol='https') for h in (360, 720, 1080)]
        with yt_dlp.YoutubeDL({'quiet': True}) as ydl:
            selector = ydl.build_format_selector(_build_format('720')[0])
            selected = list(selector({'formats': formats, 'has_merged_format': True, 'incomplete_formats': False}))
            self.assertTrue(selected)
            self.assertLessEqual(selected[0]['height'], 720)
            selected = list(selector({'formats': formats[2:], 'has_merged_format': True, 'incomplete_formats': False}))
            self.assertEqual(selected, [])

    def test_missing_ffmpeg_fails_before_network(self):
        with patch('downloader.tool', return_value=None):
            with self.assertRaises(DownloadFailed):
                build_options('720', '.')

    def test_translation_keys_match(self):
        self.assertEqual(len(LANGUAGES), 7)
        for lang in LANGUAGES:
            self.assertEqual(set(TRANS['ru']), set(TRANS[lang]))
            self.assertTrue(all(TRANS[lang].values()))
            self.assertEqual(config.validate({'lang': lang})['lang'], lang)

    def test_errors_are_explained_in_every_language(self):
        for lang in LANGUAGES:
            set_lang(lang)
            for error, key in [('Unsupported URL: example', 'err_unsupported'),
                               ('HTTP Error 403: Forbidden', 'err_access'),
                               ('HTTP Error 404: Not Found', 'err_unavailable'),
                               ('This video is DRM protected', 'err_drm'),
                               ('Requested format is not available', 'err_format'),
                               ('Connection timed out', 'err_network')]:
                self.assertIn(t(key), _explain_error(yt_dlp.utils.DownloadError(error)))
        set_lang('en')

    def test_js_runtime_is_optional_for_non_youtube_sites(self):
        with patch('downloader.tool', side_effect=lambda name: '/tools/' + name if name.startswith('ff') else None):
            self.assertEqual(build_options('best', '.')['js_runtimes'], {})

    def test_playlist_rejected_before_downloading(self):
        with tempfile.TemporaryDirectory() as folder, patch('downloader.yt_dlp.YoutubeDL') as cls:
            ydl = cls.return_value.__enter__.return_value
            ydl.extract_info.return_value = {'_type': 'playlist', 'entries': []}
            with self.assertRaises(DownloadFailed):
                download('https://example.org/collection', 'best', folder, console=Console(file=io.StringIO()))
            ydl.process_ie_result.assert_not_called()

    def test_media_validation_rejects_html_and_height_excess(self):
        with patch('downloader.subprocess.run') as run:
            run.return_value.returncode = 0
            run.return_value.stdout = '{"streams": []}'
            with self.assertRaises(DownloadFailed):
                _verify_media('fake.mp4', 'best')
            run.return_value.stdout = '{"streams": [{"codec_type": "video", "height": 1080}]}'
            with self.assertRaises(DownloadFailed):
                _verify_media('movie.mp4', '720')
            _verify_media('movie.mp4', 'best')
            run.return_value.stdout = '{"streams": [{"codec_type": "audio"}]}'
            _verify_media('sound.mp3', 'mp3')

    def test_no_final_file_does_not_report_success(self):
        set_lang('en')
        with tempfile.TemporaryDirectory() as folder, patch('downloader.yt_dlp.YoutubeDL') as cls:
            cls.return_value.__enter__.return_value.process_ie_result.return_value = {'title': 'test'}
            with self.assertRaises(DownloadFailed):
                download('https://youtu.be/BaW_jenozKc', 'best', folder, console=Console(file=io.StringIO()))


if __name__ == '__main__':
    unittest.main()
