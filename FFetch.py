import os
import sys
import subprocess
import tempfile
import shutil
import urllib.request
import ctypes
import time
import winreg

def is_admin():
    """Check if running with admin privileges"""
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def run_as_admin():
    """Relaunch the script with admin rights"""
    if sys.executable:
        ctypes.windll.shell32.ShellExecuteW(
            None, "runas", sys.executable, " ".join(sys.argv), None, 1
        )
    else:
        ctypes.windll.shell32.ShellExecuteW(
            None, "runas", sys.argv[0], " ".join(sys.argv[1:]), None, 1
        )
    sys.exit(0)

def add_to_path(path_to_add):
    """Add directory to system PATH"""
    try:
        # Access registry
        reg = winreg.ConnectRegistry(None, winreg.HKEY_LOCAL_MACHINE)
        key = winreg.OpenKey(
            reg,
            r"SYSTEM\CurrentControlSet\Control\Session Manager\Environment",
            0,
            winreg.KEY_READ | winreg.KEY_WRITE
        )
        
        # Get current PATH
        current_path, _ = winreg.QueryValueEx(key, "Path")
        
        # Check if already in PATH
        if path_to_add in current_path:
            return
        
        # Update PATH
        new_path = current_path + ";" + path_to_add
        winreg.SetValueEx(key, "Path", 0, winreg.REG_EXPAND_SZ, new_path)
        winreg.CloseKey(key)
        winreg.CloseKey(reg)
        
        # Broadcast environment change
        ctypes.windll.user32.SendMessageTimeoutW(0xFFFF, 0x1A, 0, "Environment", 0, 1000, None)
        return True
    except Exception as e:
        print(f"PATH update failed: {e}")
        return False

def main():
    # Check admin rights
    if not is_admin():
        run_as_admin()
        return

    print("FFetch - FFmpeg Installer for Windows\n")

    # Configuration
    FFMPEG_URL = "https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-full.7z"
    TARGET_DIR = r"C:\Program Files\ffmpeg"
    SEVEN_ZIP_PATH = r"C:\Program Files\7-Zip\7z.exe"
    BIN_DIR = os.path.join(TARGET_DIR, "bin")
    
    try:
        # Create target directory
        os.makedirs(TARGET_DIR, exist_ok=True)
        
        # Create temp directory
        temp_dir = tempfile.mkdtemp(prefix="ffmpeg_")
        download_path = os.path.join(temp_dir, "ffmpeg-release-full.7z")
        
        # Download FFmpeg
        print("[*] Downloading FFmpeg release (this may take several minutes)...")
        try:
            urllib.request.urlretrieve(FFMPEG_URL, download_path)
            print("[+] Download completed successfully")
        except Exception as e:
            print(f"[!] Download failed: {str(e)}")
            raise

        # Verify 7-Zip installation
        if not os.path.exists(SEVEN_ZIP_PATH):
            print("\n[!] 7-Zip not found at default location")
            print("[*] Please install 7-Zip from https://www.7-zip.org/")
            raise FileNotFoundError("7-Zip not installed")
        
        # Extract archive
        print("[*] Extracting files...")
        try:
            subprocess.run(
                [SEVEN_ZIP_PATH, "x", download_path, f"-o{TARGET_DIR}", "-aoa", "-y"],
                check=True,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL
            )
        except subprocess.CalledProcessError:
            print("[!] Extraction failed. Possible reasons:")
            print("    - Corrupted download")
            print("    - Insufficient disk space")
            print("    - 7-Zip compatibility issue")
            raise

        # Find extracted folder
        extracted_folder = None
        for entry in os.listdir(TARGET_DIR):
            full_path = os.path.join(TARGET_DIR, entry)
            if os.path.isdir(full_path) and entry.lower().startswith("ffmpeg-"):
                extracted_folder = full_path
                break
        
        if not extracted_folder:
            raise FileNotFoundError("FFmpeg folder not found in extracted files")
        
        # Move bin directory
        src_bin = os.path.join(extracted_folder, "bin")
        if not os.path.exists(src_bin):
            raise FileNotFoundError("Bin directory missing in FFmpeg package")
        
        # Remove existing bin if present
        if os.path.exists(BIN_DIR):
            shutil.rmtree(BIN_DIR)
        
        shutil.move(src_bin, TARGET_DIR)
        
        # Cleanup
        shutil.rmtree(extracted_folder)
        os.remove(download_path)
        os.rmdir(temp_dir)
        
        # Add to system PATH
        print("[*] Updating system PATH...")
        if add_to_path(BIN_DIR):
            print("[+] Added to system PATH successfully")
        else:
            print("[!] Failed to update PATH via registry. Using setx fallback...")
            subprocess.run(["setx", "/M", "PATH", f"%PATH%;{BIN_DIR}"], check=True)
        
        # Success message
        print("\n[+] FFmpeg installed successfully!")
        print(f"Location: {TARGET_DIR}")
        print("Note: You might need to restart your system for PATH changes to fully propagate")
        
        # Open browser
        print("\nOpening project links...")
        subprocess.Popen(["cmd", "/c", "start", "https://github.com/MaDTiA"], shell=False)
        subprocess.Popen(["cmd", "/c", "start", "https://madtia.cc"], shell=False)
        
        print("\nThanks for using FFetch!")
        print("Press Enter to exit...")
        input()
        
    except Exception as e:
        print(f"\n[!] Installation failed: {str(e)}")
        print("Possible solutions:")
        print(" - Run as Administrator")
        print(" - Install 7-Zip (64-bit) from https://www.7-zip.org/")
        print(" - Check internet connection")
        print(" - Ensure sufficient disk space (500MB+ free)")
        input("\nPress Enter to exit...")
        sys.exit(1)

if __name__ == "__main__":
    main()
