#Input: a number and a string.
#Output: the number of eliminations of consecutive characters
#Is it dangerous to for each in a list that you are removing elements from?

n = int(input())        #Takes the number and the line
line = input()
result = 0      #Initializes result

line = list(line)       #Transforms to list, each character an element
for i in range(0, n-1):     #-1 because there's no need to check the last element  
    while i < len(line)-1 and line[i] == line[i+1]:     #Checks it's not the last element of the list -needed because length of the list can change through the loop-
                                                        #and that the element it's not the same as the next one
        line.pop(i)     #Eliminates the element in the index
        result += 1

print(result)

#print("".join(line))       For testing