## Clase Rectangulo

class Rectangulo:
    def __init__(self, largo, ancho):
        self.__largo = largo  
        self.__ancho = ancho  


    def set_dimensiones(self, largo, ancho):
        if largo > 0 and ancho > 0:
            self.__largo = largo
            self.__ancho = ancho
        else:
            raise ValueError("El largo y el ancho deben ser mayores que cero.")

    def get_dimensiones(self):
        print(f"Largo: {self.__largo}")
        print(f"Ancho: {self.__ancho}")


    def calcular_area(self):
        return self.__largo * self.__ancho


    def calcular_perimetro(self):
        return 2 * (self.__largo + self.__ancho)


rectangulo1 = Rectangulo(10, 5)

print("Dimensiones actuales:")
rectangulo1.get_dimensiones()

print(f"Area: {rectangulo1.calcular_area()}")
print(f"Perimetro: {rectangulo1.calcular_perimetro()}")


rectangulo1.set_dimensiones(20, 8)
print("\nDimensiones actualizadas:")
rectangulo1.get_dimensiones()

print(f"Area: {rectangulo1.calcular_area()}")
print(f"Perimetro: {rectangulo1.calcular_perimetro()}")