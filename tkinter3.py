import tkinter as tk

def button_clicked():
    label.config(text="Button was clicked!")

root = tk.Tk()
root.title("Button Example")

label = tk.Label(root, text="Click the button")
label.pack(pady=10)

button = tk.Button(root, text="Click Me", command=button_clicked)
button.pack(pady=10)

root.mainloop()
