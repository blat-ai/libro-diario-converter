import os
import sys
import webbrowser
import threading
import time
from pathlib import Path

def resource_path(relative_path):
    """Get absolute path to resource, works for dev and for PyInstaller bundle."""
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def open_browser():
    """Open browser after a short delay to ensure server is running."""
    time.sleep(2)
    webbrowser.open('http://localhost:8501')

def main():
    """Launch Streamlit app with proper configuration for Windows executable."""
    try:
        # Set environment variables for Streamlit
        os.environ['STREAMLIT_BROWSER_GATHER_USAGE_STATS'] = 'false'
        os.environ['STREAMLIT_SERVER_HEADLESS'] = 'true'
        os.environ['STREAMLIT_SERVER_ADDRESS'] = 'localhost'
        os.environ['STREAMLIT_SERVER_PORT'] = '8501'
        
        # Import Streamlit components
        import streamlit.web.cli as stcli
        
        # Get the path to the streamlit app
        app_path = resource_path('app/streamlit_app.py')
        
        # Start browser in a separate thread
        browser_thread = threading.Thread(target=open_browser)
        browser_thread.daemon = True
        browser_thread.start()
        
        # Configure sys.argv for Streamlit
        sys.argv = [
            "streamlit",
            "run",
            app_path,
            "--server.port=8501",
            "--server.address=localhost",
            "--server.headless=true",
            "--browser.gatherUsageStats=false"
        ]
        
        # Launch Streamlit
        sys.exit(stcli.main())
        
    except Exception as e:
        print(f"Error launching application: {e}")
        input("Press Enter to exit...")
        sys.exit(1)

if __name__ == "__main__":
    main()