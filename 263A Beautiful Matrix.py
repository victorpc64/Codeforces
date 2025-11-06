#Input: five lines of five elemnents. All 0 except for one 1.
#Output: a single number with the minimum moves from that 1 to 3,3

i = -1 #Initialize indexes
j = -1
for iter in range(1, 6):    #Input for the 5 lines
    line = input()
    if line.find('1') != -1:    #If line contains 1
        i = iter    #Row index
        j = line.replace(' ', '').find('1') + 1     #Removes spaces and fetches the index of the one plus an extra 1 because find counts from 0
        
resultado = abs(3-i) + abs(3-j)     #The distance to 3,3 is the sum of the differences in absolute value
print(resultado)