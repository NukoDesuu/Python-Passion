def Problem1():
    pass

def Problem2():
    pass

def Problem3():
    pass

def Problem4():
    pass

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