from cryptography.fernet import Fernet
import os
import tkinter as tk
from tkinter import messagebox

def get_key():
    try:
        with open('fernet_key.key', 'rb') as key_file:
            key = key_file.read()
        print(f"Key used for encryption: {key}")
    except FileNotFoundError:
        key = Fernet.generate_key()
        with open('fernet_key.key', 'wb') as key_file:
            key_file.write(key)
        print(f"Generated new encryption key: {key}")
    return key

def encrypt_file(file_path, key):
    fernet = Fernet(key)
    with open(file_path, 'rb') as file:
        file_data = file.read()
    encrypted_data = fernet.encrypt(file_data)
    with open(file_path, 'wb') as file:
        file.write(encrypted_data)
    print(f"Encrypted {file_path} successfully.")
    show_popup(file_path)

def show_popup(file_path):
    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo(
        "File Encrypted",
        f"The file {file_path} has been successfully encrypted.\n\n"
        "Encryption performed by: Your Name\n"
        "Encryption Date: Today's Date\n\n"
        "Details: The file is now secure and cannot be accessed without decryption."
    )
    root.quit()

key = get_key()
encrypt_file('/home/sec-lab/Documents/first.txt', key)
encrypt_file('/home/sec-lab/Documents/Photo', key)
