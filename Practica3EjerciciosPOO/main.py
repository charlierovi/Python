class Arma:
    def __init__(self, nombre, dano, tipo):
        self.nombre = nombre
        self.dano = dano
        self.tipo = tipo

    def mostrar_info(self):
        return f"Arma: {self.nombre}, Daño: {self.dano}, Tipo: {self.tipo}"

    def usar(self):
        print(f"Estas usando el arma {self.nombre} para atacar!")

    def guardar(self):
        print(f"Se guarda el arma {self.nombre}!")

arma1 = Arma("Espada de hielo", 40, "Arma pesada")

arma1.usar()
arma1.guardar()
