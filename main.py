import os
import threading
import logging
import tkinter as tk
from flask import Flask
from servers.ftp_server import run_ftp_server
from servers.http_server import run_http_server
from decoys.decoy_manager import create_decoy_files
from decoys.decoy_watcher import start_decoy_monitoring



# Ensure decoys and logs folders exist
os.makedirs('decoys', exist_ok=True)
os.makedirs('logs', exist_ok=True)

# Logging setup
logging.basicConfig(
    filename='logs/honeypot.log',
    level=logging.INFO,
    format='%(asctime)s %(levelname)s:%(message)s'
)
logging.info("Honeypot started.")

# --- Flask HTTP honeypot setup ---
# app = Flask(__name__)

# @app.route('/')
# def index():
#     return "<h1>Welcome to Admin Portal</h1><p>Restricted Access.</p>"

# def run_http_server():
#     app.run(host='0.0.0.0', port=8080, debug=False, use_reloader=False)

#-------------decoy----------
def start_servers():
    create_decoy_files()
    threading.Thread(target=start_decoy_monitoring, daemon=True).start()
    threading.Thread(target=run_http_server, daemon=True).start()
    threading.Thread(target=run_ftp_server, daemon=True).start()
    print("[+] HTTP and FTP Servers started")
    logging.info("HTTP and FTP servers started. Decoy files created.")

# --- Tkinter GUI setup ---
def start_servers():
    threading.Thread(target=run_http_server, daemon=True).start()
    threading.Thread(target=run_ftp_server, daemon=True).start()
    print("[+] HTTP Server started on port 8080")

def stop_servers():
    # For now, we can't programmatically stop Flask easily without hacking it.
    # We'll improve this later by using gunicorn or waitress servers.
    print("[-] Stop not yet implemented. Close the app manually.")

# GUI window
root = tk.Tk()
root.title("Python Honeypot Controller")
root.geometry("300x150")

start_button = tk.Button(root, text="Start Honeypot", command=start_servers)
start_button.pack(pady=10)

stop_button = tk.Button(root, text="Stop Honeypot", command=stop_servers)
stop_button.pack(pady=10)

root.mainloop()
