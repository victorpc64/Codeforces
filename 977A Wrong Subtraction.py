#Input: a number and the repetitions of substractions to be performed on it. If it's mod 10 = 0, divide by 10; else -1.
#Output: the result.

line = input()
lineDivided = line.split(" ")
number = int(lineDivided[0])
repetitions = int(lineDivided[1])

for i in range(0, repetitions):
    if number <= 0:
        break
    elif number % 10 == 0:
        number = int(number / 10)
    else:
        number -= 1

print(number)