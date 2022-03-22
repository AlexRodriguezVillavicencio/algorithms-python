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






'''-----------Naturaleza multidimensional de las listas: aplicaciones avanzadas ---------------------------------'''

# Profundicemos en la naturaleza multidimensional de las listas. Para encontrar cualquier elemento de una lista 
# bidimensional, debes usar dos coordenadas:

# Una vertical (número de fila).
# Una horizontal (número de columna).
# Imagina que desarrollas una pieza de software para una estación meteorológica automática. 
# El dispositivo registra la temperatura del aire cada hora y lo hace durante todo el mes. 
# Esto te da un total de 24 × 31 = 744 valores. Intentemos diseñar una lista capaz de almacenar 
# todos estos resultados. Primero, debes decidir qué tipo de datos sería adecuado para esta aplicación. 
# En este caso, sería mejor un float, ya que este termómetro puede medir la temperatura con una precisión 
# de 0.1 ℃.
# Luego tomarás la decisión arbitraria de que las filas registrarán las lecturas cada hora exactamente 
# (por lo que la fila tendrá 24 elementos) y cada una de las filas se asignará a un día del mes 
# (supongamos que cada mes tiene 31 días, por lo que necesita 31 filas). Aquí está el par apropiado de 
# comprensiones(h es para las horas, dpara el día):

# temps = [[0.0 for h in range (24)] for d in range (31)]

# Toda la matriz está llena de ceros ahora. Puede suponer que se actualiza automáticamente utilizando 
# agentes de hardware especiales. Lo que tienes que hacer es esperar a que la matriz se llene con las mediciones.
# Ahora es el momento de determinar la temperatura promedio mensual del mediodía. Suma las 31 lecturas registradas 
# al mediodía y divida la suma por 31. Puedes suponer que la temperatura de medianoche se almacena primero. 
# Aquí está el código:

# temps = [[0.0 for h in range(24)] for d in range (31)]
                # # la matriz se actualiza mágicamente aquí
                
# suma = 0.0

# for day in temps:
#     suma += day[11]

# promedio= suma / 31
# print("Temperatura promedio al mediodía:", promedio)

# Nota: La variable day utilizada por el bucle for no es un escalar: cada paso a través de la matriz 
# temps lo asigna a la siguiente fila de la matriz; Por lo tanto, es una lista. Se debe indexar con 11 para acceder al valor de temperatura medida al mediodía.

# Ahora encuentra la temperatura más alta durante todo el mes, ve el código:

# temps = [[0.0 for h in range (24)] for d in range (31)]
                # # la matriz se actualiza mágicamente aquí


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
                # # la matriz se actualiza mágicamente aquí

# hotDays = 0
# for day in temps:
#     if day[11] > 20.0:
#         hotDays += 1

# print(hotDays, " fueron los días calurosos.")



'''------------------------- Arreglos tridimensionales ----------------------------------'''

# Python no limita la profundidad de la inclusión lista en lista. Aquí puedes ver un ejemplo de un arreglo 
# tridimensional:
# Imagina un hotel. Es un hotel enorme que consta de tres edificios, de 15 pisos cada uno. Hay 20 habitaciones 
# en cada piso. Para esto, necesitas un arreglo que pueda recopilar y procesar información sobre las habitaciones 
# ocupadas/libres.
# Primer paso: El tipo de elementos del arreglo. En este caso, sería un valor booleano (True/False).
# Paso dos: Análisis de la situación. Resume la información disponible: tres edificios, 15 pisos, 20 habitaciones.

# Ahora puedes crear el arreglo:
# habitaciones = [[[False for r in range(20)] for f in range(15)] for t in range(3)] 

# El primer índice (0 a 2) selecciona uno de los edificios; el segundo(0 a 14) selecciona el piso, el tercero
# (0 a 19) selecciona el número de habitación. Todas las habitaciones están inicialmente desocupadas.
# Ahora ya puedes reservar una habitación para dos recién casados: en el segundo edificio, en el décimo piso, 
# habitación 14:

# habitaciones[1][9][13] = True 
# y desocupa el segundo cuarto en el quinto piso ubicado en el primer edificio:

# habitaciones[0][4][1] = False 
# Verifica si hay disponibilidad en el piso 15 del tercer edificio:

# vacante = 0
# for numeroHabitacion in range(20):
#     if not habitaciones[2][14][numeroHabitacion]:
#         vacante += 1

# La variable vacante contiene 0 si todas las habitaciones están ocupadas, o en dado caso el número de 
# habitaciones disponibles.




