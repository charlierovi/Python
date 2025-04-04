class Alumne:
    def __init__(self, nom, cognoms, edat, assignatura, nota):
        self.nom=nom
        self.cognoms=cognoms
        self.edat=edat
        self.assignatura=assignatura
        self.nota=nota

    def consultar_nota(self):
        print(f"La nota és: {self.nota}.")

    def ficar_nota(self, nova_nota):
        if nova_nota<=10:
            self.nota=nova_nota
        else:
            print("La nota és erronea.")

    def actualitzar_edat(self, nova_edat):
        self.edat=nova_edat

    def consultar_dades_alumne(self):
        print(f"Nom: {self.nom}, Cognoms: {self.cognoms}, Assignatura: {self.assignatura}, Edat: {self.edat}, Nota: {self.nota}")

