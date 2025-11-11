#Input: the number of elements of the second line. A line with a sequence of 0 and 1.
#Output: if there's a 1, "HARD"; else "EASY"
#¿Sería más claro si el comentario fuera Find returns -1 if it doesn't find any y programarlo en positivo find('1') == -1 -> easy else hard?

n = input()     #Never used
line = input()

if line.find('1') != -1:    #Returns -1 if doesn't find any
    print("HARD")
else:
    print("EASY")
