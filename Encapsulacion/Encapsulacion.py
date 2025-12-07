# EJEMPLO DE ENCAPSULACIÓN

class Persona:

    def __init__(self, nombre, edad):
        self.__nombre = nombre   # Atributo privado
        self.__edad = edad       # Atributo privado

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_nombre(self):
        return self.__nombre

    def set_edad(self, edad):
        self.__edad = edad

    def get_edad(self):
        return self.__edad


# PROGRAMA PRINCIPAL
p = Persona("Luis", 20)

print("Nombre:", p.get_nombre())
print("Edad:", p.get_edad())

p.set_nombre("Carlos")
p.set_edad(25)

print("Nuevo nombre:", p.get_nombre())
print("Nueva edad:", p.get_edad())
