#Input: a line with the number of entries. 10 or 01 indicating the two positions of magnets +- or -+
#Output: the number of groups that form by the magnetic forces

n = int(input())

listMagnets = []
groupCounter = 1        #At least there's one group with one magnet

for i in range(0, n):
    magnet = int(input())       #Recieves the input and adds it to a list
    listMagnets.append(magnet)      

for i in range(0, n-1):     #For every element except the last one compares with the next one
    if listMagnets[i] != listMagnets[i+1]:      #If they're the same, they atract; if not, they form a new group. +-+- | +-  -+
        groupCounter += 1

print(groupCounter)