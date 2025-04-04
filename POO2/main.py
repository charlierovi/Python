class Persona:
    def __init__(self, nom, cognom, dni):
        self.nom = nom
        self.cognoms = cognom
        self.dni = dni

    def presentar(self):
        print(f"Hola, em dic {self.nom} {self.cognom}.")

class Estudiant(Persona):
    def __init__(self, nom, cognom, dni, curs):
        super().__init__(nom, cognom, dni)
        self.curs = curs

    def presentar(self):
        super().presentar()
        print(f"Sóc estudiant de {self.curs}.")

class Professor(Persona):
    def __init__(self, nom, cognom, dni, assignatura):
        super().__init__(nom, cognom, dni)
        self.assignatura = assignatura

    def presentar(self):
        super().presentar()
        print(f"Sóc professor de {self.assignatura}.")

class Escola:
    def __init__(self, nom):
        self.nom = nom
        self.estudiants = []
        self.professors = []

    def afegirestudiant(self, estudiant):
        if isinstance(estudiant, Estudiant):
            self.estudiants.append(estudiant)
        else:
            print("Error: No es pot afegir un objecte que no sigui Estudiant a la llista.")

    def afegirprofessor(self, professor):
        if isinstance(professor, Professor):
            self.professors.append(professor)
        else:
            print("Error: No es pot afegir un objecte que no sigui Professor a la llista.")

    def llistarestudiants(self):
        print(f"Estudiants a l'escola {self.nom}:")
        for estudiant in self.estudiants:
            estudiant.presentar()
            print("---")

    def llistarprofessors(self):
        print(f"Professors a l'escola {self.nom}:")
        for professor in self.professors:
            professor.presentar()
            print("---")

    def llistarpersones(self):
        self.llistarprofessors()
        self.llistarestudiants()
