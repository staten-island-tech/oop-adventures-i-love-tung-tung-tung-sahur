import tkinter as tk
from tkinter import messagebox

# Function to handle button click
def greet_user():
    name = name_entry.get().strip()
    if not name:
        messagebox.showwarning("Input Error", "Please enter your name.")
        return
    messagebox.showinfo("Greeting", f"Hello, {name}!")

# Create the main application window
root = tk.Tk()
root.title("Simple GUI Example")
root.geometry("300x200")  # Width x Height

# Create a label
label = tk.Label(root, text="Enter your name:", font=("Sitka Display", 12))
label.pack(pady=10)

# Create a text entry field
name_entry = tk.Entry(root, font=("Mongolian Baiti", 12))
name_entry.pack(pady=5)

# Create a button
greet_button = tk.Button(root, text="Greet Me", font=("Times New Roman", 12), command=greet_user)
greet_button.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()