
class Animal:
    def __init__(self):  # constructor
        self.tiene_hambre: bool = True  # propiedad
        self._el_lobo = 10  # protected

    def _sociedad_privada(self):
        print(self._el_lobo)

    def comer(self):  # metodo
        if (self.tiene_hambre):
            print('Comer 🍛')
            self.tiene_hambre = False
        else:
            print('Ya comió, no tiene hambre!')


animal = Animal()
animal.comer()
animal.comer()
print(animal.tiene_hambre)

animal._sociedad_privada()
print(animal._el_lobo)


# Herencia / Herencia Multiple
class Lobo(Animal):
    def __init__(self, color: str, tamanio: float):
        Animal.__init__(self)
        self.color = color
        self.tamanio = tamanio

    def cazar(self):
        print('Cazar')


class Perro(Animal, Lobo):
    def __init__(self, raza: str, color: str, tamanio: float):
        Lobo.__init__(self, color, tamanio)
        self.raza = raza

    def jugar(self):
        print('Jugar')


perrito = Perro('plomo', 1.32)
perrito.comer()
perrito.jugar()


# Dataclass (DTOs, record)

class Persona():
    def __init__(self):
        self.nombre: str
        self.esta_vivo: bool = True


# Clase, metodo y self
from dataclasses import dataclass
@dataclass # decorador o anotación
class Persona():
    nombre: str
    esta_vivo: bool = True
