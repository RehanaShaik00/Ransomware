from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
import tkinter as tk
from tkinter import messagebox
from datetime import datetime

class Watcher(FileSystemEventHandler):
    def on_modified(self, event):
        if event.is_directory:
            return
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        event_details = f"Event: File Modified\nFile: {event.src_path}\nTimestamp: {timestamp}"
        show_popup(event_details)

    def on_created(self, event):
        if event.is_directory:
            return
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        event_details = f"Event: File Created\nFile: {event.src_path}\nTimestamp: {timestamp}"
        show_popup(event_details)

    def on_deleted(self, event):
        if event.is_directory:
            return
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        event_details = f"Event: File Deleted\nFile: {event.src_path}\nTimestamp: {timestamp}"
        show_popup(event_details)

def show_popup(event_details):
    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo("File Event", event_details)
    root.quit()

if __name__ == "__main__":
    path = '/home/sec-lab/Documents'
    event_handler = Watcher()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    print(f"Monitoring started on {path}...")
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
