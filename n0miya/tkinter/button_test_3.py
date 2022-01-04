import tkinter as tk

mainWindow = tk.Tk()

label1 = tk.Label(mainWindow, text="I'm happy!", height=5, width=30)
label1.grid()

button1 = tk.Button(mainWindow, text="Press me!", height=5, width=30, command=
                    lambda :[label1.config(text="I'm sleepy!"), print("A button has been pressed!")])
button1.grid()

mainWindow.mainloop()