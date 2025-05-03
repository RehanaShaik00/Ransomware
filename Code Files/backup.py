import shutil
import os
import tkinter as tk
from tkinter import messagebox

def backup_files():
    source_files = [
        '/home/sec-lab/Documents/first.txt',
        '/home/sec-lab/Documents/Photo'
    ]
    backup_folder = '/home/sec-lab/Desktop/'

    if not os.path.exists(backup_folder):
        os.makedirs(backup_folder)

    for file_path in source_files:
        try:
            file_name = os.path.basename(file_path)
            destination = os.path.join(backup_folder, file_name)
            shutil.copy2(file_path, destination)
            print(f"Successfully backed up: {file_name}")
        except Exception as e:
            print(f"Failed to back up {file_path}. Error: {e}")
            show_error_popup(f"Failed to back up {file_path}. Error: {e}")
            return

    show_popup("Backup Successful", "The files have been successfully backed up to the Desktop.")

def show_popup(title, message):
    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo(title, message)
    root.quit()

def show_error_popup(message):
    root = tk.Tk()
    root.withdraw()
    messagebox.showerror("Error", message)
    root.quit()

if __name__ == "__main__":
    backup_files()
