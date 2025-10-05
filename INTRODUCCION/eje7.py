class Mascota:
    def __init__(self, nombre, tipo, energia = 50):
        self.nombre = nombre
        self.tipo = tipo
        self.energia = energia

    def alimentar(self):
        self.energia += 20
        if self.energia > 100:
            self.energia = 100
        print(f"{self.nombre} fue alimentado. Energia: {self.energia}")

    def jugar(self):
        self.energia -= 15
        if self.energia < 0:
            self.energia = 0
        print(f"{self.nombre} jugo. Energia: {self.energia}")


m1 = Mascota("Fido", "Perro")
m2 = Mascota("Tommy", "Gato")

m1.alimentar()
m1.jugar()

m2.jugar()
m2.alimentar()
