#Input: the number of elements of the second line. A line with a sequence of 0 and 1.
#Output: if there's a 1, "HARD"; else "EASY"

n = input()     #Never used
line = input()

if line.find('1') != -1:    #Returns -1 if doesn't find any
    print("HARD")
else:
    print("EASY")