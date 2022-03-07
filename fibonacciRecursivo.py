def fibonacci(n):
    if n < 1:
        return None
    if n < 3:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

lista = []
def conteo(num):
    for n in range(1, num + 1):
        lista.append(fibonacci(n))
    return lista

conteo(10)
print(lista)


