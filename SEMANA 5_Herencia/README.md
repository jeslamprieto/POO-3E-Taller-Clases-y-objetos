# SEMANA 5 - Herencia en POO

Ejercicios prácticos sobre el concepto de Herencia en Programación Orientada a Objetos usando Python.

---

## Ejercicio 1 - Sistema Escolar

Clases: `Persona` (padre) y `Estudiante` (hijo)

- `Persona` tiene los atributos `nombre` y `edad`, y el método `mostrar_info()`
- `Estudiante` hereda de `Persona`, agrega el atributo `grado` y el método `mostrar_grado()`

---

## Ejercicio 2 - Clínica Veterinaria

Clases: `Animal` (padre) y `Perro` (hijo)

- `Animal` tiene los atributos `nombre` y `especie`, y el método `mostrar_info()`
- `Perro` hereda de `Animal`, agrega el atributo `raza` y el método `mostrar_raza()`

---

## Ejercicio 3 - Sistema de Vehículos

Clases: `Vehiculo` (padre) y `Coche` (hijo)

- `Vehiculo` tiene los atributos `marca` y `anio`, y el método `mostrar_info()`
- `Coche` hereda de `Vehiculo`, agrega el atributo `modelo` y el método `mostrar_modelo()`

---

## Conceptos aplicados

- Herencia simple
- Uso de `super().__init__()` para reutilizar el constructor del padre
- Atributos y métodos propios de la clase hija