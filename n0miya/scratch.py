dicts = {12: "TEST1, TEST2"}

print(len(dicts.get(12).split(","))) # 2

if len(dicts.get(12).split(",")) > 1:
    print("There is more than one element!")