w = input()
w = int(w)

if (w < 1 ) or (w > 100):
    print("NO")

elif w == 1:
    print("NO")

elif w == 2:
    print("NO")

else:
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