class Animal:
    def hacer_sonido(self):
        print("Este animal hace un sonido")

class Perro(Animal):
    def hacer_sonido(self):
        print("Guau!")

class Gato(Animal):
    def hacer_sonido(self):
        print("Miau!")

def reproducir_sonido(animal: Animal):
    animal.hacer_sonido()

perro = Perro()
gato = Gato()

reproducir_sonido(perro)
reproducir_sonido(gato)
