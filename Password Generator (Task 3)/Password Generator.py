import tkinter as tk
from tkinter import ttk
import random
import string

class PasswordGeneratorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Password Generator")
        self.master.geometry("400x250")
        self.master.configure(bg="#F0F0F0")

        self.username_label = ttk.Label(master, text="Username:")
        self.username_label.grid(row=0, column=0, padx=10, pady=10, sticky='w')

        self.username_var = tk.StringVar()
        self.username_entry = ttk.Entry(master, textvariable=self.username_var)
        self.username_entry.grid(row=0, column=1, padx=10, pady=10, columnspan=2, sticky='ew')

        self.length_label = ttk.Label(master, text="Password Length:")
        self.length_label.grid(row=1, column=0, padx=10, pady=10, sticky='w')

        self.length_var = tk.StringVar()
        self.length_entry = ttk.Entry(master, textvariable=self.length_var)
        self.length_entry.grid(row=1, column=1, padx=10, pady=10, columnspan=2, sticky='ew')

        self.generate_button = ttk.Button(master, text="Generate Password", command=self.generate_password)
        self.generate_button.grid(row=2, column=0, columnspan=3, pady=10, sticky='ew')

        self.password_label = ttk.Label(master, text="Generated Password:")
        self.password_label.grid(row=3, column=0, columnspan=3, pady=10, sticky='w')

        self.result_var = tk.StringVar()
        self.password_entry = ttk.Entry(master, textvariable=self.result_var, state="readonly", font=('Helvetica', 12), justify='center')
        self.password_entry.grid(row=4, column=0, columnspan=3, pady=10, sticky='ew')

        # Configure column weights for proper resizing
        for i in range(3):
            self.master.grid_columnconfigure(i, weight=1)

        # Configure row weights for proper resizing
        for i in range(5):
            self.master.grid_rowconfigure(i, weight=1)

    def generate_password(self):
        try:
            password_length = int(self.length_var.get())
            if password_length <= 0:
                raise ValueError("Password length must be greater than 0")

            password = self.generate_random_password(password_length)
            self.result_var.set(password)
        except ValueError as ve:
            self.result_var.set("Invalid input: " + str(ve))

    def generate_random_password(self, length):
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        return password

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
