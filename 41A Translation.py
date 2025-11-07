#Input: two words.
#Output: YES if the second word is the reversed of the first one; NO otherwise.

originalWord = input()
maybeReversedWord = input()

reversed = list(originalWord)                   #Turn the string into a list, reversed it and turn it back into a string for comparison.
reversed.reverse()
reversed = "".join(reversed)

if reversed == maybeReversedWord:
    print("YES")
else:
    print("NO")
