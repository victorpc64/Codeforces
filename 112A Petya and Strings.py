#Input: two lines of strings.
#Output: -1 if the first one is first in the dictionary, 0 if they're equal, 1 if the second comes first. Not case sensitive.

line1 = input()
line2 = input()

line1 = line1.lower()       #Both strings to lower for the comparison
line2 = line2.lower()

if line1 == line2:      #Python compares lexicographically with operators =, < and >
    print(0)
elif line1 < line2:
    print(-1)
else:
    print(1)