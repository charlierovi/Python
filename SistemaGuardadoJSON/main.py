import json

class Personaje:
    def __init__(self, nombre, nivel = 1, experiencia = 0, inventario = None):
        self.nombre = nombre
        self.nivel = nivel
        self.experiencia = experiencia
        self.inventario = inventario if inventario is not None else []

    def subir_nivel(self):
        self.nivel += 1
        self.experiencia = 0
        print(f"{self.nombre} ha subido al nivel {self.nivel}!")

    def agregar_items(self, item):
        self.inventario.append(item)
        print(f"{item} ha sido añadido al inventario de {self.nombre}!")

    def guardar_partida(self, archivo):
        datos = {
            "nombre": self.nombre,
            "nivel": self.nivel,
            "experiencia": self.experiencia,
            "inventario": self.inventario
        }

        with open(archivo, "w") as f:
            json.dump(datos, f, indent=4)
        print(f"Partida guardada en {archivo}!")

    @classmethod
    def cargar_partida(cls, archivo):
        try:
            with open(archivo, "r") as f:
                datos = json.load(f)
            personaje = cls(
                datos["nombre"],
                datos["nivel"],
                datos["experiencia"],
                datos["inventario"]
            )
            print(f"Partida cargada: {personaje.nombre}, Nivel: {personaje.nivel}")
            return personaje
        except FileNotFoundError:
            print("No se ha encontrado ningun archivo de guardado.")
            return None

jugador = Personaje("Villano")
jugador.agregar_items("Espada de la luz")
jugador.subir_nivel()
jugador.guardar_partida("partida.json")

personaje_cargado = Personaje.cargar_partida("partida.json")