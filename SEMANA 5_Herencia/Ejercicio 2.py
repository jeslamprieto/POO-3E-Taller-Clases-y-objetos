class Animal:
    def __init__(self, nombre, especie):
        self.nombre = nombre
        self.especie = especie

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}")
        print(f"Especie: {self.especie}")

class Perro(Animal):
    def __init__(self, nombre, especie, raza):
        super().__init__(nombre, especie)
        self.raza = raza

    def mostrar_raza(self):
        print(f"Raza: {self.raza}")

perro1 = Perro("Loki", "Canino", "Labrador")

perro1.mostrar_info()
perro1.mostrar_raza()