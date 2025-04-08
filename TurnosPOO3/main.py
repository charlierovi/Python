import random

class Personaje:
    def __init__(self, nombre, vida, ataque, defensa):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque
        self.defensa = defensa

    def esta_vivo(self):
        return self.vida > 0

    def recibir_dano(self, dano):
        dano_real = max(dano - self.defensa, 0)
        self.vida -= dano_real
        print(f"{self.nombre} ha recibido {dano_real} de daño! Vida restante: {self.vida}")

    def atacar(self, otro):
        dano=random.randint(self.ataque-5, self.ataque+5)
        print(f"{self.nombre} ataca a {otro.nombre} con {dano} de daño base!")
        otro.recibir_dano(self.ataque)

class Jugador(Personaje):
    def elegir_accion(self):
        print("\nElige una acción:")
        print("1. Atacar")
        eleccion = input("Opción: ")
        return eleccion

class Enemigo(Personaje):
    def decidir_accion(self):
        return "1"

def combate(jugador, enemigo):
    turno = 0
    print("Comienza el combate!")

    while jugador.esta_vivo() and enemigo.esta_vivo():
        print("\nTurno", turno + 1, "!")

        if turno % 2 == 0:
            accion = jugador.elegir_accion()
            if accion == "1":
                jugador.atacar(enemigo)
        else:
            print(f"\nTurno de {enemigo.nombre}")
            accion = enemigo.decidir_accion()
            if accion == "1":
                enemigo.atacar(jugador)

        turno += 1

    if jugador.esta_vivo():
        print("\nHas ganado!")
    else:
        print("\nGAME OVER!")

jugador = Jugador(nombre="Aquiles", vida=100, ataque=20, defensa=5)
enemigo = Enemigo(nombre="Hector", vida=80, ataque=15, defensa=3)

combate(jugador, enemigo)
