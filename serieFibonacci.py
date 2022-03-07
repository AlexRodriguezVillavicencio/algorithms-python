def fibonacci(conteo):
    lista = []
    inicial = 1
    siguiente = 1
    n=2
    lista.append(inicial)
    lista.append(siguiente)
    while n < conteo:
        sum = inicial + siguiente
        inicial, siguiente = siguiente, sum
        lista.append(sum)
        n+=1
    return lista

print(fibonacci(10))



#extendida
# def fibonacci(inicial,siguiente,conteo):
#     lista = []
#     n=2
#     lista.append(inicial)
#     lista.append(siguiente)
#     while n < conteo:
#         sum = inicial + siguiente
#         inicial, siguiente = siguiente, sum
#         lista.append(sum)
#         n+=1
#     return lista

# print(fibonacci(1,3,5))