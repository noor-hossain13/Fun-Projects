"""
Universal Media Downloader - Desktop Application
Creates a native desktop window with web UI
"""

import webview
import threading
from app import app

def run_flask():
    """Run Flask server in background"""
    app.run(port=5000, debug=False)

if __name__ == "__main__":
    # Start Flask server in a background thread
    flask_thread = threading.Thread(target=run_flask)
    flask_thread.daemon = True
    flask_thread.start()

    # Create and show the desktop window
    webview.create_window(
        title="Media Downloader",
        url="http://127.0.0.1:5000",
        width=600,
        height=500,
        resizable=False
    )
    webview.start()