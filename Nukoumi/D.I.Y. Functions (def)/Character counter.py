#Detects total occurences of the "target"-ed character
def charlock(text, target):
    hits = 0
    for i in text:
        if i == target:
            hits += 1
    return hits