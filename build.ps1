param([switch]$Zip, [string]$DistRoot = 'dist\publish')
$ErrorActionPreference = 'Stop'
Set-Location -LiteralPath $PSScriptRoot
$distPath = [IO.Path]::GetFullPath((Join-Path $PSScriptRoot $DistRoot))
if (-not $distPath.StartsWith($PSScriptRoot + [IO.Path]::DirectorySeparatorChar, [StringComparison]::OrdinalIgnoreCase)) { throw 'Build output must stay inside the project folder.' }
$pythonPath = Join-Path $PSScriptRoot '.venv\Scripts\python.exe'
if (-not (Test-Path -LiteralPath $pythonPath)) { $pythonPath = Join-Path (Split-Path $PSScriptRoot -Parent) '.venv\Scripts\python.exe' }
if (-not (Test-Path -LiteralPath $pythonPath)) { throw 'Run setup.cmd first.' }
& $pythonPath -c 'import PyInstaller'
if ($LASTEXITCODE -ne 0) { throw 'Install PyInstaller in the development environment.' }
& $pythonPath -m PyInstaller --noconfirm --onedir --console --distpath $distPath --name YouTubeDownloader --collect-all yt_dlp --collect-all yt_dlp_ejs main.py
if ($LASTEXITCODE -ne 0) { throw 'Build failed.' }
$outputPath = Join-Path $distPath 'YouTubeDownloader'
$toolsPath = Join-Path $outputPath 'tools'
New-Item -ItemType Directory -Path $toolsPath -Force | Out-Null
foreach ($toolName in @('ffmpeg', 'ffprobe', 'node')) {
    $command = Get-Command $toolName -ErrorAction Stop
    Copy-Item -LiteralPath $command.Source -Destination $toolsPath -Force
}
Copy-Item -LiteralPath 'README.md', 'VERIFICATION.md', 'THIRD_PARTY_NOTICES.md', 'requirements-lock.txt', 'LICENSE', 'NOTICE' -Destination $outputPath -Force
if (Test-Path -LiteralPath 'licenses') { Copy-Item -LiteralPath 'licenses' -Destination $outputPath -Recurse -Force }
& (Join-Path $outputPath 'YouTubeDownloader.exe') --doctor
if ($LASTEXITCODE -ne 0) { throw 'Packaged dependency check failed.' }
if ($Zip) { Compress-Archive -LiteralPath $outputPath -DestinationPath (Join-Path $PSScriptRoot 'dist\YouTubeDownloader-Windows-x64.zip') -Force }
