'''Tu tarea es escribir un simple programa que simule jugar a tic-tac-toe 
(nombre en inglés) con el usuario. Para hacerlo más fácil, Hemos decidido 
simplificar el juego. Aquí están nuestras reglas:

La maquina (por ejemplo, el programa) jugará utilizando las 'X's.
El usuario (por ejemplo, tu) jugará utilizando las 'O's.
El primer movimiento es de la maquina: siempre coloca una 'X' en el centro del tablero.
Todos los cuadros están numerados comenzando con el 1 (observa el ejemplo para que tengas 
una referencia).
El usuario ingresa su movimiento introduciendo el numero de cuadro elegido. El numero debe 
de ser valido, por ejemplo un valor entero mayor que 0 y menor que 10, y no puede ser un 
cuadro que ya esté ocupado.
El programa verifica si el juego ha terminado. Existen cuatro posibles veredictos: 
el juego continua, el juego termina en empate, tu ganas, o la maquina gana.
La maquina responde con su movimiento y se verifica el estado del juego.
No se debe implementar algún tipo de inteligencia artificial, la maquina elegirá un 
cuadro de manera aleatoria, eso es suficiente para este juego.
El ejemplo del programa es el siguiente:

+-------+-------+-------+
|       |       |       |
|   1   |   2   |   3   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   4   |   X   |   6   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   7   |   8   |   9   |
|       |       |       |
+-------+-------+-------+
Ingresa tu movimiento: 1
+-------+-------+-------+
|       |       |       |
|   O   |   2   |   3   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   4   |   X   |   6   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   7   |   8   |   9   |
|       |       |       |
+-------+-------+-------+
+-------+-------+-------+
|       |       |       |
|   O   |   X   |   3   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   4   |   X   |   6   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   7   |   8   |   9   |
|       |       |       |
+-------+-------+-------+
Ingresa tu movimiento: 8
+-------+-------+-------+
|       |       |       |
|   O   |   X   |   3   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   4   |   X   |   6   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   7   |   O   |   9   |
|       |       |       |
+-------+-------+-------+
+-------+-------+-------+
|       |       |       |
|   O   |   X   |   3   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   4   |   X   |   X   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   7   |   O   |   9   |
|       |       |       |
+-------+-------+-------+
Ingresa tu movimiento: 4
+-------+-------+-------+
|       |       |       |
|   O   |   X   |   3   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   O   |   X   |   X   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   7   |   O   |   9   |
|       |       |       |
+-------+-------+-------+
+-------+-------+-------+
|       |       |       |
|   O   |   X   |   X   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   O   |   X   |   X   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   7   |   O   |   9   |
|       |       |       |
+-------+-------+-------+
Ingresa tu movimiento: 7
+-------+-------+-------+
|       |       |       |
|   O   |   X   |   X   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   O   |   X   |   X   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   O   |   O   |   9   |
|       |       |       |
+-------+-------+-------+
¡Has Ganado!

Requerimientos
Implementa las siguientes características:

El tablero debe ser almacenado como una lista de tres elementos, mientras que cada elemento es otra 
lista de tres elementos (la lista interna representa las filas) de manera que todos los cuadros puedas 
ser accedidos empleado la siguiente sintaxis:

board[fila][columna]


Cada uno de los elementos internos de la lista puede contener 'O', 'X', o un digito representando el número 
del cuadro (dicho cuadro se considera como libre).
La apariencia de tablero debe de ser igual a la presentada en el ejemplo.
Implementa las funciones definidas para ti en el editor.

Para obtener un valor numérico aleatorio se puede emplear una función integrada de Python denominada randrange(). 
El siguiente ejemplo muestra como utilizarla (El programa imprime 10 números aleatorios del 1 al 8).

Nota: La instrucción from-import provee acceso a la función randrange definida en un módulo externo de 
Python denominado random.

from random import randrange

for i in range(10):
    print(randrange(8))'''


board = [[1,2,3],[4,5,6],[7,8,9]]   # board[fila][columna]



def DisplayBoard(board):
#
# la función acepta un parámetro el cual contiene el estado actual del tablero
# y lo muestra en la consola
#
    for row in range(3):
        for col in range(3):
            print("|   " + str(board[row][col]) + "   ",end="")


def EnterMove(board):
#
# la función acepta el estado actual del tablero y pregunta al usuario acerca de su movimiento, 
# verifica la entrada y actualiza el tablero acorde a la decisión del usuario
#
    movimiento = input("ingrese su movimiento: ")
    if movimiento == 1:
        resultado = board[0][0]= 'O'
    elif movimiento == 2:
        resultado = board[0][1]= 'O'
    elif movimiento == 3:
        resultado = board[0][2]= 'O'
    elif movimiento == 4:
        resultado = board[1][0]= 'O'
    elif movimiento == 5:
        resultado = board[1][1]= 'O'
    elif movimiento == 6:
        resultado = board[1][2]= 'O'
    elif movimiento == 7:
        resultado = board[2][0]= 'O'
    elif movimiento == 8:
        resultado = board[2][1]= 'O'
    elif movimiento == 9:
        resultado = board[2][2]= 'O'
    return resultado

def MakeListOfFreeFields(board):
#
# la función examina el tablero y construye una lista de todos los cuadros vacíos 
# la lista esta compuesta por tuplas, cada tupla es un par de números que indican la fila y columna
#
    lista = [(),(),()]

def VictoryFor(board, sign):
#
# la función analiza el estatus del tablero para verificar si
# el jugador que utiliza las 'O's o las 'X's ha ganado el juego
#
    if board[0][0] == board[0][1] == board [0][2] == "X":
        return

# def DrawMove(board):
#
# la función dibuja el movimiento de la maquina y actualiza el tablero
#

# salir = 'no'
# while(salir == 'no'):
print("+-------+-------+-------+")
print("|       |       |       |")
print("|  ",board[0][0],"  |  ",board[0][1],"  |  ",board[0][2],"  |")
print("|       |       |       |")
print("+-------+-------+-------+")
print("|       |       |       |")
print("|  ",board[1][0],"  |  ",board[1][1],"  |  ",board[1][2],"  |")
print("|       |       |       |")
print("+-------+-------+-------+")
print("|       |       |       |")
print("|  ",board[2][0],"  |  ",board[2][1],"  |  ",board[2][2],"  |")
print("|       |       |       |")
print("+-------+-------+-------+")