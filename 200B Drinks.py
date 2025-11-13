#Input: a number and a line with a sequence of numbers separated by an empty space.
#Output: the average of the numbers in the sequence (the sum divided by the numbers of elements)
#Maybe I should change it with list comprehensions

n = int(input())
line = input()

lineList = line.split(" ")      #Turns the line into a list with the numbers separated by " "
sum = 0

for i in lineList:
    sum += int(i)       #Casts to int because they're input and stored as strings

result = sum / n
print(result)