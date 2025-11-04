#Two versions. This one looks for the input in a list from 4 to 100 only even numbers.

w = input()
w = int(w)

if w in range (4, 101, 2):
    print("YES")
else:
    print("NO")