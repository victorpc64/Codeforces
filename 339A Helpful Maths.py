#Input: String of 1, 2 or 3 separated by a +.   Eg: 1+3+2 or 1 or 3 or 2+3+1
#Output: String with the sequence sorted.       Eg: 1+2+3 or 1 or 3 or 1+2+3

line = input()
line = line.split('+')      #Splits the string into a list with no +
line.sort()     #Sorts the list in place.

result='+'      #Initialize the result with + because join uses the original string as the separator
result = result.join(line)  #Puts together the sorted list
print(result)