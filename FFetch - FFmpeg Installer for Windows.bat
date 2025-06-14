@echo off
setlocal enabledelayedexpansion

echo [*] Downloading FFmpeg release zip...
set "FFMPEG_ZIP_URL=https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-full.7z"
set "TEMP_DIR=%TEMP%\ffmpeg_download"
set "TARGET_DIR=C:\Program Files\ffmpeg"

if not exist "%TEMP_DIR%" mkdir "%TEMP_DIR%"
cd /d "%TEMP_DIR%"

powershell -Command "Invoke-WebRequest -Uri '%FFMPEG_ZIP_URL%' -OutFile 'ffmpeg-release-full.7z'"
if errorlevel 1 (
    echo [!] Failed to download FFmpeg. Aborting.
    exit /b 1
)

echo [*] Extracting archive...
if not exist "%ProgramFiles%\7-Zip\7z.exe" (
    echo [!] 7-Zip is required but not found in "%ProgramFiles%\7-Zip\7z.exe"
    echo [*] Please install 7-Zip from https://www.7-zip.org/ and re-run this script.
    exit /b 1
)

"%ProgramFiles%\7-Zip\7z.exe" x ffmpeg-release-full.7z -aoa -o"%TARGET_DIR%"

echo [*] Locating ffmpeg bin path...
for /d %%i in ("%TARGET_DIR%\ffmpeg-*") do (
    set "FFMPEG_EXTRACTED=%%i"
)

move /y "!FFMPEG_EXTRACTED!\bin" "%TARGET_DIR%\bin" >nul
rd /s /q "!FFMPEG_EXTRACTED!"

echo [*] Adding FFmpeg to system PATH...
setx /M PATH "%PATH%;%TARGET_DIR%\bin" >nul

echo  FFmpeg installed to "%TARGET_DIR%" and added to PATH.
echo  You may need to restart your terminal or system for PATH changes to take effect.

echo.
echo  Thanks for using my tool!
echo  Visit: https://github.com/MaDTiA
start "" "https://github.com/MaDTiA"
start "" "https://madtia.cc"
pause
