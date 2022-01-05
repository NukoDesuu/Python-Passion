def Problem1_1():
    print("Problem 1.1")

def Problem1_2():
    pass

def Problem1_3():
    pass

def Problem2():
    pass

def Problem3():
    pass

def Problem4():
    pass



problem_list = {
    "1.1" : Problem1_1,
    "1.2" : Problem1_2,
    "1.3" : Problem1_3,
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