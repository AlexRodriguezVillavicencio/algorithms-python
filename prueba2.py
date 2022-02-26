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
    return print(parte_entera, resto)

DividirDosNumeros(10,4)