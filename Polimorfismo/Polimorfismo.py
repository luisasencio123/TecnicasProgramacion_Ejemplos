# EJEMPLO DE POLIMORFISMO

class Ave:
    def volar(self):
        return "El ave está volando"


class Pinguino(Ave):
    def volar(self):
        return "El pingüino NO puede volar"


class Aguila(Ave):
    def volar(self):
        return "El águila vuela muy alto"


# PROGRAMA PRINCIPAL
aves = [Ave(), Pinguino(), Aguila()]

for a in aves:
    print(a.volar())
