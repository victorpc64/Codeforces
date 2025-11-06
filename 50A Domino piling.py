#Input: a single line with two integers m and n (1<=M<=N<=16)
#Output: one number. Maximal number of dominoes.

line = input()
m = int(line.partition(" ")[0]) #Takes the first number out of the line
n = int(line.partition(" ")[2])

mn = m * n  #Total of squares

if mn % 2 == 0:     #If even, divide by 2.
    print(int(mn / 2))  #int so it doesnt give .0
else:       #If odd, substract 1 and divide by 2. Could also have done it by integer division
    print(int((mn-1) / 2))