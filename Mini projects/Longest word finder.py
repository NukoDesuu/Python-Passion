##### Tool that "Find the longest word" from the input (omitting comma, endl, fullstop) version 2

txtfile = open("E:\\Nono\\Programming\\LOCAL FILES\\NukoNote2.txt")
txt = txtfile.read().replace("\n\n", " ").replace("\n", "").replace(",", "").replace(".","").lower()

print("\nWords sample : \n" + txt + "\n")

words = txt.split(" ")

print("Word elements : \n" + str(words) + "\n")

char = []
wordsc = {}

for i in words:
    c = len(i)
    char.append(c)
    if c in wordsc:
        old = wordsc[c]
        if i in old:
            continue
        else:
            new = "{0}, {1}".format(old, i)
            wordsc[c] = new
    else:
        wordsc[c] = i
    

print("Character counts for each word :\n" + str(char) + "\n")
print("Character/Word pairs : \n" + str(wordsc) + "\n")

maxc = max(char)
maxcwrd = wordsc.get(maxc).split(",")
maxcwrd2 = ",".join(maxcwrd)

if len(maxcwrd) > 1:
    s = "s"
    be = "are"
else:
    s = ""
    be = "is"

print("The longest word{0} {1} : {2} ({3} character{4})\n".format(s, be, maxcwrd2, maxc, s))

#####