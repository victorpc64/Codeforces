#Input: a word that can have upper and lower case letters.
#Output: same word with only the first letter changed to upper.

word = input()

result = word[0].upper() + word[1:]     #Extracts the first letter and make upper and append the original word from the second letter.
print(result)