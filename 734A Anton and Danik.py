#Input: an int with the number of games played and a string with the A or D letter indicating who won each game
#Output: Anton if there's more As than Ds, Danik if Ds and Friendship if equal

n = input()     #Given by the problem but never used
outcomesPlayed = input()
antonCounter = 0
danikCounter = 0

for i in outcomesPlayed:
    if i == 'A':
        antonCounter +=1
    else:
        danikCounter +=1

if antonCounter > danikCounter:
    print("Anton")
elif antonCounter < danikCounter:
    print("Danik")
else:
    print("Friendship")