class Cotxe:

    def __init__(self, tipus_motor, combustible, portes):
        self.tipus_motor = tipus_motor
        self.combustible = combustible
        self.portes = portes

    def get_tipus_motor(self):
        print(f"El tipus de motor és: {self.tipus_motor}")

    def get_combustible(self):
        print(f"El tipus de combustible és: {self.combustible}")

    def get_portes(self):
        print(f"Té {self.portes} portes.")

    def set_portes(self, numero_portes):
        self.portes = numero_portes


class Mercedes(Cotxe):
    def __init__(self, tipus_acabat):
        self.tipus_acabat = tipus_acabat

    def get_tipus_acabat(self):
        print(f"El tipus d'acabat del Mercedes és: {self.tipus_acabat}.")

class Audi(Cotxe):
    def __init__(self, cv, longitut, amplada, tipus_motor, combustible, portes):
        self.cv = cv
        self.longitut = longitut
        self.amplada = amplada
        self.tipus_motor = tipus_motor
        self.combustible = combustible
        self.portes = portes

    def get_cv(self):
        print(f"El cotxe Audi té: {self.cv} cv.")

    def get_longitut(self):
        print(f"La longitut del cotxe Audi és: {self.longitut} m.")

    def get_amplada(self):
        print(f"L'amplada del cotxe Audi és: {self.amplada} m.")

cotxe1 = Cotxe("Combustió", "Gasoil", "5")
cotxe_audi = Audi("200", "5", "3", "Combustió", "Gasoil", "5")
cotxe_audi.get_combustible()

cotxe1.get_portes()

cotxe_mercedes = Mercedes("Luxury")
cotxe_mercedes.set_portes("4")
cotxe_mercedes.get_portes()


