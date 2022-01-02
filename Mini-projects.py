### Vowel characters counter with ratio comparing only vowels sample

def charlock(text, target):
    hits = 0
    for i in text:
        if i == target:
            hits += 1
    return hits

#Replace ??? with your file path
with open("???") as textfile:
    cont = textfile.read()

samp = []

for ch in "aeiou":
    samp.append(charlock(cont, ch))

samsum = sum(samp)

print("\nVowel ratios(count)...\n")

ind = 0

for ch in "aeiou":
    perc = (charlock(cont, ch) / samsum) * 100
    perco = round(perc, 3)
    print("{0} : {1}% ({2})".format(ch, perco, samp[ind]))
    ind += 1

print()

#####