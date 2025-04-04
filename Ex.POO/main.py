class Persona:
    def __init__(self, nom, edat):
        self.nom = nom
        self.edat = edat

    def parlar(self):
        print(f"{self.nom} està parlant.")

    def digues_edad(self):
        print(f"Tinc {self.edat} anys.")

pepe=Persona("pepe","20")
pepe.parlar()
pepe.digues_edad()