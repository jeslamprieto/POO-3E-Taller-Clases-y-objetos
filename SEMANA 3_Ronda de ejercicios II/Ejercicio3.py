## Clase Estudiante
class Estudiante:
    def __init__(self, nombre, edad):
        self.__nombre = nombre  
        self.__edad = edad      
        self.__notas = []       

    
    def get_nombre(self):
        return self.__nombre

    
    def get_edad(self):
        return self.__edad

    def agregar_nota(self, nota):
        if 0 <= nota <= 100:
            self.__notas.append(nota)
        else:
            raise ValueError("La nota debe estar entre 0 y 100.")

    def calcular_promedio(self):
        if len(self.__notas) == 0:
            return 0
        return sum(self.__notas) / len(self.__notas)


estudiante1 = Estudiante("Pepito", 20)

print(f"Nombre: {estudiante1.get_nombre()}")
print(f"Edad: {estudiante1.get_edad()}")

estudiante1.agregar_nota(85)
estudiante1.agregar_nota(90)
estudiante1.agregar_nota(78)

print(f"Promedio: {estudiante1.calcular_promedio()}")