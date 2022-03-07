def factorial(n):
    if n == 1:    # la condición de terminación
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(4)) 