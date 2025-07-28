@echo off
echo Installing dependencies...
pip install -r requirements.txt

echo Building executable...
pyinstaller streamlit_app.spec --clean

echo Build complete! Check dist/ folder for libro-diario-converter.exe
pause