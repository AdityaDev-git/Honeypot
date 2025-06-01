import time
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class DecoyEventHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if not event.is_directory:
            logging.warning(f"Decoy file modified: {event.src_path}")
            print(f"[!] Decoy file modified: {event.src_path}")

    def on_deleted(self, event):
        if not event.is_directory:
            logging.warning(f"Decoy file deleted: {event.src_path}")
            print(f"[!] Decoy file deleted: {event.src_path}")

    def on_opened(self, event):
        if not event.is_directory:
            logging.warning(f"Decoy file opened: {event.src_path}")
            print(f"[!] Decoy file opened: {event.src_path}")

def start_decoy_monitoring(folder="decoys"):
    event_handler = DecoyEventHandler()
    observer = Observer()
    observer.schedule(event_handler, folder, recursive=False)
    observer.start()
    print("[+] Decoy file monitoring started.")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
