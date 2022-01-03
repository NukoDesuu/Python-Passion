### Vowel characters counter with ratio comparing only vowels sample version 3

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
letters = "aeiou"

for ch in letters:
    samp.append(charlock(cont, ch))


samsum = sum(samp)

print("\nVowel ratios(count)...\n")
print("Total characters : " + str(tot))
print("Total vowels : " + str(samsum) + "\n")

ind = 0

for ch in letters:
    perc = (charlock(cont, ch) / samsum) * 100
    perco = round(perc, 3)
    print("{0} : {1}% ({2})".format(ch, perco, samp[ind]))
    ind += 1

print()

#####