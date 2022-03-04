def ProximoPrimo(actual_primo):
    '''
    Esta función devuelve el número primo siguiente al enviado como parámetro.
    En caso de que el parámetro no sea de tipo entero y/o no sea un número primo, debe retornar nulo.
    Recibe un argumento:
        actual_primo: Será el número primo a partir del cual debo buscar el siguiente
    Ej:
        ProximoPrimo(7) debe retornar 11
        ProximoPrimo(8) debe retornar nulo
    '''
    #Tu código aca:
    if(isinstance(actual_primo,int)):
        def cont(actual_primo):
            n=2
            contador=0
            while (n <= actual_primo):
                if actual_primo%n == 0:
                    contador += 1
                n+=1
            return contador           
        if cont(actual_primo) > 1:
            resultado = None
        else:
            proximo = True
            while proximo:         
                actual_primo +=1
                if cont(actual_primo) > 1:
                    proximo = True
                else:
                    proximo = False
                    resultado = actual_primo
        return resultado
    else:
        return None

print(ProximoPrimo(7))
print(ProximoPrimo(8))
print(ProximoPrimo(5))
print(ProximoPrimo(61))
print(ProximoPrimo(139))
print(ProximoPrimo(200))
print(ProximoPrimo('string'))
