import random

class Maid:
    def __init__ (self, name, height, weight):
        self.n = name
        self.h = height
        self.w = weight

    def ReportBio(self):
        print(f"My name is... {self.n}. \nI'm {self.h} cm tall and weighs {self.w} kg.")

    def coom(self):
        print("Anh~ huh~ iku-iku!")


class Muku(Maid):
    def call(self):
        calls = ["Mk1", "Mk2", "Mk3"]
        return print(random.choice(calls))


class Majime(Maid):
    def call(self):
        calls = ["Mj1", "Mj2", "Mj3"]
        return print(random.choice(calls))


class Rindere(Maid):
    def call(self):
        calls = ["Rd1", "Rd2", "Rd3"]
        return print(random.choice(calls))


Mochi = Muku("Mochi", 153, 46)
Chocola = Muku("Chocola", 151, 45)

Mochi.call()
Chocola.ReportBio()

Chocola.coom()