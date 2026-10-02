@echo off
setlocal
chcp 65001 >nul
cd /d "%~dp0"
if exist "dist\publish\YouTubeDownloader\YouTubeDownloader.exe" (
    "dist\publish\YouTubeDownloader\YouTubeDownloader.exe" %*
) else if exist "dist\YouTubeDownloader\YouTubeDownloader.exe" (
    "dist\YouTubeDownloader\YouTubeDownloader.exe" %*
) else if exist ".venv\Scripts\python.exe" (
    ".venv\Scripts\python.exe" main.py %*
) else (
    echo Run setup.cmd first.
    pause
    exit /b 1
)
if errorlevel 1 pause
