file = open("books.txt", "r")

for line in file.readlines():
    print(f"{line.strip()[0]}{len(line.strip())}")

# Another solution if you're one line boi (not recommended!)
# print(*[f"{line.strip()[0]}{len(line.strip())}" for line in file.readlines()], sep="\n")

file.close()