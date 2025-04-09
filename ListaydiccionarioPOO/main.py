class Empleado:
    def __init__(self, emp_id, nombre, edad, salario):
        self.emp_id = emp_id
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

    def __str__(self):
        return f"ID: {self.emp_id}, Nombre: {self.nombre}, Edad: {self.edad}, Salario: {self.get_salario()} EUROS"

empleados = [
    Empleado(101, "Antonio", 30, 2500),
    Empleado(102, "Gerard", 45, 3200),
    Empleado(103, "Roger", 28, 2100),
    Empleado(104, "Ignasi", 35, 2800)
]

empleados_ordenados = sorted(empleados, key=lambda e: e.get_salario())

print("Empleados ordenados por salario:")
for emp in empleados_ordenados:
    print(emp)

print("\n")

empleados_por_id = {emp.emp_id: emp for emp in empleados}

id_buscado = 102
empleado_encontrado = empleados_por_id.get(id_buscado)

print(f"Empleado con ID {id_buscado}:")
if empleado_encontrado:
    print(empleado_encontrado)
else:
    print("No se encontró un empleado con ese ID!")