'''-------------------------tuplas, listas y diccionarios ----------------------------------'''


# #metodo zip() para relacionar dos listas o tuplas
# l1 = [2,4,1]
# l2 = [6,7,8]
# l3 = zip(l1,l2)
# print(l3)
# l4 = tuple(l3)
# print(l4)


# #metodo sort() para ordenar una lista
# l1 = [2,4,1]
# l1.sort()
# print(l1)
# l1.sort(reverse = True)
# print(l1)


# #metodo keys() para recorrer un diccionario
# dict = {"gato" : "chat", "perro" : "chien", "caballo" : "cheval"}
# for key in dict.keys():
#     print(key, "->", dict[key])


# #metodo sorted() para odenar
# dict = {"gato" : "chat", "perro" : "chien", "caballo" : "cheval"}
# for key in sorted(dict.keys()):
#     print(key, "->", dict[key])


# #metodo item() para recorrer diccionarios (otra manera)
# dict = {"gato" : "chat", "perro" : "chien", "caballo" : "cheval"}
# for spanish, french in dict.items():
#     print(spanish, "->", french)

# #metodo values() para regresar solo los valores de un diccionario
# Como el diccionario no es capaz de automáticamente encontrar la clave de un 
# valor dado, el rol de este método es algo limitado.
# dict = {"gato" : "chat", "perro" : "chien", "caballo" : "cheval"}
# for french in dict.values():
#     print(french)



# #dos maneras de insertar valores a un diccionario:
# dict = {"gato" : "chat", "perro" : "chien", "caballo" : "cheval"}
# dict['cisne'] = 'cygne'
# print(dict)
# dict.update({"pato" : "canard"})
# print(dict)


# #eliminando una clave de un diccionario
# dict = {"gato" : "chat", "perro" : "chien", "caballo" : "cheval"}
# del dict['perro']
# print(dict)
# dict.popitem()
# print(dict)


# #desempaquetando una tupla
# tup = 1, 2, 3
# a, b, c = tup
# print(a * b * c)


# #metodo count() para contar el numero de veces que se repite un elemento de una tupla 
# tup = 1, 2, 3, 2, 4, 5, 6, 2, 7, 2, 8, 9
# duplicates = tup.count(2)
# print(duplicates) 


# #unir varios diccionarios para crear uno nuevo:
# d1 = {'Adam Smith':'A', 'Judy Paxton':'B+'}
# d2 = {'Mary Louis':'A', 'Patrick White':'C'}
# d4 = {'Mry Louis':'Ad', 'Packite':'Cs'}
# d3 = {}
# for elemento in (d1, d2, d4):
#     d3.update(elemento)
# print(d3)


# # tupla a diccionario: dict() , a tupla: tuple(), a lista: list()
# colores = [["verde", "#008000"], ("azul", "#0000FF")]
# colDict = dict(colores)
# print(colDict)

'''-------------------------explicación del juego de michi ----------------------------------'''
# from random import randrange

# def DisplayBoard(board):
# 	print("+-------" * 3,"+",sep="")
# 	for row in range(3):
# 		print("|       " * 3,"|",sep="")
# 		for col in range(3):
# 			print("|   " + str(board[row][col]) + "   ",end="")
# 		print("|")
# 		print("|       " * 3,"|",sep="")
# 		print("+-------" * 3,"+",sep="")

# def EnterMove(board):
# 	ok = False	# suposición falsa - lo necesitamos para entrar en el bucle
# 	while not ok:
# 		move = input("Ingresa tu movimiento: ") 
# 		ok = len(move) == 1 and move >= '1' and move <= '9' # ¿es valido lo que ingreso el usuario?
# 		if not ok:
# 			print("Movimiento erróneo, ingrésalo nuevamente") # no, no lo es. Ingrésalo nuevamente.
# 			continue
# 		move = int(move) - 1 	# numero de la celda, del 0 al 8
# 		row = move // 3 	# fila de la celda
# 		col = move % 3		# columna de la celda
# 		sign = board[row][col]	# marca el cuadro elegido
# 		ok = sign not in ['O','X'] 
# 		if not ok:	# esta ocupado, ingresa una posición nuevamente
# 			print("¡Campo ocupado, ingresa nuevamente!")
# 			continue
# 	board[row][col] = 'O' 	# colocar '0' al cuadro seleccionado

# def MakeListOfFreeFields(board):
# 	free = []	# la lista esta vacía inicialmente
# 	for row in range(3): # itera a través de las filas
# 		for col in range(3): # itera a través de las columnas
# 			if board[row][col] not in ['O','X']: # ¿Está la celda libre?
# 				free.append((row,col)) # si, agrega una nueva tupla a la lista
# 	return free


