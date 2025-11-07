#Input: a line with the number of stops. As many lines as the number with two numbers: the people that exit and the people that enters.
#Output: the minimum capacity to accommodate all people.

nStops = int(input())
currentCapacity = 0
listCapacities = []

for i in range(0, nStops):      #for every stop
    line = input()
    exits = int(line.partition(" ")[0])     #takes out of line the number of exits and enters
    enters = int(line.partition(" ")[2])
    currentCapacity = currentCapacity + enters - exits      #caculates the capacity needed for that stop
    listCapacities.append(currentCapacity)      #records the capacity

print(max(listCapacities))      #returns the maximum capacity needed for the stops, which is the minimum for the train line