### Vowel characters counter with ratio comparing only vowels sample version 2

def charlock(text, target):
    hits = 0
    for i in text:
        if i == target:
            hits += 1
    return hits

try:
    with open("E:\\Nono\\Programming\\LOCAL FILES\\NukoNote.txt") as textfile:
        cont = textfile.read()
except UnicodeDecodeError:
    print("Unicode character detected! Please try again...\n")

samp = []
tot = len(cont)

for ch in "aeiou":
    samp.append(charlock(cont, ch))


samsum = sum(samp)

print("\nVowel ratios(count)...\n")
print("Total characters : " + str(tot))
print("Total vowels : " + str(samsum) + "\n")

ind = 0

for ch in "aeiou":
    perc = (charlock(cont, ch) / samsum) * 100
    perco = round(perc, 3)
    print("{0} : {1}% ({2})".format(ch, perco, samp[ind]))
    ind += 1

print()

#####

##### Tool that "Find the longest word" from the input (omitting comma)

txt = input()

#your code goes here
words = txt.split(" ")
char = []
wordsc = {}

for i in words:
    x = len(i)
    if "," in i:
        x -= 1
    
    char.append(x)
    wordsc[x] = i

maxc = max(char)
maxw = wordsc[maxc]

print(maxw)

#####