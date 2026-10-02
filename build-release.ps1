param([string]$Version = '1.1.0', [string]$BuiltDirectory = 'dist\publish\YouTubeDownloader')
$ErrorActionPreference = 'Stop'
Set-Location -LiteralPath $PSScriptRoot
if ($Version -notmatch '^\d+\.\d+\.\d+$') { throw 'Version must be X.Y.Z.' }
$builtPath = [IO.Path]::GetFullPath((Join-Path $PSScriptRoot $BuiltDirectory))
if (-not $builtPath.StartsWith($PSScriptRoot + [IO.Path]::DirectorySeparatorChar, [StringComparison]::OrdinalIgnoreCase)) { throw 'Build path must stay inside the project folder.' }
if (-not (Test-Path -LiteralPath (Join-Path $builtPath 'YouTubeDownloader.exe'))) { throw 'Run build.ps1 first.' }
$sourcePath = Join-Path $PSScriptRoot 'build\dependency-sources'
foreach ($name in @('mutagen-1.48.1.tar.gz', 'certifi-2026.7.22.tar.gz')) {
    if (-not (Test-Path -LiteralPath (Join-Path $sourcePath $name))) { throw 'Download Mutagen/certifi source archives as documented in README.' }
}
$stagingPath = Join-Path $PSScriptRoot ('build\release-' + [guid]::NewGuid().ToString('N'))
$appPath = Join-Path $stagingPath 'VideoDownloader'
New-Item -ItemType Directory -Path $appPath -Force | Out-Null
Copy-Item -LiteralPath (Join-Path $builtPath 'YouTubeDownloader.exe'), (Join-Path $builtPath '_internal') -Destination $appPath -Recurse
New-Item -ItemType Directory -Path (Join-Path $appPath 'tools') | Out-Null
Copy-Item -LiteralPath (Join-Path $builtPath 'tools\node.exe') -Destination (Join-Path $appPath 'tools')
Copy-Item -LiteralPath 'README.md', 'VERIFICATION.md', 'LICENSE', 'NOTICE', 'THIRD_PARTY_NOTICES.md', 'requirements-lock.txt', 'install-tools.cmd', 'licenses' -Destination $appPath -Recurse
Copy-Item -LiteralPath $sourcePath -Destination (Join-Path $appPath 'dependency-sources') -Recurse
$archivePath = Join-Path $PSScriptRoot ('dist\VideoDownloader-' + $Version + '-Source.zip')
git archive --format=zip "--output=$archivePath" HEAD
if ($LASTEXITCODE -ne 0) { throw 'Source archive failed.' }
Expand-Archive -LiteralPath $archivePath -DestinationPath (Join-Path $appPath 'source')
if (Get-ChildItem -LiteralPath $appPath -Recurse -File | Where-Object { $_.Name -in @('ffmpeg.exe', 'ffprobe.exe') }) { throw 'FFmpeg must be installed separately for this release.' }
$zipPath = Join-Path $PSScriptRoot ('dist\VideoDownloader-' + $Version + '-Windows-x64.zip')
Compress-Archive -LiteralPath $appPath -DestinationPath $zipPath -Force
$hashes = Get-FileHash -LiteralPath $zipPath, $archivePath -Algorithm SHA256
$hashes | ForEach-Object { $_.Hash.ToLower() + '  ' + (Split-Path $_.Path -Leaf) } | Set-Content -LiteralPath (Join-Path $PSScriptRoot 'dist\SHA256SUMS.txt') -Encoding ascii
Write-Output $zipPath
Write-Output $archivePath
