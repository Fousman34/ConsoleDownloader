"""Real HTTP downloads and FFmpeg processing using generated, temporary media."""
import functools
import io
import subprocess
import tempfile
import threading
import unittest
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from unittest.mock import patch

from rich.console import Console
from downloader import DownloadFailed, download
from i18n import set_lang, t
from runtime import tool


class QuietHandler(SimpleHTTPRequestHandler):
    def log_message(self, *args):
        pass

    def copyfile(self, source, output):
        # Generic extraction closes its sniffing request before downloading again.
        try:
            super().copyfile(source, output)
        except (ConnectionResetError, BrokenPipeError):
            pass


@unittest.skipUnless(tool('ffmpeg') and tool('ffprobe'), 'Install FFmpeg for HTTP integration tests')
class HttpDownloadTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.temp = tempfile.TemporaryDirectory()
        cls.root = Path(cls.temp.name)
        try:
            subprocess.run([tool('ffmpeg'), '-v', 'error', '-f', 'lavfi', '-i',
                            'testsrc2=size=1280x720:rate=24', '-f', 'lavfi', '-i',
                            'sine=frequency=440', '-t', '1', '-c:v', 'libx264',
                            '-preset', 'ultrafast', '-c:a', 'aac', str(cls.root / 'video.mp4')],
                           check=True, capture_output=True, timeout=30)
            (cls.root / 'empty.html').write_text('<html><body>No video here</body></html>')
            (cls.root / 'fake.mp4').write_text('<html><body>Access denied</body></html>')
            (cls.root / 'player.html').write_text('<html><video src="video.mp4" controls></video></html>')
            cls.server = ThreadingHTTPServer(('127.0.0.1', 0), functools.partial(QuietHandler, directory=str(cls.root)))
            cls.thread = threading.Thread(target=cls.server.serve_forever, daemon=True)
            cls.thread.start()
            cls.base = f'http://127.0.0.1:{cls.server.server_port}/'
        except Exception:
            cls.temp.cleanup()
            raise

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()
        cls.server.server_close()
        cls.thread.join(timeout=5)
        cls.temp.cleanup()

    def setUp(self):
        set_lang('en')

    def fetch(self, path, quality='best'):
        # Direct files and generic HTML players must work without Node/Deno.
        with tempfile.TemporaryDirectory() as output, patch('downloader.tool',
                side_effect=lambda name: tool(name) if name.startswith('ff') else None):
            result = download(self.base + path, quality, output, console=Console(file=io.StringIO()))
            self.assertTrue(result['saved_files'])
            for name in result['saved_files']:
                self.assertGreater(Path(name).stat().st_size, 1000)
            return result

    def test_direct_video_and_quality_with_unknown_metadata(self):
        self.fetch('video.mp4?token=signed%2Fvalue', '720')

    def test_generic_html_player(self):
        self.fetch('player.html')

    def test_audio_conversion(self):
        result = self.fetch('video.mp4', 'mp3')
        self.assertTrue(all(name.endswith('.mp3') for name in result['saved_files']))

    def test_invalid_page_and_missing_video_are_errors(self):
        for path, expected in [('empty.html', 'err_unsupported'), ('missing.mp4', 'err_unavailable')]:
            with self.subTest(path=path), self.assertRaises(DownloadFailed) as error:
                self.fetch(path)
            self.assertIn(t(expected), str(error.exception))

    def test_disguised_html_is_not_success(self):
        with self.assertRaises(DownloadFailed):
            self.fetch('fake.mp4')

    def test_unknown_metadata_cannot_bypass_actual_height_limit(self):
        with self.assertRaises(DownloadFailed) as error:
            self.fetch('video.mp4', '360')
        self.assertIn(t('err_height'), str(error.exception))