# def VictoryFor(board,sgn):
# 	if sgn == "X":	# ¿Estamos buscando X?
# 		who = 'yo'	# Si, es la maquina
# 	elif sgn == "O": # ... o estamos buscando O?
# 		who = 'tu'	# Si, es el usuario
# 	else:
# 		who = None	# ¡No debemos de caer aquí!
# 	cross1 = cross2 = True  # para las diagonales
# 	for rc in range(3):
# 		if board[rc][0] == sgn and board[rc][1] == sgn and board[rc][2] == sgn:	# revisar filas rc
# 			return who
# 		if board[0][rc] == sgn and board[1][rc] == sgn and board[2][rc] == sgn: # revisar columnas rc
# 			return who
# 		if board[rc][rc] != sgn: # revisar la primer diagonal
# 			cross1 = False
# 		if board[2 - rc][2 - rc] != sgn: # revisar la segunda diagonal
# 			cross2 = False
# 	if cross1 or cross2:
# 		return who
# 	return None

# def DrawMove(board):
# 	free = MakeListOfFreeFields(board) # hace una lista de los cuadros vacios o libres
# 	cnt = len(free)
# 	if cnt > 0:	# si la lista no esta vacía, elegir un lugar para 'X' y colocarla 
# 		this = randrange(cnt)
# 		row, col = free[this]
# 		board[row][col] = 'X'

# board = [ [3 * j + i + 1 for i in range(3)] for j in range(3) ] # crear un tablero vacío
# board[1][1] = 'X' # colocar la primer 'X' en el centro
# free = MakeListOfFreeFields(board)
# humanturn = True # ¿De quien es turno ahora?
# while len(free):
# 	DisplayBoard(board)
# 	if humanturn:
# 		EnterMove(board)
# 		victor = VictoryFor(board,'O')
# 	else:	
# 		DrawMove(board)
# 		victor = VictoryFor(board,'X')
# 	if victor != None:
# 		break
# 	humanturn = not humanturn		
# 	free = MakeListOfFreeFields(board)

# DisplayBoard(board)
# if victor == 'tu':
# 	print("¡Has ganado!")
# elif victor == 'yo':
# 	print("¡He ganado!")
# else:
# 	print("¡Empate!")



# lst = [[x for x in range(3)] for y in range(3)]
# print(lst)

'''-------------------------conociendo nuestro sistema ----------------------------------'''
# #modelo code/ python/ os/ hardware
# from platform import platform, machine, processor,system ,version ,python_implementation, python_version_tuple
# print(platform())
# print(machine())
# print(processor())
# print(system())
# print(version())
# print(python_implementation())
# print(python_version_tuple())




#jugando con el ctrl c
# from time import sleep
# seconds = 0
# while True:
#     try:
#         print(seconds)
#         seconds += 1
#         sleep(1)
#     except KeyboardInterrupt:
#         print("¡No hagas eso!")




# # como abusar del diccionario
# # y cómo lidiar con ello

# dict = { 'a' : 'b', 'b' : 'c', 'c' : 'd' }
# ch = 'a'
# try:
#     while True:
#         ch = dict[ch]
#         print(ch)
# except KeyError:
#     print('No existe tal clave:', ch)




# # Demostrando la función ord ()

# ch1 = 'a' 
# ch2 = ' ' # espacio

# print(ord(ch1))
# print(ord(ch2))


'''-------------------------operaciones con cadenas ----------------------------------'''
# https://docs.python.org/3.4/library/stdtypes.html#string-methods
# # Demostrando la función ord ()
# ch1 = 'a' 
# ch2 = ' ' # espacio
# print(ord(ch1))
# print(ord(ch2))
# print(ord('9'))
# print(ord('0'))
# print(ord('9') - ord('0'))


# # Demostrando la función chr()
# print(chr(97))
# print(chr(945))



# # Rodajas o rebanadas
# alpha = "abdefg"

# print(alpha[1:3])
# print(alpha[3:])
# print(alpha[:3])
# print(alpha[3:-2])
# print(alpha[-3:4])
# print(alpha[::2])
# print(alpha[1::2])


# # Demonstrando max() y min()
# t = 'Los Caballeros Que Dicen "¡Ni!"'
# print('[' + max(t) + ']')
# print('[' + min(t) + ']')


# # Demonstrando el método index()
# print("aAbByYzZaA".index("b"))
# print("aAbByYzZaA".index("Z"))


# # Demostrando la función list()
# print(list("abcabc"))

