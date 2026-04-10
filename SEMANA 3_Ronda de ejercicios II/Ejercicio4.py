## Clase Libro
class Libro:
    def __init__(self, titulo, autor, total_paginas):
        self.__titulo = titulo              
        self.__autor = autor                
        self.__total_paginas = total_paginas  
        self.__pagina_actual = 1            

    def avanzar_paginas(self, num_paginas):
        if self.__pagina_actual + num_paginas > self.__total_paginas:
            raise ValueError("No puedes avanzar mas alla del total de paginas.")
        else:
            self.__pagina_actual += num_paginas

    def retroceder_paginas(self, num_paginas):
        if self.__pagina_actual - num_paginas < 1:
            raise ValueError("No puedes retroceder mas alla de la pagina 1.")
        else:
            self.__pagina_actual -= num_paginas

    def get_pagina_actual(self):
        return self.__pagina_actual

    def get_info(self):
        print(f"Titulo: {self.__titulo}")
        print(f"Autor: {self.__autor}")
        print(f"Total de paginas: {self.__total_paginas}")
        print(f"Pagina actual: {self.__pagina_actual}")


libro1 = Libro("Cien años de soledad", "Gabriel Garcia Marquez", 471)

print("Informacion del libro:")
libro1.get_info()

libro1.avanzar_paginas(50)
print(f"\nDespues de avanzar 50 paginas: {libro1.get_pagina_actual()}")

libro1.retroceder_paginas(20)
print(f"Despues de retroceder 20 paginas: {libro1.get_pagina_actual()}")