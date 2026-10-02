import io
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import config
import yt_dlp
from downloader import _build_format, build_options, download, DownloadFailed
from i18n import TRANS, set_lang
from rich.console import Console
from urls import normalize_url


class AppTests(unittest.TestCase):
    def test_youtube_links_and_spoofed_hosts(self):
        for url in ('youtu.be/BaW_jenozKc', 'https://www.youtube.com/watch?v=BaW_jenozKc&list=abc',
                    'https://m.youtube.com/shorts/BaW_jenozKc', 'https://youtube.com/live/BaW_jenozKc'):
            self.assertEqual(normalize_url(url), 'https://www.youtube.com/watch?v=BaW_jenozKc')
        for url in ('https://youtube.com.evil.org/watch?v=BaW_jenozKc',
                    'https://evil.org/youtube.com', 'https://youtube.com/playlist?list=abc',
                    'https://youtube.com@evil.org/watch?v=BaW_jenozKc', '',
                    'file://youtube.com/watch?v=BaW_jenozKc', 'https://youtu.be/abc'):
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
        self.assertEqual(set(TRANS['ru']), set(TRANS['en']))

    def test_no_final_file_does_not_report_success(self):
        set_lang('en')
        with tempfile.TemporaryDirectory() as folder, patch('downloader.yt_dlp.YoutubeDL') as cls:
            cls.return_value.__enter__.return_value.extract_info.return_value = {'title': 'test'}
            with self.assertRaises(DownloadFailed):
                download('https://youtu.be/BaW_jenozKc', 'best', folder, console=Console(file=io.StringIO()))


if __name__ == '__main__':
    unittest.main()
