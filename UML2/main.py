class Motor:
    def __init__(self, tipo, potencia):
        self.tipo = tipo
        self.potencia = potencia

    def encender(self):
        print(f"El motor {self.tipo} de {self.potencia} CV está encendido.")


class Coche:
    def __init__(self, marca, modelo, año, tipo_motor, potencia_motor):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.motor = Motor(tipo_motor, potencia_motor)

    def arrancar(self):
        print(f"{self.marca} {self.modelo}, {self.año} está arrancando.")
        self.motor.encender()

    def detener(self):
        print(f"{self.marca} {self.modelo} se ha detenido.")


coche1 = Coche("Opel", "Astra", 2002, "Gasolina", 110)
coche1.arrancar()
coche1.detener()
