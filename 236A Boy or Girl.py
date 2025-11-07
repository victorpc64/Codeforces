#Input: a name.
#Output: if the count of distinct characters is even "CHAT WITH HER"; if it's odd "IGNORE HIM!"
#Maybe I should have implement it with a set instead of a list.

name = input()
distinctCharacters = []     #Initialize an empty list

for i in name:      #Runs through all characters in name
    if i not in distinctCharacters:     
        distinctCharacters.append(i)    #Adds the character if it's distinct

if len(distinctCharacters) % 2 != 0:    #Checks if odd
    print("IGNORE HIM!")
else:
    print("CHAT WITH HER!")