# # Demostrando el método count()
# print("abcabc".count("b"))

# # Demostración del método capitalize()
# print('aBcD'.capitalize())

# # Demostración del método center()
# print('[' + 'alfa'.center(10) + ']')
# print('[' + 'gamma'.center(20, '*') + ']')

# # Demostración del método endswith()
# if "epsilon@gmail.com".endswith("@gmail.com"):
#     print("si")
# else:
#     print("no")


# # Demostración del método find()

# txt = """the ordinary lorem ipsum
# text has been used in typesetting since the 1960s 
# or earlier, when it was popularized by advertisements 
# for Letraset transfer sheets. It was introduced to 
# the Information Age in the mid-1980s by the Aldus Corporation, 
# which employed it in graphics and word-processing templates
# for its desktop publishing program PageMaker (from Wikipedia)"""

# fnd = txt.find('the')
# while fnd != -1:
#     print(fnd)
#     fnd = txt.find('the', fnd + 1)



# # Demostración del método the isalnum()
# print('lambda30'.isalnum())
# print('lambda'.isalnum())
# print('30'.isalnum())
# print('@'.isalnum())
# print('lambda_30'.isalnum())
# print(''.isalnum())

# # Ejemplo 1: Demostración del método isapha()
# print("Moooo".isalpha())
# print('Mu40'.isalpha())

# # Ejemplo 2: Demostración del método isdigit()
    
# print('2018'.isdigit())
# print("Año2019".isdigit())

# # Ejemplo 1: Demostración del método islower()
# print("Moooo".islower())
# print('moooo'.islower())

# # Ejemplo 2: Demostración del método isspace()
# print(' \n '.isspace())
# print(" ".isspace())
# print("mooo mooo mooo".isspace())

# # Ejemplo 3: Demostración del método isupper() 
# print("Moooo".isupper())
# print('moooo'.isupper())
# print('MOOOO'.isupper())

# # Demostración del método join()
# print(",".join(["omicron", "pi", "rho"]))

# # Demostración del método lower()
# print("SiGmA=60".lower())


# # Demostración del método the lstrip()
# print(" www.cisco.com".lstrip("w."))
# print("www.cisco.com".lstrip("w."))
# print("cisco.com".lstrip(".com"))


# # Demostración del método replace()
# print("www.netacad.com".replace("netacad.com", "pythoninstitute.org"))
# print("This is it!".replace("is", "are"))
# print("Apple juice".replace("juice", ""))


# # Demostración del método split()
# print("phi       chi\npsi".split())

# # Demostración del método swapcase()
# print("Yo sé que no sé nada.".swapcase())

# print()

# # Demostración del método title()
# print("Yo sé que no sé nada. Parte 1.".title())

# # Demostración del método upper()
# print("Yo sé que no sé nada. Parte 2.".upper())


digitos=['1111110',  	# 0
	   '0110000',	# 1
	   '1101101',	# 2
	   '1111001',	# 3
	   '0110011',	# 4
	   '1011011',	# 5
	   '1011111',	# 6
	   '1110000',	# 7
	   '1111111',	# 8
	   '1111011',	# 9
	   ]

def printNumero(num):
    digs = str(num)
    lineas = [ ''  for l in range(5) ]
    print(lineas)
    for d in digs:
        segs = [ [' ',' ',' '] for l in range(5) ]
        print(segs)
        ptrn = digitos[ord(d) - ord('0')]
        print(ptrn[0])
        print(ptrn[1])
        print(ptrn[2])
        print(ptrn[3])
        print(ptrn[4])
        print(ptrn[5])
        print(ptrn[6])
        
        if ptrn[0] == '1':
            segs[0][0] = segs[0][1] = segs[0][2] = '#'
        if ptrn[1] == '1':
            segs[0][2] = segs[1][2] = segs[2][2] = '#'
        if ptrn[2] == '1':
            segs[2][2] = segs[3][2] = segs[4][2] = '#'
        if ptrn[3] == '1':
            segs[4][0] = segs[4][1] = segs[4][2] = '#'
        if ptrn[4] == '1':
            segs[2][0] = segs[3][0] = segs[4][0] = '#'
        if ptrn[5] == '1':
            segs[0][0] = segs[1][0] = segs[2][0] = '#'
        if ptrn[6] == '1':
            segs[2][0] = segs[2][1] = segs[2][2] = '#'
            for l in range(5):
                lineas[l] += ''.join(segs[l]) + ' '
        for l in lineas:
            print(l)

printNumero(int(input("Ingresa el número que deseas mostrar: ")))

