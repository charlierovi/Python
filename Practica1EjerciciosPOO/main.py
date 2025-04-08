class Personaje:
    def __init__(self, nombre, nivel):
        self.nombre = nombre
        self.nivel = nivel

    def saludar(self):
        print(f"Hola! Soy {self.nombre} y estoy en el nivel {self.nivel}!")

personaje1 = Personaje("Brandon", 5)
personaje2 = Personaje("Drogo", 10)

personaje1.saludar()
personaje2.saludar()
