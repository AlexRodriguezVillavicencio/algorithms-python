def misplit(strng):
    if strng == '' or strng.isspace():
        return [ ]

    lst = []
    word = ''
    inword = not strng[0].isspace()
    print(inword)

    for x in strng:
        if inword:
            if not x.isspace():
                word = word + x
                print(word)
            else:
                lst.append(word)
                inword = False
        else:
            if not x.isspace():
                inword = True
                word = x
            else:
                pass
    if inword:
        lst.append(word)

    return lst

print(misplit("Ser o no ser, esa es la pregunta"))