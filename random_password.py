import tkinter as tk
from tkinter import messagebox
import random
import string
import pyperclip

def generate_password():
    length = length_var.get()
    use_letters = letters_var.get()
    use_digits = digits_var.get()
    use_symbols = symbols_var.get()

    character_set = ''
    if use_letters:
        character_set += string.ascii_letters
    if use_digits:
        character_set += string.digits
    if use_symbols:
        character_set += string.punctuation

    if not character_set:
        messagebox.showerror("Error", "At least one character set must be selected.")
        return

    password = ''.join(random.choice(character_set) for _ in range(length))
    password_var.set(password)

def copy_to_clipboard():
    password = password_var.get()
    if password:
        pyperclip.copy(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")
    else:
        messagebox.showwarning("Warning", "No password to copy!")

# Initialize the main window
root = tk.Tk()
root.title("Random Password Generator")

# Password length label and spinbox
length_label = tk.Label(root, text="Password Length:")
length_label.grid(row=0, column=0, padx=10, pady=10)
length_var = tk.IntVar(value=12)
length_spinbox = tk.Spinbox(root, from_=1, to_=100, textvariable=length_var, width=5)
length_spinbox.grid(row=0, column=1, padx=10, pady=10)

# Checkbuttons for character types
letters_var = tk.BooleanVar(value=True)
digits_var = tk.BooleanVar(value=True)
symbols_var = tk.BooleanVar(value=True)

letters_check = tk.Checkbutton(root, text="Include Letters", variable=letters_var)
letters_check.grid(row=1, column=0, padx=10, pady=5)

digits_check = tk.Checkbutton(root, text="Include Digits", variable=digits_var)
digits_check.grid(row=1, column=1, padx=10, pady=5)

symbols_check = tk.Checkbutton(root, text="Include Symbols", variable=symbols_var)
symbols_check.grid(row=2, column=0, padx=10, pady=5)

# Generate button
generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.grid(row=2, column=1, padx=10, pady=10)

# Entry to display the generated password
password_var = tk.StringVar()
password_entry = tk.Entry(root, textvariable=password_var, width=40)
password_entry.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Copy to clipboard button
copy_button = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.grid(row=4, column=0, columnspan=2, pady=10)

# Run the application
root.mainloop()
