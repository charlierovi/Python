import random

class Pregunta:
    def __init__(self, pregunta, opciones, respuesta_correcta):
        self.pregunta = pregunta
        self.opciones = opciones
        self.respuesta_correcta = respuesta_correcta

    def es_correcta(self, respuesta):
        return self.respuesta_correcta == respuesta

class Juego:
    def __init__(self):
        self.preguntas = []
        self.puntuacion = 0

    def agregar_pregunta(self, pregunta):
        self.preguntas.append(pregunta)

    def jugar(self):
        random.shuffle(self.preguntas)

        for pregunta in self.preguntas:
            print("\n" + pregunta.pregunta)

            for i, opcion in enumerate(pregunta.opciones, 1):
                print(f"{i}. {opcion}")

            try:
                respuesta = int(input("Elige una opcion (1-4): ")) - 1
                if 0 <= respuesta < len(pregunta.opciones) and pregunta.es_correcta(pregunta.opciones[respuesta]):
                    print("Correcto! Muy bien!")
                    self.puntuacion += 1
                else:
                    print(f"Incorrecto, la respuesta correcta es: {pregunta.respuesta_correcta}")

            except ValueError:
                print("Entrada no valida.")

        print(f"\nJuego terminado! Puntuacion final: {self.puntuacion}/{len(self.preguntas)}")

juego = Juego()
juego.agregar_pregunta(Pregunta("Cual es el personaje principal de la saga Harry Potter?", ["Frodo", "Ron", "Harry Potter", "Aslan"], "Harry Potter"))
juego.agregar_pregunta(Pregunta("En que año se lanzo Fortnite?", ["1998", "2025", "2017", "2010"], "2017"))
juego.agregar_pregunta(Pregunta("Como se llama el villano de Star Wars?", ["Obi", "Yoda", "Merlin", "DarthVader"], "DarthVader"))
juego.agregar_pregunta(Pregunta("Quien es el protagonista de la saga El señor de los anillos?", ["Aragorn", "Sam", "Draco", "Frodo"], "Frodo"))

juego.jugar()