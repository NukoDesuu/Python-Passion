import math as m
import turtle as t
import time

def Problem1():
    
    w = 2
    x = 3
    y = 4
    z = 5
    ans = x**3 + y * (z / 2) - w
    print(str(ans) + "\n")
    return

def Problem2():

    r = float(input("Please input the radius of the cylinder (in meter): "))
    l = float(input("Please input the length of the cylinder (in meter): "))

    area = round(m.pi * (r**2), 3)
    volume = round(area * l, 3)

    print("This cylinder has the area of {0} m^2 and volume of {1} m^3\n".format(area, volume))

def Problem3():

    i = 0
    t.pd()
    time.sleep(5)

    while i<5:
        t.fd(100)
        time.sleep(0.5)
        t.lt(60)
        time.sleep(0.5)
        i += 1
    t.fd(100)
    print("Please click on the screen to exit window.")
    t.exitonclick()

def Problem4():
    #statements
    pass


#General format for question reviewing...

problem_list = {
    "1" : Problem1,
    "2" : Problem2,
    "3" : Problem3,
    "4" : Problem4
}

while True:
    ec = len(problem_list)
    p = input("Select the problem you want to check ({0} problems) or 'exit' to exit the program : ".format(ec))
    if p in problem_list:
        q = problem_list[p]
        q()
    elif p == "exit":
        exit()
    else:
        try:
            p = int(p)
            print("That question number doesn't exists!")
        except ValueError:
            print("Please enter number, not characters!")