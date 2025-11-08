#Input: an integer with the number of input lines (the rooms). Each line has two integers: the people in the room and its capacity.
#Output: how many rooms can acommodate two extra people.

n = int(input())
availableRoomsCounter = 0

for i in range(0, n):
    line = input()
    people = int(line.partition(" ")[0])        #Takes out the first number
    capacity = int(line.partition(" ")[2])
    if (capacity - people) >= 2:        #If there's extra capacity for two, +1 to counter
        availableRoomsCounter += 1
    
print(availableRoomsCounter)