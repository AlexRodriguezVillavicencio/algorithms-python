def displayLed(num):
    cadena = str(num)

    arreglo = []
    for palabra in cadena:
        arreglo.append(palabra)

    for led in arreglo:
        if led == "0":
            print("###")
            print("# #")
            print("# #")
            print("# #")
            print("###")
        if led == "1":
            print("  #")
            print("  #")
            print("  #")
            print("  #")
            print("  #")
        if led == "2":
            print("###")
            print("  #")
            print("###")
            print("#  ")
            print("###")
        if led == "3":
            print("###")
            print("  #")
            print("###")
            print("  #")
            print("###")
        if led == "4":
            print("# #")
            print("# #")
            print("###")
            print("  #")
            print("  #")
        if led == "5":
            print("###")
            print("#  ")
            print("###")
            print("  #")
            print("###")
        if led == "6":
            print("###")
            print("#  ")
            print("###")
            print("# #")
            print("###")
        if led == "7":
            print("###")
            print("  #")
            print("  #")
            print("  #")
            print("  #")
        if led == "8":
            print("###")
            print("# #")
            print("###")
            print("# #")
            print("###")
        if led == "9":
            print("###")
            print("# #")
            print("###")
            print("  #")
            print("  #")


while True:
    try:
        displayLed(int(input('ingresa el numero: ')))
        break
    except ValueError:
        print("hey! hazme caso, ingresa solo numeros: \n")
