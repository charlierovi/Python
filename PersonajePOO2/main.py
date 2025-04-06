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

    def atacar(self, otro_personaje):
        if self.esta_vivo():
            print(f"{self.nombre} ha atacado a {otro_personaje.nombre}")
            otro_personaje.recibir_dano(self.ataque)
        else:
            print(f"{self.nombre} no puede atacar porque está fuera de combate!")

def batalla(personaje1, personaje2):
    print(f"\nComienza la pelea entre {personaje1.nombre} y {personaje2.nombre}!\n")
    turno = 0
    while personaje1.esta_vivo() and personaje2.esta_vivo():
        if turno % 2 == 0:
            personaje1.atacar(personaje2)
        else:
            personaje2.atacar(personaje1)
        turno += 1
        print("-" * 40)

    ganador = personaje1 if personaje1.esta_vivo() else personaje2
    print(f"\nLa batalla ha terminado! {ganador.nombre} ha ganado!\n")

p1 = Personaje("Guerrero", vida=100, ataque=20, defensa=5)
p2 = Personaje("Mago", vida=80, ataque=25, defensa=3)

batalla(p1, p2)
