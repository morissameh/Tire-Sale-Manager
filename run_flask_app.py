import webbrowser
import subprocess
import time
from sys import platform

def open_browser(url):
    webbrowser.open_new(url)

def run_server():
    """ Run the Flask application. """
    command = 'flask run'
    # Windows specific settings to hide the command prompt
    return subprocess.Popen(command)

def main():
    flask_process = run_server()
    time.sleep(2)  # Wait for Flask to start before opening the browser
    url = 'http://127.0.0.1:5000'
    open_browser(url)

if __name__ == '__main__':
    main()
