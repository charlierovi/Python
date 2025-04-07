class Inventario:
    def __init__(self):
        self.objetos = {}

    def agregar_objeto(self, nombre, cantidad=1):
        if nombre in self.objetos:
            self.objetos[nombre] += cantidad
        else:
            self.objetos[nombre] = cantidad
        print(f"Se ha agregado {cantidad} '{nombre}' al inventario!")

    def eliminar_objeto(self, nombre, cantidad=1):
        if nombre in self.objetos:
            if self.objetos[nombre] > cantidad:
                self.objetos[nombre] -= cantidad
                print(f"Se ha eliminado {cantidad} '{nombre}' del inventario!")
            elif self.objetos[nombre] == cantidad:
                del self.objetos[nombre]
                print(f"Se ha eliminado completamente '{nombre}' del inventario!")
            else:
                print(f"No tienes suficientes '{nombre}' para eliminar!")
        else:
            print(f"El objeto '{nombre}' no se encuentra en el inventario!")

    def mostrar_inventario(self):
        if not self.objetos:
            print("El inventario está vacío!")
        else:
            print("Inventario actual:")
            for nombre, cantidad in self.objetos.items():
                print(f" - {nombre}: {cantidad}")


if __name__ == "__main__":
    inventario = Inventario()

    inventario.agregar_objeto("Poción revitalizadora", 3)
    inventario.agregar_objeto("Espada de diamante", 1)
    inventario.agregar_objeto("Poción revitalizadora", 2)

    inventario.mostrar_inventario()

    inventario.eliminar_objeto("Poción revitalizadora", 4)
    inventario.eliminar_objeto("Espada de diamante")

    inventario.mostrar_inventario()
