import tkinter as tk

def print_nya():
    print("Nya~")

mainWindow = tk.Tk()

button1 = tk.Button(mainWindow, text="Press to pet neko!", height=5, width=30, command=print_nya)
button1.grid()

mainWindow.mainloop()