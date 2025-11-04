n = int(input())
counterResult = 0

for i in range(0, n):
    line = input()
    line = line.replace(' ', '')
    if line == '101' or line == '110' or line == '111' or line == '011':
            counterResult += 1

print(counterResult)
    

#Casos válidos       000, 001, 010, 100
#Casos no válidos    101, 110, 111. 011