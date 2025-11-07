#Input: an integer.
#Output: the minimum number of steps necessary to get there from 0 with available moves 1, 2, 3, 4, 5.

n = int(input())

#The minimum moves is as many 5 moves plus one for the remainder if any.
if n % 5 == 0: 
    print(int(n/5))     #Number of 5 moves
else:
    print(int(n/5) + 1)     #Number of 5 moves plus one for the remainder.