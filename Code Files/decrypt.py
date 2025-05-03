from cryptography.fernet import Fernet, InvalidToken
import os
import tkinter as tk
from tkinter import messagebox
import base64

def get_key():
    try:
        with open('fernet_key.key', 'rb') as key_file:
            key = key_file.read()
        print(f"Key used for decryption: {key}")
    except FileNotFoundError:
        raise Exception("Encryption key not found. Please run the encryption process first.")
    return key

def decrypt_file(file_path, key):
    fernet = Fernet(key)
    with open(file_path, 'rb') as file:
        encrypted_data = file.read()
    print(f"Encrypted data for {file_path} (Base64): {base64.b64encode(encrypted_data)[:100]}")
    try:
        decrypted_data = fernet.decrypt(encrypted_data)
        with open(file_path, 'wb') as file:
            file.write(decrypted_data)
        print(f"Decrypted {file_path} successfully.")
        show_popup(file_path)
    except InvalidToken as e:
        print(f"Decryption failed for {file_path}. Invalid token error: {str(e)}")
        show_error_popup(file_path, "Decryption failed. Invalid key or data was tampered with.")
    except Exception as e:
        print(f"Decryption failed for {file_path}. Error: {str(e)}")
        show_error_popup(file_path, str(e))

def show_popup(file_path):
    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo(
        "File Decrypted",
        f"The file {file_path} has been successfully decrypted.\n\n"
        "Decryption performed by: Your Name\n"
        "Decryption Date: Today's Date\n\n"
        "Details: The file is now restored to its original form."
    )
    root.quit()

def show_error_popup(file_path, error_message):
    root = tk.Tk()
    root.withdraw()
    messagebox.showerror(
        "Decryption Failed",
        f"Failed to decrypt the file {file_path}.\n\nError: {error_message}"
    )
    root.quit()

key = get_key()
decrypt_file('/home/sec-lab/Documents/first.txt', key)
decrypt_file('/home/sec-lab/Documents/Photo', key)
