import tkinter as tk
from tkinter.filedialog import askopenfile, asksaveasfile
from tkinter import Button, WORD, INSERT, END

def saveFile():
    new_file = asksaveasfile(mode="w", defaultextension=".txt", filetypes=[('Text files', '*.txt')])
    if new_file is None:
        return
    text = str(entry.get(1.0, END))
    new_file.write(text)
    new_file.close()

def openFile():
    file = askopenfile(mode='r', filetypes=[('Text files', '*.txt')])
    if file is not None:
        content = file.read()
        entry.delete(1.0, END)  # Clear the current content before inserting new content
        entry.insert(INSERT, content)

def clearFile():
    entry.delete(1.0, END)

canvas = tk.Tk()
canvas.geometry("400x600")
canvas.title("Notepad")
canvas.config(bg="white")
top = tk.Frame(canvas)
top.pack(padx=10, pady=5, anchor='nw')

b1 = Button(canvas, text="Open", bg='white', command=openFile)
b1.pack(in_=top, side=tk.LEFT)

b2 = Button(canvas, text="Save", bg='white', command=saveFile)
b2.pack(in_=top, side=tk.LEFT)

b3 = Button(canvas, text="Clear", bg='white', command=clearFile)
b3.pack(in_=top, side=tk.LEFT)

b4 = Button(canvas, text="Exit", bg='white', command=canvas.quit)
b4.pack(in_=top, side=tk.LEFT)

entry = tk.Text(canvas, wrap=WORD, bg="#F9DDA4", font=("Poppins", 15))
entry.pack(padx=10, pady=5, expand=True, fill=tk.BOTH)

canvas.mainloop()
