# FFetch - FFmpeg Installer for Windows
<p align="center">
  <img src="https://i.ibb.co/WvpzrtLG/FFetch-FFmpeg-Installer-for-Windows.png" alt="FFetch Logo" width="250"/>
</p>

A simple and reliable way to install FFmpeg on Windows with minimal effort.

FFetch is a batch script that automatically downloads, extracts, and installs the latest full release of FFmpeg for Windows. It sets up FFmpeg in `C:\Program Files\ffmpeg` and updates the system PATH so you can use FFmpeg from any terminal window.

## Features

* Downloads the latest FFmpeg release from gyan.dev
* Extracts using 7-Zip
* Installs to `C:\Program Files\ffmpeg`
* Adds FFmpeg to your system PATH

## Requirements

* Windows OS
* 7-Zip installed at `C:\Program Files\7-Zip` (required for extraction)

## Installation

1. Download the `FFetch.bat` or  `FFetch.exe` file from this repository.
2. Right-click on the file and select "Run as administrator".
3. Follow the prompts. The script will:

   * Download the latest FFmpeg full release archive
   * Extract it to the target location
   * Add FFmpeg to your system PATH

## After Installation

Once the script has finished and you have restarted your terminal, you should be able to run:

```
ffmpeg -version
```

This confirms that FFmpeg is correctly installed.

You can then start using FFmpeg as usual. Example:

```
ffmpeg -i input.mp4 output.avi
```

Or if you want to test GPU acceleration (NVIDIA example):

```
ffmpeg -hwaccel cuda -i input.mp4 -c:v h264_nvenc output.mp4
```

## Author

Made by MaDTiA

GitHub: [https://github.com/MaDTiA](https://github.com/MaDTiA)
Website: [https://madtia.cc](https://madtia.cc)
