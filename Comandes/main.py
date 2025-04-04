#Comandes en una Botiga
#Es crea el diccionari amb els clients, el material que compren, la quantitat i el preu de cada element.
comandes_clients = {
    "Anna" : [("LLibre", 2, 10.0), ("Bolígraf", 5, 1.50)],
    "Joan": [("Carpeta", 3, 4.50)],
    "Marta": [("Ordinador", 1, 800.00), ("Ratolí", 2, 20.00)]
}
#Es crea la funció per calcular el cost total de la comanda.
def calcular_cost_total(client, comandes_clients):
    comandes = comandes_clients[client]
    cost_total = 0

    for comanda in comandes:
        nom_producte, quantitat, preu_unitari = comanda
        cost_total += quantitat * preu_unitari
    return cost_total
#Es crea la funció per buscar el client que ha fet una comanda superior als 100€.
def comanda_100(comandes_clients):
    clients = []

    for client, comandes in comandes_clients.items():
        cost_total = calcular_cost_total(client, comandes_clients)
        if cost_total > 100:
            clients.append(client)
    return clients
#Es crea la funció per imprimir la comanda de cada client i totes les dades necessàries.
def imprimir_comandes(client, comandes_clients):
    comandes = comandes_clients[client]
    print(f"Comandes de {client}:")

    for comanda in comandes:
        nom_producte, quantitat, preu_unitat = comanda
        cost_comanda = quantitat * preu_unitat
        print(f"{nom_producte}: {quantitat} unitats a {preu_unitat} €. Total: {cost_comanda} €.\n")

#EXEMPLES DE FUNCIONAMENT
cost_anna = calcular_cost_total("Anna", comandes_clients)
print(f"El cost total de les comandes de l'Anna és: {cost_anna} €.\n")

cost_joan = calcular_cost_total("Joan", comandes_clients)
print(f"El cost total de les comandes del Joan és: {cost_joan} €.\n")

cost_marta = calcular_cost_total("Marta", comandes_clients)
print(f"El cost total de les comandes de la Marta és: {cost_marta} €.\n")

clients_100 = comanda_100(comandes_clients)
print(f"Els clients amb comandes superiors a 100 € són: {clients_100}\n")

imprimir_comandes("Anna", comandes_clients)

#Es crea un menú amb el bucle While per poder fer ús de les funcions.
while True:
    print("Menú:")
    print("1. Mostra el cost total de cada client.")
    print("2. Mostra els clients amb comandes superiors a 100 €.")
    print("3. Mostra les comandes d'un client.")
    print("4. EXIT")

    opció = input("Selecciona una opció del menú: ")

    if opció == '1':
        for client in comandes_clients:
            cost_total = calcular_cost_total(client, comandes_clients)
            print(f"El cost total de les comandes de {client} és: {cost_total} €.")

    elif opció == '2':
        clients_100 = comanda_100(comandes_clients)
        if clients_100:
            print("Els clients amb comandes superiors a 100 € son:")
            for client in clients_100:
                print(client)

    elif opció == '3':
        client = input("Introdueix el nom d'un client: ")
        if client in comandes_clients:
            imprimir_comandes(client, comandes_clients)

    elif opció == '4':
        print("EXIT")
        break

    else:
        print("Opció no vàlida. Selecciona una opció del menú.")