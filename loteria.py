# Supongamos que has elegido los siguientes números en la lotería: 3, 7, 11, 42, 34, 49.

# Los números que han salido sorteados son: 5, 11, 9, 42, 3, 49.

# La pregunta es: ¿A cuántos números le has atinado?


sorteados = [5, 11, 9, 42, 3, 49]
seleccionados = [3, 7, 11, 42, 34, 49]
aciertos = 0

for i in seleccionados:
    if i in sorteados:
        aciertos += 1
print(aciertos)