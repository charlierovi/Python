class Lavadora:
    def __init__(self, carga, estado):
        self.carga=carga
        self.estado=estado

    def apagar(self):
        self.estado="apagada"
        print("La lavadora está apagada.")

    def encender(self):
        if self.estado=="encendida":
            print("La lavadora ya está encendida.")
        else:
            self.estado="encendida"
            print("La lavadora ahora está encendida")

    def sacar_ropa(self):
        if self.estado=="apagada":
            self.carga=0
            print("La lavadora está vacía.")
        if self.estado=="encendida":
            print("No puedes retirar la ropa porque está encendida")

    def meter_ropa(self, kg):
        if self.estado=="apagada":
            if self.carga+kg<=8:
                self.carga+=kg
                print(f"La lavadora tiene {self.carga} kg de ropa.")
        else:
            print("No cabe la ropa")



lavadora1=Lavadora(0,"apagada")
lavadora1.meter_ropa(1)

