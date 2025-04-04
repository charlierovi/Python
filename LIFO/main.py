#Crea una classe anomenada Cola_LIFO que implementi una cua LIFO (pila) utilitzant una llista. A diferència de la cua de prioritat, aquí els elements s'afegiran i s'extreuran seguint el principi Last In, First Out (últim en entrar, primer en sortir).
#Es crea la classe Cola_LIFO i es defineix una llista.
class Cola_LIFO:
    def __init__(self):
        self.elements = []
#Es crea la funció afegir amb append.
    def afegir(self, element):
        self.elements.append(element)
#Es crea la funció extreure amb pop.
    def extreure(self):
        if not self.buit():
            return self.elements.pop()
#Es crea la funció veure darrer.
    def veure_darrer(self):
        if not self.buit():
            return self.elements[-1]
#Es crea la funció buit per saber si està buit o no.
    def buit(self):
        return len(self.elements) == 0
#Es crea la funció lonfitud per saber quants elements hi ha.
    def longitud(self):
        return len(self.elements)
#EXEMPLE DE FUNCIONAMENT
pila = Cola_LIFO()
pila.afegir("A")
pila.afegir("B")
pila.afegir("C")

print(pila.veure_darrer())
print(pila.extreure())
print(pila.veure_darrer())
print(pila.longitud())
print(pila.buit())
pila.extreure()
pila.extreure()
print(pila.buit())

