#This version tests if w is even and bigger than 2.
#In both version starts from 4 because if it's 0 there's nothing to divide, 1 and 3 are odd and 2 there's no way to split it

w = input()
w = int(w)

if (w > 2) and (w % 2 == 0):
    print("YES")
else:
    print("NO")