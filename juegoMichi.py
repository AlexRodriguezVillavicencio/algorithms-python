from time import sleep
from random import randint

def tablero():
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
    return

def juegoJugador():
    if jugador == 1:
        resultado = board[0][0]= 'O'
    elif jugador == 2:
        resultado = board[0][1]= 'O'
    elif jugador == 3:
        resultado = board[0][2]= 'O'
    elif jugador == 4:
        resultado = board[1][0]= 'O'
    elif jugador == 5:
        resultado = board[1][1]= 'O'
    elif jugador == 6:
        resultado = board[1][2]= 'O'
    elif jugador == 7:
        resultado = board[2][0]= 'O'
    elif jugador == 8:
        resultado = board[2][1]= 'O'
    elif jugador == 9:
        resultado = board[2][2]= 'O'
    return resultado

def juegoMaquina():
    if maquina == 1:
        resultado = board[0][0]= 'X'
    elif maquina == 2:
        resultado = board[0][1]= 'X'
    elif maquina == 3:
        resultado = board[0][2]= 'X'
    elif maquina == 4:
        resultado = board[1][0]= 'X'
    elif maquina == 5:
        resultado = board[1][1]= 'X'
    elif maquina == 6:
        resultado = board[1][2]= 'X'
    elif maquina == 7:
        resultado = board[2][0]= 'X'
    elif maquina == 8:
        resultado = board[2][1]= 'X'
    elif maquina == 9:
        resultado = board[2][2]= 'X'
        return resultado


def movimientoJugador():
    global jugador
    ciclo = True
    while ciclo:
        try:
            jugador = int(input("Selecciona un número: "))
            if jugador >= 1 and jugador <= 9 :
                if jugador not in newmaquina and jugador not in newjugador:
                    newjugador.append(jugador)
                    ciclo = False
                else:
                    print("hey, no hagas trampa")
            else:
                print("selecciona un numero del 1 al 9")
        except ValueError:
            print("solo debes seleccionar números")   
    return jugador

def movimientoMaquina():
    global maquina
    ciclo2 = True
    while ciclo2:
        maquina = randint(1,9)
        if maquina not in newjugador and maquina not in newmaquina:   
                newmaquina.append(maquina)
                ciclo2 = False
    print("yo selecciono: ", maquina)            
    return maquina


newjugador = []
newmaquina = [5]
board = [[1,2,3],[4,5,6],[7,8,9]]
print("Bienvenido al juego del TicTacToe o Michi")
print(board)
sleep(1)

maquina = board[1][1] = 'X'
tablero()
sleep(1)
ciclo3 = True
while ciclo3:

    movimientoJugador()
    juegoJugador()
    tablero()
    sleep(1)


    movimientoMaquina()
    juegoMaquina()
    tablero()
    sleep(1)

print("gracias")



