class Arma:
    def __init__(self, nombre, dano, tipo):
        self.nombre = nombre
        self.dano = dano
        self.tipo = tipo
        self.durabilidad = 100  # Ahora es un atributo de instancia

    def mostrar_info(self):
        return f"Arma: {self.nombre}, Daño: {self.dano}, Tipo: {self.tipo}, Durabilidad: {self.durabilidad}"

    def usar(self):
        if self.durabilidad > 0:
            print(f"Estas usando el arma {self.nombre} para atacar!")
            self.durabilidad -= 10
            print(f"Durabilidad actualizada: {self.durabilidad}")
        else:
            print(f"El arma {self.nombre} está muy desgastada y no se puede usar!")

    def guardar(self):
        print(f"Se está guardando el arma {self.nombre}!")

arma1 = Arma("Espada de hielo", 50, "Arma pesada")
arma2 = Arma("Arco celestial", 40, "Arma a distancia")

arma1.usar()
arma1.usar()
arma2.usar()
print()

print(arma1.mostrar_info())
print(arma2.mostrar_info())
