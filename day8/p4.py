import tkinter as tk
root = tk.Tk()

FONT = ("Arial", 12, "bold")

def handleSubmit():
    message = tk.Label(root, text="Hello " + entry.get(), font=FONT)
    message.pack()

root.geometry("300x300")
root.title("My First GUI")
label = tk.Label(root, text="Name", font=FONT)
entry = tk.Entry(root, width=30, font=FONT)
entry.place(x=150, y=100)
label.place(x=100, y=100)
button = tk.Button(root, text="Submit", command=handleSubmit, font=FONT)
button.place(x=140, y=150)
root.mainloop()