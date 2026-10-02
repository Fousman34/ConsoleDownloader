"""Discover portable tools first, then installed tools."""
import shutil
import subprocess
import sys
from pathlib import Path


def tool(name):
    roots = [Path(sys.executable).parent] if getattr(sys, 'frozen', False) else []
    roots += [Path(getattr(sys, '_MEIPASS', Path(__file__).parent))]
    for root in roots:
        for directory in (root / 'tools', root):
            candidate = directory / (name + ('.exe' if sys.platform == 'win32' else ''))
            if candidate.is_file():
                return str(candidate)
    return shutil.which(name)


def diagnostics():
    result = {}
    for name in ('ffmpeg', 'ffprobe', 'deno', 'node'):
        path = tool(name)
        if path:
            try:
                process = subprocess.run([path, '-version' if name.startswith('ff') else '--version'],
                                         capture_output=True, text=True, timeout=10,
                                         creationflags=subprocess.CREATE_NO_WINDOW if sys.platform == 'win32' else 0)
                result[name] = (process.stdout or process.stderr).splitlines()[0] if process.returncode == 0 else 'ERROR'
            except (OSError, subprocess.TimeoutExpired, IndexError):
                result[name] = 'ERROR'
        else:
            result[name] = 'MISSING'
    return result
