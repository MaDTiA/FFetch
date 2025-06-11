# FFetch - FFmpeg Installer for Windows

<p align="center">
  <img src="https://i.ibb.co/WvpzrtLG/FFetch-FFmpeg-Installer-for-Windows.png" alt="FFetch Logo" width="250"/>
</p>

A simple and reliable way to install FFmpeg on Windows with minimal effort.

**FFetch** is a batch script that automatically downloads, extracts, and installs the latest full release of FFmpeg for Windows. It sets up FFmpeg in `C:\Program Files\ffmpeg` and updates the system `PATH`, so you can use FFmpeg from any terminal or script.

---

## 🚀 Features

* 🔽 Downloads the latest **full** FFmpeg release from [gyan.dev](https://www.gyan.dev/ffmpeg/builds/)
* 📦 Extracts it using 7-Zip
* 📁 Installs to `C:\Program Files\ffmpeg`
* ✅ Automatically adds FFmpeg to your system `PATH`
* ⚡️ **GPU-ready out of the box** – includes support for NVIDIA/CUDA and other hardware encoders
  👉 *No need to compile or mess with custom builds!*

---

## ✅ Requirements

* 🖥️ Windows OS
* 📦 [7-Zip](https://www.7-zip.org/) installed at `C:\Program Files\7-Zip` (used for extraction)

---

## 🔧 Installation

1. Download `FFetch.bat` or `FFetch.exe` from this repository.
2. **Right-click → Run as administrator**.
3. Let the script do the work:

   * Downloads FFmpeg
   * Extracts it
   * Installs it
   * Adds it to your `PATH`

---

## 🧪 After Installation

To verify everything is set up:

```bash
ffmpeg -version
```

You should see FFmpeg output with support for hardware acceleration like `cuda`, `nvenc`, `qsv`, etc.

Use it like this:

```bash
ffmpeg -i input.mp4 output.avi
```

### 🔥 GPU Example (NVIDIA):

```bash
ffmpeg -hwaccel cuda -i input.mp4 -c:v h264_nvenc output.mp4
```

That’s it, you're now ready for hardware accelerated encoding without compiling a single line.

---

## 🙌 Author

Made with 💻 by **MaDTiA**
<br>
🌐 [https://github.com/MaDTiA](https://github.com/MaDTiA)
<br>
🧠 [https://madtia.cc](https://madtia.cc)

---

Let me know if you want a matching `CHANGELOG.md`, GitHub Actions auto-build, or a `ffetch.exe` builder added to the repo!
