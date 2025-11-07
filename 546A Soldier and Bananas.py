#Input: a line with three numbers separated by spaces: cost of the first banana, soldier dollars and number of banana he wants. Each banana costs number of banana * cost of initial banana
#Output: number of dollars borrowed

line = input()
lineList = line.split(" ")      #Turns the line into a list, indexes each element and converts them to int
costBanana = int(lineList[0])
dollarsSoldier = int(lineList[1])
numberBananas = int(lineList[2])

totalPrice = 0
for i in range(1, numberBananas + 1):       #+1 because range doesn't do the last number
    totalPrice += costBanana * i        #The problem indications

if (totalPrice - dollarsSoldier) > 0:       #Needs to borrow money
    print(totalPrice - dollarsSoldier)
else:       #Doesn't need to borrow money
    print(0)