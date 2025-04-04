llista = []

while True:
    print("\n1. Afegir element")
    print("2. Mostrar llista")
    print("3. Esborrar element")
    print("4. Sortir")
    opcio = int(input("Escull una opció: "))

    if opcio == 1:
        element = input("Introdueix un element: ")
        llista.append(element)
    elif opcio == 2:
        print("Llista actual:", llista)
    elif opcio == 3:
        index = int(input("Introdueix l'índex a esborrar: "))
        if 0 <= index < len(llista):
            llista.pop(index)
        else:
            print("Índex no vàlid!")
    elif opcio == 4:
        break
    else:
        print("Opció no vàlida!")
