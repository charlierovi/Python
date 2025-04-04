class Persona:
    def __init__(self, nom):
        self.nom = nom

class Professor(Persona):
    def __init__(self, nom, sou):
        super().__init__(nom)
        self.sou = sou

    def cobrar(self):
        print(f"{self.nom} cobra aixo: {self.sou}.")

professor_Ignasi=Professor('Ignasi', '2000')
professor_Ignasi.cobrar()
