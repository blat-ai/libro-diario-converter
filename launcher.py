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
    # Setup logging
    import logging
    log_file = os.path.join(os.path.expanduser("~"), "libro-diario-converter.log")
    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
    
    try:
        logging.info("Starting Libro Diario Converter application")
        
        # Set environment variables for Streamlit
        os.environ['STREAMLIT_BROWSER_GATHER_USAGE_STATS'] = 'false'
        os.environ['STREAMLIT_SERVER_HEADLESS'] = 'true'
        os.environ['STREAMLIT_SERVER_ADDRESS'] = 'localhost'
        os.environ['STREAMLIT_SERVER_PORT'] = '8501'
        logging.info("Set Streamlit environment variables")
        
        # Import Streamlit components
        import streamlit.web.cli as stcli
        
        # Get the path to the streamlit app
        app_path = resource_path('app/streamlit_app.py')
        logging.info(f"Using app path: {app_path}")
        
        # Set config directory to use bundled config
        config_path = resource_path('app/.streamlit')
        os.environ['STREAMLIT_CONFIG_DIR'] = config_path
        logging.info(f"Using config path: {config_path}")
        
        # Start browser in a separate thread
        browser_thread = threading.Thread(target=open_browser)
        browser_thread.daemon = True
        browser_thread.start()
        logging.info("Started browser thread")
        
        # Configure sys.argv for Streamlit
        sys.argv = [
            "streamlit",
            "run",
            app_path,
            "--global.developmentMode=false"
        ]
        
        logging.info("Launching Streamlit with args: " + str(sys.argv))
        # Launch Streamlit
        sys.exit(stcli.main())
        
    except Exception as e:
        logging.error(f"Error launching application: {e}", exc_info=True)
        print(f"Error occurred. Check log file: {log_file}")
        sys.exit(1)

if __name__ == "__main__":
    main()