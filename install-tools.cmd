@echo off
setlocal
echo Video Downloader - console application by Fousman34
echo Installing FFmpeg using the Windows package manager...
winget install --id Gyan.FFmpeg --exact --source winget
if errorlevel 1 (
    echo Installation failed or FFmpeg is already installed.
    echo Check README.md for manual installation instructions.
    pause
    exit /b 1
)
echo Close this window and start YouTubeDownloader.exe in a new terminal.
pause
