class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def desplazarse(self):
        return "El animal se desplaza."


class Leon(Animal):
    def desplazarse(self):
        return f"{self.nombre} corre por la jungla."


class Pinguino(Animal):
    def desplazarse(self):
        return f"{self.nombre} nada y camina."


class Canguro(Animal):
    def desplazarse(self):
        return f"{self.nombre} salta grandes distancias."

animales = [
    Leon("Simba", 5),
    Pinguino("Pingu", 3),
    Canguro("Jack", 7)
]

for animal in animales:
    print(animal.desplazarse())
