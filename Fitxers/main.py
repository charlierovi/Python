def ejercicio1():
    with open("Frases.txt", "r") as fitxer:
        i = 1
        for linia in fitxer:
            print(f"{i} {linia}")
            i += 1

def ejercicio2():
    frase = input("Afegeix una frase al fitxer Frases.txt: ")
    with open("Frases.txt", "a") as fitxer:
        fitxer.write(f"\n{frase}")

def contar_paraules(fitxer, paraula):
    try:
        with open(fitxer, "r", encoding="utf-8") as llibre:
            contingut = llibre.read()
        return contingut.count(paraula)
    except:
        print("Hi ha un error, ho sentim.")
        return -1

ocurrencies = contar_paraules("quijote.txt", "Quijote")
print(f"Ha aparegut {ocurrencies} vegades.")

def canviar_text(fitxer, cadena_replace, nova_cadena):
    try:
        with open(fitxer, "r", encoding="utf-8") as llibre:
            contingut = llibre.read()
            contingut_nou = contingut.replace(cadena_replace, nova_cadena)

        with open(fitxer, "w", encoding="utf-8") as nou_llibre:
            nou_llibre.write(contingut_nou)

    except:
        print("Hi ha hagut un error, ho sentim.")
        return -1

canviar_text("quijote.txt", "Quijote", "Pepe")







