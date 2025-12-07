# EJEMPLO DE HERENCIA

class Vehiculo:
    def __init__(self, marca):
        self.marca = marca

    def encender(self):
        return "El vehículo está encendido"


class Carro(Vehiculo):
    def tocar_claxon(self):
        return "Bip bip!"


# PROGRAMA PRINCIPAL
c = Carro("Toyota")

print("Marca:", c.marca)
print(c.encender())
print(c.tocar_claxon())
