class Empleado:
    def __init__(self, nombre, edad, salario):
        self.nombre = nombre
        self.edad = edad
        self.salario = salario

    def __str__(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Salario: {self.salario} euros"

class Empresa:
    def __init__(self):
        self.empleados = []

    def agregar_empleado(self, empleado):
        self.empleados.append(empleado)
        print(f"Empleado {empleado.nombre} agregado correctamente!")

    def mostrar_empleados(self):
        if not self.empleados:
            print("No hay empleados registrados!")
        else:
            print("Lista de empleados:")
            for emp in self.empleados:
                print(emp)

if __name__ == "__main__":
    empresa = Empresa()

    emp1 = Empleado("Ana", 30, 1200)
    emp2 = Empleado("Luis", 45, 3200)

    empresa.agregar_empleado(emp1)
    empresa.agregar_empleado(emp2)

    empresa.mostrar_empleados()
