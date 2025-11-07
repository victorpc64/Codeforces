#Input: Two lines. The firs line with the number of elements and the number of loops to perform. The second with a sequence of Gs and Bs
#Output: Same sequence with Gs moving infront consecutive Bs one position per iteration

line1 = input()
characters = input()

t = int(line1.partition(" ")[2])        #Takes out the second element
characters = list(characters)       #Turns the string to list for manipulation

for iteration in range(0, t):     #t is the number of iterations given
    rest = False    #Initialize rest so there's only one position improvement per iteration
    for i in range(0, len(characters) -1):      #Doesn't run the last element
        if characters[i] == 'B':
            if rest == True:    #If the element has already been manipulated, changes rest and continues
                rest = False
                continue
            else:
                if characters[i+1] == 'G':      #If a G comes after a B swaps them
                    characters[i] = 'G'
                    characters[i+1] = 'B'
                    rest = True     #So there's only one change per element

characters = "".join(characters)    #List back to string
print(characters)