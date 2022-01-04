import tkinter as tk

mainWindow = tk.Tk()

button1 = tk.Button(mainWindow, text="Press to pet neko!", height=5, width=30, command=lambda :print("Nya~"))
button1.grid()

mainWindow.mainloop()