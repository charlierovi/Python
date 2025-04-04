# Definim la classe pare
class Animal:
    def __init__(self, nom):
        self.nom = nom

    def parla(self):
        print(f"{self.nom} està fent un so.")


# Definim una classe filla que hereta de la classe Animal
class Gos(Animal):
    def parla(self):
        print(f"{self.nom} està lladrant.")

class Gat(Animal):

    def parla(self):
        print(f"{self.nom} està fent miau.")


# Creem un objecte de la classe filla
gos1 = Gos("Rex")
gos1.parla()    # Rex està lladrant
gat1 = Gat("Gatet")
gat1.parla()
