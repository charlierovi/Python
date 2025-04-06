import random

def generar_mapa(filas, columnas):
    mapa = []

    for i in range(filas):
        fila = []
        for j in range(columnas):
            celda = random.choice(['.', '#'])
            fila.append(celda)
        mapa.append(fila)

    fila_personaje = random.randint(0, filas - 1)
    columna_personaje = random.randint(0, columnas - 1)
    mapa[fila_personaje][columna_personaje] = 'P'

    return mapa

def mostrar_mapa(mapa):
    for fila in mapa:
        print(' '.join(fila))

filas = 10
columnas = 15

mapa = generar_mapa(filas, columnas)
mostrar_mapa(mapa)
