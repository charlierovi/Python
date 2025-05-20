class Empleado:
    def __init__(self, nombre, edad, salario):
        self.nombre = nombre
        self.edad = edad
        self.__salario = None
        self.set_salario(salario)  # Usamos el setter para validar

    def get_salario(self):
        return self.__salario

    def set_salario(self, salario):
        if salario < 0:
            print("Error: El salario no puede ser negativo!")
        else:
            self.__salario = salario

    def mostrar_informacion(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Salario: {self.__salario} euros"

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
        print(f"El empleado {empleado.nombre} ha sido agregado correctamente!")

    def mostrar_empleados(self):
        if not self.empleados:
            print("No hay empleados en la empresa!")
        else:
            print("Lista de empleados:")
            for emp in self.empleados:
                print(emp)


empresa = Empresa()

empleado1 = Empleado("Antonio", 30, 1500)
gerente1 = Gerente("Ignasi", 45, 3500, "Educacion")

empresa.agregar_empleado(empleado1)
empresa.agregar_empleado(gerente1)

empresa.mostrar_empleados()
