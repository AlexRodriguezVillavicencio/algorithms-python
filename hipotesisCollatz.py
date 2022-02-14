c0 = int(input("Escriba un numero entero positivo: "))
pasos = 0

if c0>0:
    while c0 != 1:
        if c0%2 == 0:
            c0//=2
        elif c0%2 != 0:
            c0= 3*c0 + 1
        print(c0)
        pasos+=1
    print("pasos =", pasos)
else:
    print("Escriba un número positivo por favor")

