
def NumeroCapicua(numero):
    global total
    # Tu código aca:
    lista= []
    if isinstance(numero,int):
        arreglo = list(str(numero))
        for i in reversed(arreglo):
            lista.append(i)
        invertido = "".join(lista)

        if(int(invertido) == int(numero)):
            resultado = True
        else:
            resultado = False 
    else:
        resultado = None

    return resultado

print(NumeroCapicua(232)) 
print(NumeroCapicua(132)) 
print(NumeroCapicua('hola')) 