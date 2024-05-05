import tkinter as tk
from tkinter import ttk

def caesar_cipher(text, shift):
    """Encrypts or decrypts the given text using the Caesar Cipher algorithm."""
    result = ""
    for char in text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            result += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
        else:
            result += char
    return result

def encrypt_text():
    """Encrypts the text using the Caesar Cipher."""
    text = entry_text.get("1.0", "end-1c")
    shift = int(entry_shift.get())
    encrypted_text = caesar_cipher(text, shift)
    entry_text.delete("1.0", "end")
    entry_text.insert("1.0", encrypted_text)

def decrypt_text():
    """Decrypts the text using the Caesar Cipher."""
    text = entry_text.get("1.0", "end-1c")
    shift = int(entry_shift.get())
    decrypted_text = caesar_cipher(text, -shift)
    entry_text.delete("1.0", "end")
    entry_text.insert("1.0", decrypted_text)

# Create the main window
root = tk.Tk()
root.title("Caesar Cipher")
root.geometry("500x300")

# Create widgets
label_text = tk.Label(root, text="Enter the text:")
entry_text = tk.Text(root, height=5, width=40)
label_shift = tk.Label(root, text="Enter the shift value:")
entry_shift = tk.Entry(root)
button_encrypt = tk.Button(root, text="Encrypt", command=encrypt_text)
button_decrypt = tk.Button(root, text="Decrypt", command=decrypt_text)

# Place widgets using grid layout
label_text.grid(row=0, column=0, padx=10, pady=10, sticky="w")
entry_text.grid(row=1, column=0, padx=10, pady=5)
label_shift.grid(row=2, column=0, padx=10, pady=10, sticky="w")
entry_shift.grid(row=3, column=0, padx=10, pady=5)
button_encrypt.grid(row=4, column=0, padx=10, pady=10, sticky="ew")
button_decrypt.grid(row=5, column=0, padx=10, pady=10, sticky="ew")

# Run the application
root.mainloop()
