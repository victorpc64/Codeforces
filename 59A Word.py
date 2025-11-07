#Input: a word with mixed upper and lower characters
#Output: the word with all upper if there's more upper characters than lower; all lower otherwise

word = input()
upperCounter = 0
lowerCounter = 0

for i in word:
    if i.isupper():
        upperCounter += 1
    else:
        lowerCounter += 1

if upperCounter > lowerCounter:
    print(word.upper())
else:
    print(word.lower())