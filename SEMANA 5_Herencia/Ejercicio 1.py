class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")

class Estudiante(Persona):
    def __init__(self, nombre, edad, grado):
        super().__init__(nombre, edad)
        self.grado = grado

    def mostrar_grado(self):
        print(f"Grado: {self.grado}")


estudiante1 = Estudiante("Pepito", 15, "10mo")

estudiante1.mostrar_info()
estudiante1.mostrar_grado()