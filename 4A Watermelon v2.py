#4A Watermelon

#Hay que escribir los programas con el input vacío. No me lo aceptaba porque el juez online se confundía con la cadena que puse de prompt.
w = input()
w = int(w)

#No necesitaba comprobar lo límites superiores e inferiores del input del problema.
#if (w < 1 ) or (w > 100):
#    print("NO")


#No necesitaba esta comprobación.
#if w == 1:
#    print("NO")

#Tampoco necesitaba esta comprobación
# if w == 2:
#     print("NO")

# else:

if w % 2 == 0:
    limite = w-1
else:
    limite = w

if w == 2:
    print("NO")

else:
    for i in range(2, limite, 2):
        if ((w - i) % 2) == 0:
            print ("YES")
            break
    else:
        print ("NO")