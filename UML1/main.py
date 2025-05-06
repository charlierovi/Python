class Persona:
    def __init__(self, nombre, edad):
        self.nombre=nombre
        self.edad=edad

    def hablar(self):
        print(f"{self.nombre} está hablando.")

    def caminar(self):
        print(f"{self.nombre} tiene {self.edad} años y camina poco.")

class Estudiante(Persona):
    def __init__(self, nombre, edad, matricula):
        super().__init__(nombre, edad)
        self.matricula=matricula

    def estudiar(self):
        print(f"{self.nombre} que tiene {self.edad} años, tiene que estudiar {self.matricula}.")

persona1=Persona("Carlos", 26)
persona1.hablar()
persona1.caminar()

estudiante1=Estudiante("Roger", 25, "DAM")
estudiante1.hablar()
estudiante1.caminar()
estudiante1.estudiar()
