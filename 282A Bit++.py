x = 0

n = int(input())

for i in range(0, n):
    line = input()
    if line.find('+') != -1:
        x += 1
    else:
        x -=1

print(x)