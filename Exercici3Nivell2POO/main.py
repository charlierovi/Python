class Empleado:
    def __init__(self, id, nombre, salario):
        self.id = id
        self.nombre = nombre
        self.salario = salario

    def __repr__(self):
        return f"Empleado(ID={self.id}, Nombre={self.nombre}, Salario={self.salario})"

empleados = [
    Empleado(3, "Antonio", 1500),
    Empleado(1, "Ignasi", 1200),
    Empleado(2, "Joan", 1800),
]

empleados.sort(key=lambda emp: emp.salario)

print("Lista de empleados ordenada por salario:")
for e in empleados:
    print(e)

empleados_por_id = {emp.id: emp for emp in empleados}

print("\nEmpleado con ID 2:")
print(empleados_por_id[2])
