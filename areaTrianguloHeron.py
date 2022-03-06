def esUnTriangulo(a, b, c):
    return a + b > c and b + c > a and c + a > b      #desigualdad triangular

def heron(a, b, c):
    p = (a + b + c) / 2
    return (p * (p - a) * (p - b) * (p - c)) ** 0.5     #formula de Herón

def campoTriangulo(a, b, c):
    if not esUnTriangulo(a, b, c):
        return None
    return heron(a, b, c)

print(campoTriangulo(2,3,4))