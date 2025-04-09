class Empleado:
    def __init__(self, nombre, edad, salario):
        self.nombre = nombre
        self.edad = edad
        self.__salario = None
        self.set_salario(salario)

    def get_salario(self):
        return self.__salario

    def set_salario(self, nuevo_salario):
        if nuevo_salario >= 0:
            self.__salario = nuevo_salario
        else:
            print("Error! El salario no puede ser negativo!")

    def mostrar_informacion(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Salario: {self.get_salario()} euros"

    def __str__(self):
        return self.mostrar_informacion()

class Gerente(Empleado):
    def __init__(self, nombre, edad, salario, departamento):
        super().__init__(nombre, edad, salario)
        self.departamento = departamento

    def mostrar_informacion(self):
        info_base = super().mostrar_informacion()
        return f"{info_base}, Departamento: {self.departamento}"

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

    emp1 = Empleado("Ana", 30, 1500)
    gerente1 = Gerente("Carlos", 40, 2000, "Finanzas")

    empresa.agregar_empleado(emp1)
    empresa.agregar_empleado(gerente1)

    empresa.mostrar_empleados()
