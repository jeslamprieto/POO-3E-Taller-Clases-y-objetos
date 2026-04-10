## Clase Empleado
class Empleado:
    total_empleados = 0

    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario
        Empleado.total_empleados += 1

    @classmethod
    def cantidad_empleados(cls):
        return cls.total_empleados



empleado1 = Empleado("Pepito", 3000)
empleado2 = Empleado("Juancho", 4500)
empleado3 = Empleado("Maria", 3800)

print(f"Total de empleados: {Empleado.cantidad_empleados()}")