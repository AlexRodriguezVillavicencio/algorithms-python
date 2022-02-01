# Érase una vez una tierra - una tierra de leche y miel, habitada por gente feliz y próspera.
# La gente pagaba impuestos, por supuesto, su felicidad tenía límites. 
# El impuesto más importante, denominado Impuesto Personal de Ingresos (IPI, para abreviar) 
# tenía que pagarse una vez al año y se evaluó utilizando la siguiente regla:

#     Si el ingreso del ciudadano no era superior a 85,528 pesos, el impuesto era igual 
#    al 18% del ingreso menos 556 pesos y 2 centavos (esta fue la llamada exención fiscal ).
#     Si el ingreso era superior a esta cantidad, el impuesto era igual a 14,839 pesos y 
#       2 centavos, más el 32% del excedente sobre 85,528 pesos.

# Tu tarea es escribir una calculadora de impuestos.

#     Debe aceptar un valor de punto flotante: el ingreso.

# Nota: Este país feliz nunca devuelve dinero a sus ciudadanos. Si el impuesto calculado 
# es menor que cero, solo significa que no hay impuesto (el impuesto es igual a cero). 


ingreso=float(input("Ingrese el ingreso anual:"))

#
# Coloca tu código aquí.
limite = 85528

if ingreso <= limite:
    impuesto = .18*ingreso - 556.2
    if impuesto>0:
        impuesto = impuesto
    else:
        impuesto = 0.0
elif ingreso > limite:
    impuesto = 14839.2 + .32*(ingreso-limite)

#
impuesto=round(impuesto, 0)
print("El impuesto es: ", impuesto, "pesos")