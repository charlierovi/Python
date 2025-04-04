#Utilitzar diccionaris i llistes per gestionar informació sobre una biblioteca.
#Es crea el diccionari amb les claus i els altres diccionaris.
biblioteca = {
    1: {"titol": "Python per a tothom", "autor": "John Doe", "quantitat": 3},
    2: {"titol": "Dades i Estructures", "autor": "Anna Smith", "quantitat": 5},
    3: {"titol": "Introducció a OOP", "autor": "Joan Costa", "quantitat": 2},
}
#Es crea la funció per poder afegir els llibres nous i es quedin guardats al diccionari biblioteca. S'utilitza la variable int davant del input perquè funcioni correctament amb els enters.
#S'afegeix un missatge per confirmar que el llibre ha sigut afegit correctament al diccionari biblioteca.
def afegir_llibre():
    id_llibre = int(input("Introdueix l'ID del llibre: "))
    títol = input("Introdueix el títol del llibre: ")
    autor = input("Introdueix l'autor del llibre: ")
    quantitat = int(input("Introdueix la quantitat d'exemplars disponibles: "))
    biblioteca[id_llibre] = {"titol": títol, "autor": autor, "quantitat": quantitat}
    print(f"Llibre '{títol}' afegit correctament.")

#Es crea la funció per buscar un llibre utilitzant l'ID i es dona tota la informació d'aquest.
def buscar_llibre():
    id_llibre = int(input("Introdueix l'ID del llibre a buscar: "))
    if id_llibre in biblioteca:
        llibre = biblioteca[id_llibre]
        print(f"ID: {id_llibre}")
        print(f"Títol: {llibre['titol']}")
        print(f"Autor: {llibre['autor']}")
        print(f"Quantitat: {llibre['quantitat']}")

#Es crea la funció per mostrar tots els llibres del diccionari biblioteca tenint en compte els llibres nous afegits.
def mostrar_llibres():
    print("Llibres disponibles a la biblioteca:")
    for id_llibre, llibre in sorted(biblioteca.items()):
        print(f"ID: {id_llibre}, Títol: {llibre['titol']}, Autor: {llibre['autor']}, Quantitat: {llibre['quantitat']}")

#Es crea la funció per al prèstec d'un llibre utilitzant l'ID i després en cas de poder fer el prèstec es dona un missatge confirmant-lo i mostra quants exemplars queden a la biblioteca.
#Es donen missatges d'error en cas de no trobar el llibre demanat o de no tenir exemplars per fer el prèstec.
def prestec_llibre():
    id_llibre = int(input("Introdueix l'ID del llibre per fer el préstec: "))
    if id_llibre in biblioteca:
        if biblioteca[id_llibre]['quantitat'] > 0:
            biblioteca[id_llibre]['quantitat'] -= 1
            print(f"Préstec realitzat correctament. Queden {biblioteca[id_llibre]['quantitat']} exemplars.")
        else:
            print("No hi ha llibres disponibles per aquest préstec.")
    else:
        print("Llibre no trobat.")

#Es crea el bucle while amb el menú per poder fer ús de les funcions i del diccionari.
while True:
    print("Menú de la biblioteca:")
    print("1. Afegeix un nou llibre")
    print("2. Busca un llibre")
    print("3. Mostra tots els llibres")
    print("4. Préstec d'un llibre")
    print("5. EXIT")

    opció = input("Tria una opció del menú: ")

    if opció == "1":
            afegir_llibre()
    elif opció == "2":
            buscar_llibre()
    elif opció == "3":
            mostrar_llibres()
    elif opció == "4":
            prestec_llibre()
    elif opció == "5":
        print("Fins aviat!")
        break
    else:
        print("Opció no vàlida. Introdueix una opció del menú.")

