#Input: two numbers separated by a space.
#Output: the number of years where the first number (was smaller or equal) will be bigger than the second one. The rate is triple the first and double the second one a year.

line = input()

a = int(line.partition(" ")[0])     #Gets the first number out of input
b = int(line.partition(" ")[2])

for i in range(1,100):      #100 arbitrarly. Maybe I should change the implementation.
    aEvolution = a * pow(3, i)      #Triple a year is expressed as 3 to the power of number of years
    bEvolution = b * pow(2, i)

    if aEvolution > bEvolution:
        print(i)
        break