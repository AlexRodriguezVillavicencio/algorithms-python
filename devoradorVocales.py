#  Tu programa debe:

#     Pedir al usuario que ingrese una palabra.
#     Utilizar userWord = userWord.upper() para convertir la palabra ingresada por el usuario a mayúsculas; 
#     Usa la ejecución condicional y la instrucción continue para "comer" las siguientes vocales A , E , I , O , U de la palabra ingresada.
#     Asigne las letras no consumidas a la variable palabrasinVocal e imprime la variable en la pantalla.


#  Datos de prueba

# Entrada de muestra: Gregory

# Salida esperada:
# GRGRY

# Entrada de muestra: abstemious

# Salida esperada:
# BSTMS

userWord = input("ingrese una palabra: ")
userWord = userWord.upper()

for i in userWord:
    if i == "A":
        continue
    elif i == "E":
        continue
    elif i == "I":
        continue
    elif i == "O":
        continue
    elif i == "U":
        continue
    else:
        print(i)

