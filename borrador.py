# text = "pyxpyxpyx"
# new=[]
# for letter in text:
#     if letter == "x":
#         new.append(letter)
#         continue
# print(len(new))


# list=[]
# for digit in "0165031806510":
#     if digit == "0":
#         x = "x"
#         list.append(x)
#         continue
#     list.append(digit)

# str = "".join(list)
# print(str)

# lst = [1, 2, 3, 4, 5]
# lst2 = []
# agregar = 0

# for number in lst:
#     agregar += number
#     lst2.append (agregar)
    
# print(lst2)









miLista = [8, 10, 6, 2, 4] # lista para ordenar
swapped = True # lo necesitamos verdadero (True) para ingresar al bucle while

while swapped:
    swapped = False # no hay swaps hasta ahora
    for i in range(len(miLista) - 1):
        if miLista[i] > miLista[i + 1]:
            swapped= True # ocurrió el intercambio!
            miLista[i], miLista[i + 1] = miLista[i + 1], miLista[i]

print(miLista)






# El ordenamiento burbuja - versión interactiva
# miLista = []
# num = int (input("¿Cuántos elementos deseas ordenar?:"))

# for i in range(num):
#     val = float(input("Introduce un elemento de la lista:"))
#     miLista.append(val)


# swapped = True
# while swapped:
#     swapped = False
#     for i in range(len(miLista) - 1):
#         if miLista[i] > miLista[i + 1]:
#             swapped = True
#             miLista[i], miLista[i + 1] = miLista[i + 1], miLista[i]

# print("\nOrdenado:")
# print(miLista)



# python ordenando mi lista

# miLista = []
# num = int(input("de cuantos elementos serán?: "))
# for i in range(num):
#     val = int(input('ingresa el elemto: '))
#     miLista.append(val)

# miLista.sort() 
# print(miLista)


