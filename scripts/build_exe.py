#!/usr/bin/env python3
"""
Build script for creating standalone executable
"""

import subprocess
import sys
import os


def build_exe():
    """Build the executable using PyInstaller"""
    try:
        # Run PyInstaller with the spec file
        cmd = [sys.executable, "-m", "PyInstaller", "streamlit_app.spec", "--clean"]
        print(f"Running: {' '.join(cmd)}")
        result = subprocess.run(cmd, check=True, capture_output=True, text=True)
        print("Build successful!")
        print(f"Executable created at: dist/libro-diario-converter.exe")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Build failed: {e}")
        print(f"stdout: {e.stdout}")
        print(f"stderr: {e.stderr}")
        return False


if __name__ == "__main__":
    success = build_exe()
    sys.exit(0 if success else 1)

