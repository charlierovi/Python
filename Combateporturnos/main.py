import random

class Personaje:
    def __init__(self, nombre, vida, ataque):
        self.nombre=nombre
        self.vida=vida
        self.ataque=ataque

    def esta_vivo(self):
        return self.vida>0

    def recibir_dano(self, cantidad):
        self.vida-=cantidad
        print(f"{self.nombre} ha recibido {cantidad} de dano. Le queda de vida: {self.vida}!")

    def atacar(self, objetivo):
        print(f"{self.nombre} ataca a {objetivo.nombre} con {self.ataque} de dano!")
        objetivo.recibir_dano(self.ataque)

class Guerrero(Personaje):
    def habilidad_especial(self, objetivo):
        dano=self.ataque*2
        print(f"{self.nombre} usa 'Golpe furioso' y causa {dano} de dano!")
        objetivo.recibir_dano(dano)

class Mago(Personaje):
    def __init__(self, nombre, vida, ataque, mana):
        super().__init__(nombre, vida, ataque)
        self.mana=mana

    def habilidad_especial(self, objetivo):
        if self.mana>=20:
            dano=self.ataque+15
            print(f"{self.nombre} lanza 'Rayo de la muerte' y causa {dano} de dano!")
            objetivo.recibir_dano(dano)
            self.mana-=20
        else:
            print(f"{self.nombre} no tiene mana! Mana actual: {self.mana}!")

class Arquero(Personaje):
    def habilidad_especial(self, objetivo):
        dano=self.ataque+random.randint(5, 15)
        print(f"{self.nombre} dispara 'Flecha del infierno' y causa {dano} de dano!")
        objetivo.recibir_dano(dano)

def turno(jugador, enemigo):
    print("\n--- Turno del Jugador ---")
    print("1. Ataque normal")
    print("2. Habilidad especial")
    eleccion = input("Elige una acción a realizar: ")

    if eleccion=="1":
        jugador.atacar(enemigo)
    elif eleccion=="2":
        jugador.habilidad_especial(enemigo)
    else:
        print("Opcion incorrecta! Lo siento, pierdes el turno!")

    if enemigo.esta_vivo():
        print("\n--- Turno del Enemigo ---")
        enemigo.atacar(jugador)

def juego():
    print("Elige tu clase de personaje:")
    print("1. Guerrero")
    print("2. Mago")
    print("3. Arquero")
    eleccion = input("Opción: ")

    if eleccion == "1":
        jugador = Guerrero("Guerrero", 100, 15)
    elif eleccion == "2":
        jugador = Mago("Mago", 80, 10, 50)
    elif eleccion == "3":
        jugador = Arquero("Arquero", 90, 12)
    else:
        print("Opción incorrecta! Se usará Guerrero por defecto.")
        jugador = Guerrero("Guerrero", 100, 15)

    enemigo = Guerrero("Orco", 100, 12)

    while jugador.esta_vivo() and enemigo.esta_vivo():
        turno(jugador, enemigo)

    if jugador.esta_vivo():
        print("\nHas ganado!")
    else:
        print("\nHas sido derrotado!")

juego()
