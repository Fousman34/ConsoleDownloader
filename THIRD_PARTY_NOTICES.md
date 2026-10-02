# Third-party components

The Windows build includes the Python runtime, Python packages listed
in requirements-lock.txt, Node.js, FFmpeg and ffprobe. Their respective licenses
apply independently. License texts collected from installed packages are in
the licenses directory. This notice is not a replacement for those licenses.

* Python: PSF license — https://www.python.org/psf/license/
* yt-dlp: Unlicense; see wheel license text — https://github.com/yt-dlp/yt-dlp
* yt-dlp-ejs: see bundled package license — https://github.com/yt-dlp/ejs
* Rich: MIT — https://github.com/Textualize/rich
* Questionary: MIT — https://github.com/tmbo/questionary
* Node.js: MIT plus bundled third-party licenses — https://github.com/nodejs/node
* FFmpeg: this Gyan full build is GPL; its license and build README are included
  in licenses. Source/build information: https://www.gyan.dev/ffmpeg/builds/
  and https://ffmpeg.org/legal.html

* Mutagen: GPL-2.0-or-later; corresponding source is included in release
  dependency-sources/ — https://github.com/quodlibet/mutagen
* certifi: MPL-2.0; corresponding source is included in release
  dependency-sources/ — https://github.com/certifi/python-certifi

The downloadable GitHub EXE release does NOT bundle FFmpeg or ffprobe.
Install them separately using install-tools.cmd or the instructions in README.
The local developer build contains those binaries for testing; its FFmpeg
license/build notices are retained here for reference.
The project source is GPL-3.0-only; see LICENSE and NOTICE. Dependencies retain
their own licenses and copyright notices. Unmodified Mutagen and certifi source
archives accompany the EXE release, along with this application's source.
