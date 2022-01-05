def concatenate(*args):
    ans = ""
    for element in args:
        ans += element + "-"
    return ans.removesuffix("-")

print(concatenate("I", "love", "Python", "!"))


def concatenate(*args):
    return "-".join(args)

print(concatenate("I", "love", "Python", "!"))