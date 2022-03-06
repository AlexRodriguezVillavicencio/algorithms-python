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









# miLista = [8, 10, 6, 2, 4] # lista para ordenar
# swapped = True # lo necesitamos verdadero (True) para ingresar al bucle while

# while swapped:
#     swapped = False # no hay swaps hasta ahora
#     for i in range(len(miLista) - 1):
#         if miLista[i] > miLista[i + 1]:
#             swapped= True # ocurrió el intercambio!
#             miLista[i], miLista[i + 1] = miLista[i + 1], miLista[i]

# print(miLista)






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







# Naturaleza multidimensional de las listas: aplicaciones avanzadas
# Profundicemos en la naturaleza multidimensional de las listas. Para encontrar cualquier elemento de una lista bidimensional, debes usar dos coordenadas:

# Una vertical (número de fila).
# Una horizontal (número de columna).
# Imagina que desarrollas una pieza de software para una estación meteorológica automática. El dispositivo registra la temperatura del aire cada hora y lo hace durante todo el mes. Esto te da un total de 24 × 31 = 744 valores. Intentemos diseñar una lista capaz de almacenar todos estos resultados.

# Primero, debes decidir qué tipo de datos sería adecuado para esta aplicación. En este caso, sería mejor un float, ya que este termómetro puede medir la temperatura con una precisión de 0.1 ℃.

# Luego tomarás la decisión arbitraria de que las filas registrarán las lecturas cada hora exactamente (por lo que la fila tendrá 24 elementos) y cada una de las filas se asignará a un día del mes (supongamos que cada mes tiene 31 días, por lo que necesita 31 filas). Aquí está el par apropiado de comprensiones(h es para las horas, dpara el día):

# temps = [[0.0 for h in range (24)] for d in range (31)]

# Toda la matriz está llena de ceros ahora. Puede suponer que se actualiza automáticamente utilizando agentes de hardware especiales. Lo que tienes que hacer es esperar a que la matriz se llene con las mediciones.

# Ahora es el momento de determinar la temperatura promedio mensual del mediodía. Suma las 31 lecturas registradas al mediodía y divida la suma por 31. Puedes suponer que la temperatura de medianoche se almacena primero. Aquí está el código:

# temps = [[0.0 for h in range(24)] for d in range (31)]
# #
# # la matriz se actualiza mágicamente aquí
# #

# suma = 0.0

# for day in temps:
#     suma += day[11]

# promedio= suma / 31

# print("Temperatura promedio al mediodía:", promedio)

# Nota: La variable day utilizada por el bucle for no es un escalar: cada paso a través de la matriz temps lo asigna a la siguiente fila de la matriz; Por lo tanto, es una lista. Se debe indexar con 11 para acceder al valor de temperatura medida al mediodía.

# Ahora encuentra la temperatura más alta durante todo el mes, ve el código:

# temps = [[0.0 for h in range (24)] for d in range (31)]
# #
# # la matriz se actualiza mágicamente aquí
# #

# mas_alta = -100.0

# for day in temps:
#     for temp in day:
#         if temp > mas_alta:
#             mas_alta = temp

# print("La temperatura más alta fue:", mas_alta)

# Nota:

# La variable day itera en todas las filas de la matriz temps.
# La variable temp itera a través de todas las mediciones tomadas en un día.
# Ahora cuenta los días en que la temperatura al mediodía fue de al menos 20 ℃:

# temps = [[0.0 for h in range(24)] for d in range(31)]
# #
# # la matriz se actualiza mágicamente aquí
# #

# hotDays = 0

# for day in temps:
#     if day[11] > 20.0:
#         hotDays += 1

# print(hotDays, " fueron los días calurosos.")





# Arreglos tridimensionales
# Python no limita la profundidad de la inclusión lista en lista. Aquí puedes ver un ejemplo de un arreglo tridimensional:

# Imagina un hotel. Es un hotel enorme que consta de tres edificios, de 15 pisos cada uno. Hay 20 habitaciones en cada piso. Para esto, necesitas un arreglo que pueda recopilar y procesar información sobre las habitaciones ocupadas/libres.

# Primer paso: El tipo de elementos del arreglo. En este caso, sería un valor booleano (True/False).

# Paso dos: Análisis de la situación. Resume la información disponible: tres edificios, 15 pisos, 20 habitaciones.

# Ahora puedes crear el arreglo:

# habitaciones = [[[False for r in range(20)] for f in range(15)] for t in range(3)] 

# El primer índice (0 a 2) selecciona uno de los edificios; el segundo(0 a 14) selecciona el piso, el tercero (0 a 19) selecciona el número de habitación. Todas las habitaciones están inicialmente desocupadas.

# Ahora ya puedes reservar una habitación para dos recién casados: en el segundo edificio, en el décimo piso, habitación 14:

# habitaciones[1][9][13] = True 

# y desocupa el segundo cuarto en el quinto piso ubicado en el primer edificio:

# habitaciones[0][4][1] = False 

# Verifica si hay disponibilidad en el piso 15 del tercer edificio:

# vacante = 0

# for numeroHabitacion in range(20):
#     if not habitaciones[2][14][numeroHabitacion]:
#         vacante += 1

# La variable vacante contiene 0 si todas las habitaciones están ocupadas, o en dado caso el número de habitaciones disponibles.



# lst = [0 for i in range(1,3)]
# print(lst)
 
 