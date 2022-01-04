import tkinter as tk

class Spinner:
    def __init__(self, mainWindow):
        self.mainWindow = mainWindow
        mainWindow.title("Spinner")
        self.num = 0

        self.text = tk.Label(mainWindow, text = self.num, width = 15, height = 3)
        self.text.grid(row = 2, column = 1)

        self.plusButton = tk.Button(mainWindow, text = "+", width = 10, command = self.countUp)
        self.plusButton.grid(row = 1, column = 2)

        self.minusButton = tk.Button(mainWindow, text = "-", width = 10, command = self.countDown)
        self.minusButton.grid(row = 2, column = 2)

        self.resetButton = tk.Button(mainWindow, text = "Reset", width = 10, command = self.reset)
        self.resetButton.grid(row = 3, column = 2)

    def countUp(self):
        self.num += 1
        self.text.config(text = self.num)

    def countDown(self):
        self.num -= 1
        self.text.config(text = self.num)
    
    def reset(self):
        self.num = 0
        self.text.config(text = self.num)

mainWindow = tk.Tk()
app = Spinner(mainWindow)
mainWindow.mainloop()