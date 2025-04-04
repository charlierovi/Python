import random

class Personaje:
    def __init__(self, nombre, salud, ataque, defensa):
        self.nombre = nombre
        self.salud = salud
        self.ataque = ataque
        self.defensa = defensa
        self.experiencia = 0
    def recalcular_ataque_defensa(self):
        if self.experiencia > 0:
            self.ataque = (1 + (0.1 * self.experiencia)) * self.ataque
            self.defensa = (1 + (0.1 * self.experiencia)) * self.defensa


    def esta_vivo(self):
        return self.salud > 0

    def recibir_dano(self, dano):
        self.salud -= dano - self.defensa
        if self.salud < 0:
            self.salud = 0

    def atacar(self, otro_personaje):
        dano = random.randint(0, self.ataque)
        print(f"{self.nombre} ataca a {otro_personaje.nombre} y causa {dano} de daño.")
        otro_personaje.recibir_dano(dano)

    def estadisticas(self):
        print(f"{self.nombre} tiene salud: {self.salud}, ataque: {self.ataque}, defensa: {self.defensa}, experiencia: {self.experiencia}. ")


class Juego:
    def __init__(self, personaje1, personaje2):
        self.personaje1 = personaje1
        self.personaje2 = personaje2

    def combate(self):
        while self.personaje1.esta_vivo() and self.personaje2. esta_vivo():
            print("Personaje 1 ataca a Personaje 2")
            self.personaje1.atacar(self.personaje2)
            juego1.versus()
            print("Personaje 2 ataca a Personaje 1")
            self.personaje2.atacar(self.personaje1)
            juego1.versus()

        if self.personaje1.esta_vivo():
            self.personaje1.experiencia += 1
            self.personaje1.recalcular_ataque_defensa()
            print(f"Ha ganado {self.personaje1.nombre}")
            self.personaje1.estadisticas()
        else:
            self.personaje2.experiencia += 1
            self.personaje2.recalcular_ataque_defensa()
            print(f"Ha ganado {self.personaje2.nombre}")
            self.personaje2.estadisticas()

    def versus(self):
        print(f"{self.personaje1.nombre} // {self.personaje2.nombre}")
        print(f"{self.personaje1.salud} // {self.personaje2.salud}")


p1 = Personaje("P1", 100, 100, 2)
p2 = Personaje("P2", 100, 12, 3)

juego1 = Juego(p1, p2)
juego1.combate()
