def NumeroCapicua(numero):
    '''
    En matemáticas, la palabra capicúa (del catalán cap i cua, 'cabeza y cola')​ 
    se refiere a cualquier número que se lee igual de izquierda a derecha que 
    de derecha a izquierda. Se denominan también números palíndromos.
    Esta función devuelve el valor booleano True si el número es capicúa, de lo contrario
    devuelve el valor booleano False 
    En caso de que el parámetro no sea de tipo entero, debe retornar nulo.
    Recibe un argumento:
        numero: Será el número sobre el que se evaluará si es capicúa o no lo es.
    Ej:
        NumeroCapicua(787) debe retornar True
        NumeroCapicua(108) debe retornar False
    '''
    #Tu código aca:
    lista= []
    if type(numero)=='int':
        hola = list(str(numero))
        for i in reversed(hola):
            lista.append(i)
        invertido = "".join(lista)

        if(numero == invertido):
            resultado = True
        else:
            resultado = False 

        return resultado    
    else:
        return 'falta'
   

        
print(NumeroCapicua(123))    


# def invertir_numero(n):
#     numero = 0
#     while n != 0:
#         numero = 10*numero+n % 10
#         print(numero)
#         # print(n)
#         n //= 10
#         # print(n)
#     return numero

# print(invertir_numero(123))