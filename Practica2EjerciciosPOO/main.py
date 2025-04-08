class Arma:
    def __init__(self, nombre, dano, tipo):
        self.nombre = nombre
        self.dano = dano
        self.tipo = tipo

    def mostrar_info(self):
        return f"Arma: {self.nombre}, Daño: {self.dano}, Tipo: {self.tipo}"

arma1 = Arma("Espada de hielo", 35, "Arma pesada")

print(arma1.mostrar_info())
