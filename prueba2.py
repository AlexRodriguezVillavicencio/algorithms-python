def DividirDosNumeros(dividendo, divisor):
    '''
    Esta función devuelve dos valores, la parte entera de la división y su resto
    Recibe dos argumentos:
        dividendo: El número que va a ser dividido
        divisor: El número que va a dividir
    Ej:
        DividirDosNumeros(10,3) debe retornar 3, 1
    '''
    parte_entera = None
    resto = None
    #Tu código aca:
    parte_entera = int(dividendo/divisor)
    resto= dividendo%divisor
    return parte_entera, resto

print(DividirDosNumeros(10,3))
print(DividirDosNumeros(5,4))
print(DividirDosNumeros(10,2))
print(DividirDosNumeros(10,5))
print(DividirDosNumeros(17,3))
print(DividirDosNumeros(13,3))