line1 = input()
nInput = int(line1.partition(" ")[0])   #Divides input by space and takes the first element and converts it to int
kIndex = int(line1.partition(" ")[2])
result = 0

line2 = input()
line2 = line2.split(" ")    #Creates a list with each element of line2 between spaces

for i in range(0, kIndex):      #Since it starts in 0, kIndex includes the number
    if line2[i] != '0':
        result += 1
    else:
        break


for i in range(kIndex, len(line2)):     #Starts in kIndex because it's the next element.
    if line2[kIndex-1] == '0':      #Since lists start with 0 I have to put -1 to access the real kIndex
        break
    else:
        if line2[kIndex-1] == line2[i]:     
            result += 1
        else:
            break
    
print(result)