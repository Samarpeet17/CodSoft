import tkinter as tk
import random
import string

class PasswordGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")

        self.password_length = tk.IntVar()
        self.password_length.set(8)

        self.include_lower = tk.BooleanVar()
        self.include_lower.set(True)

        self.include_upper = tk.BooleanVar()
        self.include_upper.set(True)

        self.include_digits = tk.BooleanVar()
        self.include_digits.set(True)

        self.include_symbols = tk.BooleanVar()
        self.include_symbols.set(True)

        self.password_label = tk.Label(self.root, text="Password Length:")
        self.password_label.pack()

        self.password_entry = tk.Entry(self.root, textvariable=self.password_length)
        self.password_entry.pack()

        self.lower_checkbox = tk.Checkbutton(self.root, text="Include Lowercase", variable=self.include_lower)
        self.lower_checkbox.pack()

        self.upper_checkbox = tk.Checkbutton(self.root, text="Include Uppercase", variable=self.include_upper)
        self.upper_checkbox.pack()

        self.digits_checkbox = tk.Checkbutton(self.root, text="Include Digits", variable=self.include_digits)
        self.digits_checkbox.pack()

        self.symbols_checkbox = tk.Checkbutton(self.root, text="Include Symbols", variable=self.include_symbols)
        self.symbols_checkbox.pack()

        self.generate_button = tk.Button(self.root, text="Generate Password", command=self.generate_password)
        self.generate_button.pack()

        self.result_label = tk.Label(self.root, text="")
        self.result_label.pack()

    def generate_password(self):
        length = self.password_length.get()
        include_lower = self.include_lower.get()
        include_upper = self.include_upper.get()
        include_digits = self.include_digits.get()
        include_symbols = self.include_symbols.get()

        password = self.generate_random_password(length, include_lower, include_upper, include_digits, include_symbols)
        self.result_label.config(text=password)

    def generate_random_password(self, length, include_lower, include_upper, include_digits, include_symbols):
        characters = ''
        if include_lower:
            characters += string.ascii_lowercase
        if include_upper:
            characters += string.ascii_uppercase
        if include_digits:
            characters += string.digits
        if include_symbols:
            characters += string.punctuation

        if not characters:
            return "Please select at least one character type."

        password = ''.join(random.choice(characters) for _ in range(length))
        return password

root = tk.Tk()
root.geometry("300x300")
password_generator = PasswordGenerator(root)
root.mainloop()
