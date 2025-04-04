class Persona:
    def __init__(self, nom, edat):
        self.nom = nom
        self.edat = edat

    def parlar(self):
        print(f"{self.nom} esta parlant.")

class Estudiant(Persona):
    def __init__(self, nom, edat, estudi):
        super().__init__(nom, edat)
        self.estudi = estudi

    def estudiar(self):
        print(f"{self.nom} esta estudiant {self.estudi}.")

estudiante_pepe=Estudiant('Pepe', '18', 'DAM1')
estudiante_pepe.parlar()
estudiante_pepe.estudiar()