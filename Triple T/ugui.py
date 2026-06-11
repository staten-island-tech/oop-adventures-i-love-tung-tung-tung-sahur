def beninnings():
    import tkinter as tk
    from tkinter import messagebox

    # Function to handle button click
    def beninnins():
        messagebox.showinfo("Greetings", "Hello, Triple T!")
    def begiggigs():
        messagebox.showinfo('GAME OVER', 'GAME OVER')

    # Create the main application window
    root = tk.Tk()
    root.title('tungtungtung sahur')
    root.geometry('100x150')  # Width x Height

    # Create a label
    label = tk.Label(root, text="Wake up?", font=("Sitka Display", 12))
    label.pack(pady=10)

    # Create a text entry field
    

    # Create a button
    yes = tk.Button(root, text="Yes", font=("Times New Roman", 12), command=beninnins)
    yes.pack(pady=10)
    no= tk.Button(root, text="No", font=("Times New Roman", 12), command=begiggigs)
    no.pack(pady=10)

    # Start the Tkinter event loop
    root.mainloop()
beninnings()