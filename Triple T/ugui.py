def beninnins():
    import tkinter as tk
    from tkinter import messagebox

    # Function to handle button click
    def beninnings():
        ans = name_entry.get().strip().lower()
        if not ans:
            messagebox.showwarning("Input Error", "Wake up?")
            return
        elif ans!='no':
            messagebox.showinfo("Greetings", "Hello, Triple T!")
        else:
            messagebox.showinfo('GAME OVER', 'GAME OVER')

    # Create the main application window
    root = tk.Tk()
    root.title('tungtungtung sahur')
    root.geometry("200x150")  # Width x Height

    # Create a label
    label = tk.Label(root, text="Wake up?", font=("Sitka Display", 12))
    label.pack(pady=10)

    # Create a text entry field
    name_entry = tk.Entry(root, font=("Mongolian Baiti", 12))
    name_entry.pack(pady=5)

    # Create a button
    greet_button = tk.Button(root, text="Answer", font=("Times New Roman", 12), command=beninnings)
    greet_button.pack(pady=10)

    # Start the Tkinter event loop
    root.mainloop()