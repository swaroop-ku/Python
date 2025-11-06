import tkinter as tk

def show_input():
    user_text = entry.get()
    label.config(text=f"You entered: {user_text}")

root = tk.Tk()
root.title("Entry Example")

entry = tk.Entry(root, width=30)
entry.pack(pady=10)

button = tk.Button(root, text="Submit", command=show_input)
button.pack(pady=5)

label = tk.Label(root, text="")
label.pack(pady=10)

root.mainloop()
