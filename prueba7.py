def ClaseAnimal(especie, color):
    '''
    Esta función devuelve un objeto instanciado de la clase Animal, 
    la cual debe tener los siguientes atributos:
        Edad    (Un valor de tipo de dato entero, que debe inicializarse en cero)
        Especie (Un valor de tipo de dato string)
        Color   (Un valor de tipo de dato string)
    y debe tener el siguiente método:
        CumplirAnios  (este método debe sumar uno al atributo Edad y debe devolver ese valor)
    Recibe dos argumento:
        especie: Dato que se asignará al atributo Especie del objeto de la clase Animal
        color: Dato que se asignará al atributo Color del objeto de la clase Animal
    Ej:
        a = ClaseAnimal('perro','blanco')
        a.CumpliAnios() -> debe devolver 1
        a.CumpliAnios() -> debe devolver 2
        a.CumpliAnios() -> debe devolver 3
    '''
    #Tu código aca:   
    class ClaseAnimal:
        edad = 0
        especie = ''
        color = ''
    
        def __init__(self,especie,color):
            self.edad = 0
            self.especie = especie
            self.color = color
    
        def CumplirAnios(self):
            self.edad += 1
            return self.edad
    a = ClaseAnimal(especie,color)
    return a

a = ClaseAnimal('perro','negro')
print(a.CumplirAnios())
print(a.CumplirAnios())
print(a.CumplirAnios())


a = ClaseAnimal('ballena','azul')
for i in range(0,10):
    print(a.CumplirAnios())






