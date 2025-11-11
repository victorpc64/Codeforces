#Input: a number
#Output: YES if the sum of number digits 4 and 7 in the input is only composed by 4s and 7s 

n = input()
luckyDigitsCounter = 0

for i in n:     #Runs through the input as a string and counts the apparitions of 4s and 7s
    if i == '4' or i == '7':
        luckyDigitsCounter +=1


for i in str(luckyDigitsCounter):       #Supposing the counter can be more than 1 digit long, checks every digit to be 4 or 7
    if i != '4' and i != '7':
        print("NO")
        break
else:       #for runs without break
    print("YES")

#Implementation with one digit counter
# if luckyDigitsCounter == 4 or luckyDigitsCounter == 7:
#     print("YES")
# else:
#     print("NO")
