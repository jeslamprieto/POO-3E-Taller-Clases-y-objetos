class Vehiculo:
    def __init__(self, marca, anio):
        self.marca = marca
        self.anio = anio

    def mostrar_info(self):
        print(f"Marca: {self.marca}")
        print(f"Año: {self.anio}")

class Coche(Vehiculo):
    def __init__(self, marca, anio, modelo):
        super().__init__(marca, anio)
        self.modelo = modelo

    def mostrar_modelo(self):
        print(f"Modelo: {self.modelo}")

coche1 = Coche("Toyota", 2022, "Corolla")

coche1.mostrar_info()
coche1.mostrar_modelo()