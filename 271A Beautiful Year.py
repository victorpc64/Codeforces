#Input: a year (1000<=y<=9000)
#Output: the first year after the given one that has all its digits distinct.

year = input()
result = 0

for tryYear in range(int(year)+1, 90000):       #Range next year and an arbitrarly big number
    isNumber = True     #Flag to know it's an answer
    tryYear = str(tryYear)      #Turns the number to a list, then a list for manipulating digits
    tryYear = list(tryYear)
    for i in range(0, len(tryYear)-1):      #Tests all digits except the last one
        for j in range(i+1, len(tryYear)):  #Against every next digit
            if tryYear[i] == tryYear[j]:
                isNumber = False    #If the digit is not unique and breaks and breks the nested loop with the flag
                break
        if isNumber == False:   #Breaks the second for
            break
    else:
        result = tryYear     #Executes if all digits are distinct. Saves the result.
        result = "".join(result)      #Turns back to string from list
        break

print(result)