# def ListaEnteros(inicio, tamanio):
#     '''
#     Esta función devuelve una lista de números enteros
#     Recibe dos argumentos:
#         inicio: Numero entero donde inicia la lista
#         tamanio: Cantidad de números enteros consecutivos
#     Ej:
#         ListaEnteros(10,5) debe retornar [10,11,12,13,14]
#     '''
#     lista = []
#     #Tu código aca:
#     for i in range(tamanio):
#         i+=inicio
#         lista.append(i)
#         print(i)
#     return lista

# ListaEnteros(10,5)


def ListaEnteros(inicio, tamanio):
    lista = []
    for i in range(inicio,tamanio+inicio):
        i+=0
        lista.append(i)
    return lista

print(ListaEnteros(10,5))
print(ListaEnteros(1,8))
print(ListaEnteros(0,5))

