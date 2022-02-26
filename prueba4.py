def Factorial(numero):
    '''
    Esta función devuelve el factorial del número pasado como parámetro.
    En caso de que no sea de tipo entero y/o sea menor que 1, debe retornar nulo.
    Recibe un argumento:
        numero: Será el número con el que se calcule el factorial
    Ej:
        Factorial(4) debe retornar 24
        Factorial(-2) debe retornar nulo
    '''
    #Tu código aca:
    if isinstance(numero,int) and numero >= 1:
        multiplicar = 1
        for i in range(1,numero+1):
            multiplicar *=i
        resultado = multiplicar
    else:
        resultado = None

    return resultado

   

        
print(Factorial(-2)) 
