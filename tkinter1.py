import tkinter as tk

root = tk.Tk()
root.title("Checkbutton Example")

var = tk.BooleanVar()

def show_choice():
    if var.get():
        label.config(text="Checkbox is checked")
    else:
        label.config(text="Checkbox is unchecked")

check = tk.Checkbutton(root, text="Accept Terms", variable=var, command=show_choice)
check.pack(pady=10)

label = tk.Label(root, text="")
label.pack(pady=10)

root.mainloop()
