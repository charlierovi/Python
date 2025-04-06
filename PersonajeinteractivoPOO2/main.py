import os

mapa = [
    ['.', '.', '.', '.', '.'],
    ['.', '#', '.', '#', '.'],
    ['.', '.', '.', '.', '.'],
    ['#', '.', '#', '.', '#'],
    ['.', '.', '.', '.', '.']
]

pos_x = 0
pos_y = 0
mapa[pos_y][pos_x] = 'P'

def mostrar_mapa():
    os.system('cls' if os.name == 'nt' else 'clear')
    for fila in mapa:
        print(' '.join(fila))
    print("\nUsa W/A/S/D para mover, Q para salir")

def mover_personaje(direccion):
    global pos_x, pos_y

    nueva_x, nueva_y = pos_x, pos_y
    if direccion == 'w':
        nueva_y -= 1
    elif direccion == 's':
        nueva_y += 1
    elif direccion == 'a':
        nueva_x -= 1
    elif direccion == 'd':
        nueva_x += 1

    if 0 <= nueva_x < len(mapa[0]) and 0 <= nueva_y < len(mapa):
        if mapa[nueva_y][nueva_x] != '#':
            mapa[pos_y][pos_x] = '.'
            pos_x, pos_y = nueva_x, nueva_y
            mapa[pos_y][pos_x] = 'P'

while True:
    mostrar_mapa()
    movimiento = input("Movimiento: ").lower()
    if movimiento == 'q':
        print("GAME OVER!")
        break
    elif movimiento in ['w', 'a', 's', 'd']:
        mover_personaje(movimiento)
