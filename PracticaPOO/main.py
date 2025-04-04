from unicodedata import normalize

#Comencem creant la classe base que serà projecte.
class Projecte:
    def __init__(self, nom, durada, llenguatge_principal): #Es defineixen els atributs.
        self.nom = nom
        self.durada = durada
        self.llenguatge_principal = llenguatge_principal
        self.tasques = [] #[] S'utilitza per emmagatzemar la llista de tasques en aquest cas.

    def mostrar_informació(self): #Creem el mètode per mostrar la informació.
        return f"Nom: {self.nom}, Durada: {self.durada}, Llenguatge_principal: {self.llenguatge_principal}"

    def afegir_tasca(self, tasca): #Es crea el mètode per afegir tasques que després es podrà utilitzar per afegir tasques tant al projecte intern com extern.
        self.tasques.append(tasca)

    def mostrar_tasques(self): #Es crea el mètode per mostrar les tasques.
        resultat = ""
        for tasca in self.tasques:
            resultat += tasca.__str__() + "\n"
        return resultat.strip()

class Projecte_intern(Projecte): #Es crea la subclasse Projecte intern.
    def __init__(self, nom, durada, llenguatge_principal, responsable, departament): #Es defineixen els atributs.
        super().__init__(nom, durada, llenguatge_principal)
        self.responsable = responsable
        self.departament = departament

    def mostrar_informació(self): #Es crida al mètode per mostrar informació i s'afegeixen els nous atributs d'aquesta subclasse.
        base_info = super().mostrar_informació()
        return f"{base_info}, Responsable: {self.responsable}, Departament: {self.departament}"

class Projecte_extern(Projecte): #Es crea la subclasse Projecte extern.
    def __init__(self, nom, durada, llenguatge_principal, client, pressupost): # S'afegeixen els nous atributs d'aquesta subclasse.
        super().__init__(nom, durada, llenguatge_principal)
        self.client = client
        self.pressupost = pressupost

    def mostrar_informació(self): #Es crida al mètode per mostrar la informació de la subclasse.
        base_info = super().mostrar_informació()
        return f"{base_info}, Client: {self.client}, Pressupost: {self.pressupost}"

class Membre: #Es crea la classe membre.
    def __init__(self, nom, rol, experiència): #Es posen els atributs.
        self.nom = nom
        self.rol = rol
        self.experiència = experiència

    def __str__(self): #Es crea el mètode per mostrar la informació amb __str__.
        return f"Nom: {self.nom}, Rol: {self.rol}, Experiència: {self.experiència}"

class Equip: #Es crea la classe Equip.
    def __init__(self, nom): #Es posen els atributs de la classe.
        self.nom = nom
        self.membres = [] #[] Per emmagatzemar els membres.

    def afegir_membre(self, membre): #Mètode per afegir membres a la llista.
        self.membres.append(membre)

    def mostrar_membres(self): #Mètode per mostrar els membres que hi ha.
        resultat = ""
        for membre in self.membres:
            resultat += membre.__str__() + "\n"
        return resultat.strip()

    def __str__(self): #Es mostren els atributs amb __str__ i en un principi em donava error i buscant a google he trobat la funció "len" i ja em surt correctament el número.
        return f"Nom Equip: {self.nom}, Membres: {len(self.membres)}"

class Tasca: #Es crea la classe Tasca.
    def __init__(self, títol, estat, responsable): # S'afegeixen els atributs.
        self.títol = títol
        self.estat = estat
        self.responsable = responsable

    def __str__(self): #Es mostren els atributs amb __str__.
        return f"Títol: {self.títol}, Estat: {self.estat}, Responsable: {self.responsable}."

if __name__ == "__main__":
    # Crear un projecte intern
    Projecte_intern = Projecte_intern(
        nom="Aplicació CRM Interna",
        durada="12 mesos",
        llenguatge_principal="Python",
        responsable="Joan Rovira",
        departament="IT"
    )

    # Crear un projecte extern
    Projecte_extern = Projecte_extern(
        nom="Plataforma E-learning",
        durada="18 mesos",
        llenguatge_principal="Java",
        client="Educorp",
        pressupost="300K"
    )

    # Crear un equip i membres
    equip = Equip("Equip Desenvolupament")
    membre1 = Membre("Anna", "Desenvolupadora", "3 anys")
    membre2 = Membre("Marc", "Tester", "2 anys")
    equip.afegir_membre(membre1)
    equip.afegir_membre(membre2)

    # Afegir tasques al projecte intern
    tasca1 = Tasca("Definir requeriments", "pendent", membre1)
    tasca2 = Tasca("Provar funcionalitats", "pendent", membre2)
    Projecte_intern.afegir_tasca(tasca1)
    Projecte_intern.afegir_tasca(tasca2)

    # Mostrar informació del projecte intern
    print("Informació del projecte intern:")
    print(Projecte_intern.mostrar_informació())
    print("\nTasques del projecte intern:")
    print(Projecte_intern.mostrar_tasques())

    # Mostrar informació de l'equip
    print("\nInformació de l'equip:")
    print(equip.__str__())
    print("\nMembres de l'equip:")
    print(equip.mostrar_membres())

    # Mostrar informació del projecte extern
    print("\nInformació del projecte extern:")
    print(Projecte_extern.mostrar_informació())

