def factorizar_numero(numero):
    '''
     Esta función recibe como parámetro un número entero mayor a cero y devuelva dos listas, 
     una con cada factor común y otra con su exponente, 
     esas dos listas tienen que estar contenidas en otra lista.
     En caso de que el parámetro no sea de tipo entero y/ó mayor a cero debe retornar nulo.
     Recibe un argumento:
         numero: Será el número sobre el que se hará la factorización.
     Ej:
         factorizar_numero(12) debe retornar [[2,3],[2,1]]
         factorizar_numero(13) debe retornar [[13],[1]]
         factorizar_numero(14) debe retornar [[2,7],[1,1]]
    '''
    #Tu código aca:
    if not (isinstance(numero,int) and numero > 0):
          resultado = None
    else:
        exponente = [] 
        comun = []

        i = 1
        for i in range(1, numero+1):      
          if i==1: 
              i=2                         
          counter = 0
          while numero % i == 0:
            numero /= i
            counter += 1

          if counter:
            comun.append(i)
            exponente.append(counter)

        resultado = []
        resultado.append(comun)
        resultado.append(exponente)
        return resultado
    

print(factorizar_numero(12))
print(factorizar_numero(13))
print(factorizar_numero(14))
print(factorizar_numero(5))
print(factorizar_numero(1428))
print(factorizar_numero('hola'))
print(factorizar_numero(0))
print(factorizar_numero(-8))