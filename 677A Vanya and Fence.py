#Input: one line with the number of friends and the fence height, and a second line with the heights of each friend.
#Output: a number with the numbers of friends +1 for each one higher than the fence.

line1 = input()     
friendsHeights = input()

nFriends = int(line1.partition(" ")[0])     #Takes out the first number
heightFence = int(line1.partition(" ")[2])
friendsHeights = friendsHeights.split(" ")      #Turns the string into a list separated by " "
result = len(friendsHeights)        #The initial number is the number of friends

for i in friendsHeights:        #Checks each friend height against the fence. +1 to result if bigger.
    if int(i) > heightFence:    #Turns to int for comparison
        result += 1

print(result)