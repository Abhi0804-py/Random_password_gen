# Random Password Generator

This is a simple password generator GUI application built using Python's `tkinter` module. Users can generate secure, random passwords with options to include letters, digits, and special characters, as well as copy the generated password to the clipboard.

## Features

- Customizable password length (1 to 100 characters).
- Options to include/exclude:
  - Letters (uppercase and lowercase).
  - Digits (0-9).
  - Symbols (!, @, #, etc.).
- Displays the generated password in a text box.
- Allows copying the password to the clipboard.
- Error handling for invalid selections.

## Requirements

- Python 3.x
- `tkinter` (pre-installed with Python)
- `pyperclip` (Install using `pip install pyperclip`)

## How to Run

1. Install the `pyperclip` library:
    ```bash
    pip install pyperclip
    ```
2. Navigate to the project directory:
    ```bash
    cd random-password-generator
    ```
3. Run the application:
    ```bash
    python password_generator.py
    ```
