import random

ANCHO = 20
ALTO = 10
PORCENTAJE_PAREDES = 0.25

def crear_mapa_vacio(ancho, alto):
    mapa = []
    for y in range(alto):
        fila = []
        for x in range(ancho):
            if x == 0 or y == 0 or x == ancho - 1 or y == alto - 1:
                fila.append("#")
            else:
                fila.append(".")
        mapa.append(fila)
    return mapa

def agregar_paredes_aleatorias(mapa, porcentaje):
    ancho = len(mapa[0])
    alto = len(mapa)
    cantidad = int((ancho * alto) * porcentaje)

    for _ in range(cantidad):
        x = random.randint(1, ancho - 2)
        y = random.randint(1, alto - 2)
        mapa[y][x] = "#"

def colocar_jugador(mapa):
    ancho = len(mapa[0])
    alto = len(mapa)

    while True:
        x = random.randint(1, ancho - 2)
        y = random.randint(1, alto - 2)
        if mapa[y][x] == ".":
            mapa[y][x] = "P"
            break

def mostrar_mapa(mapa):
    for fila in mapa:
        print("".join(fila))

if __name__ == "__main__":
    mapa = crear_mapa_vacio(ANCHO, ALTO)
    agregar_paredes_aleatorias(mapa, PORCENTAJE_PAREDES)
    colocar_jugador(mapa)
    mostrar_mapa(mapa)
