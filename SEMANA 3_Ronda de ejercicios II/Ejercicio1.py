## Clase Producto
class Producto:
    def __init__(self, nombre, precio):
        self.__nombre = nombre  
        self.__precio = precio  


    def get_nombre(self):
        return self.__nombre


    def get_precio(self):
        return self.__precio


    def set_precio(self, nuevo_precio):
        if nuevo_precio > 0:
            self.__precio = nuevo_precio
        else:
            raise ValueError("El precio debe ser mayor que cero.")


    def aplicar_descuento(self, porcentaje):
        if 0 < porcentaje <= 100:
            self.__precio -= self.__precio * (porcentaje / 100)
        else:
            raise ValueError("El porcentaje debe estar entre 0 y 100.")



producto1 = Producto("Laptop", 1200)

print(f"Nombre: {producto1.get_nombre()}")
print(f"Precio inicial: ${producto1.get_precio()}")


producto1.set_precio(1500)
print(f"Precio actualizado: ${producto1.get_precio()}")


producto1.aplicar_descuento(10)
print(f"Precio con 10% de descuento: ${producto1.get_precio()}")