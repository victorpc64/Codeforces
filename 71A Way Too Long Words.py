n = int(input())
#n = int(n)

palabras = []
for i in range (0, n):
    palabras.append(input())

for i in palabras:
    if len(i) <= 10:
        print(i)
    else:
        temp = i[1:-1]      #Characters between the first and last one
        resultado = i[0] + str(len(temp)) + i[-1]       #First character + number of characters in between + last character
        print(resultado)