import random as rnd

class Maid:
    def __init__ (self, name, height, weight):
        self.n = name
        self.h = height
        self.w = weight
    def ReportBio(self):
        return print("My name is... {0}. \nI'm {1} cm tall and weighs {2} kg.".format(self.n, self.h, self.w))

class Muku(Maid):
    def call(self):
        calls = ["Mk1", "Mk2", "Mk3"]
        return print(rnd.choice(calls))

class Majime(Maid):
    def call(self):
        calls = ["Mj1", "Mj2", "Mj3"]
        return print(rnd.choice(calls))

class Rindere(Maid):
    def call(self):
        calls = ["Rd1", "Rd2", "Rd3"]
        return print(rnd.choice(calls))

Mochi = Muku("Mochi", 153, 46)
Chocola = Muku("Chocola", 151, 45)

Mochi.call()
Chocola.ReportBio()