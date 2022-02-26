def NumeroBinario(numero):
    '''
    Esta función recibe como parámetro un número entero mayor ó igual a cero y lo devuelve en su 
    representación binaria. Debe recibir y devolver un valor de tipo entero.
    En caso de que el parámetro no sea de tipo entero y mayor a -1 debe retornar nulo.
    Recibe un argumento:
        numero: Será el número que se convertirá a binario.
    Ej:
        NumeroBinario(12) debe retornar 1100
        NumeroBinario(2) debe retornar 10
        NumeroBinario(14) debe retornar 1110
    '''
    #Tu código aca:
    if not(isinstance(numero,int)) or numero <= -1:
        resultado = None
    else:
        arreglo = [] 
        binario = []

        while numero != 0: 
            residuo = numero % 2
            cociente = numero // 2
            arreglo.append(residuo) 
            numero = cociente 

        new_arreglo = arreglo[:]
        for i in reversed(new_arreglo):
            binario.append(i)
        resultado = int("".join([str(i) for i in binario]))

    
    return resultado

print(NumeroBinario(5))
print(NumeroBinario(255))
print(NumeroBinario(-10))
print(NumeroBinario('hey'))



