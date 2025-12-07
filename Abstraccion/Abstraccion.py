# EJEMPLO DE ABSTRACCIÓN

from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def sonido(self):
        pass  # Método abstracto

class Perro(Animal):
    def sonido(self):
        return "Guau!"

class Gato(Animal):
    def sonido(self):
        return "Miau!"

# PROGRAMA PRINCIPAL
p = Perro()
g = Gato()

print(p.sonido())
print(g.sonido())
