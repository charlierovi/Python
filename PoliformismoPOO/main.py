class Animal:
    def hacer_sonido(self):
        print("Este animal hace un sonido!")

class Perro(Animal):
    def hacer_sonido(self):
        print("El perro hace: Guau!")

class Gato(Animal):
    def hacer_sonido(self):
        print("El gato hace: Miau!")

def emitir_sonido(animal):
    if isinstance(animal, Animal):
        animal.hacer_sonido()
    else:
        print("Este no es un animal válido para representar el sonido!.")

if __name__ == "__main__":
    perro = Perro()
    gato = Gato()

    emitir_sonido(perro)
    emitir_sonido(gato)
