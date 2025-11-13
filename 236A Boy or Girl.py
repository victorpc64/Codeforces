#Input: a name.
#Output: if the count of distinct characters is even "CHAT WITH HER"; if it's odd "IGNORE HIM!"

name = input()
distinctCharacters = {c for c in name}      #Adds every distinct character in name

if len(distinctCharacters) % 2 != 0:    #Checks if odd
    print("IGNORE HIM!")
else:
    print("CHAT WITH HER!")