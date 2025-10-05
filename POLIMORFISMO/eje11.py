class Pasajero:
    def __init__(self, nombre, edad, genero, nroHabitacion, costoPasaje):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero  
        self.nroHabitacion = nroHabitacion
        self.costoPasaje = costoPasaje

    def mostrar(self):
        print(f"{self.nombre}, {self.edad} años, {self.genero}, Hab: {self.nroHabitacion}, Costo: {self.costoPasaje}")

class Crucero:
    def __init__(self, nombre, origen, destino):
        self.nombre = nombre
        self.paisOrigen = origen
        self.paisDestino = destino
        self.pasajeros = []

    def __add__(self, pasajero):
        if isinstance(pasajero, Pasajero):
            nuevo_crucero = Crucero(self.nombre, self.paisOrigen, self.paisDestino)
            nuevo_crucero.pasajeros = self.pasajeros[:]
            nuevo_crucero.pasajeros.append(pasajero)
            return nuevo_crucero
        return self  

    def __sub__(self, pasajero):
        if pasajero in self.pasajeros:
            self.pasajeros.remove(pasajero)
        return self

    def __eq__(self, otro):
        if isinstance(otro, Crucero):
            return self.sumaCostos() == otro.sumaCostos()
        return False

    def __len__(self):
        return len(self.pasajeros)

    def contarGenero(self, genero):
        return sum(1 for p in self.pasajeros if p.genero == genero)

    def sumaCostos(self):
        return sum(p.costoPasaje for p in self.pasajeros)

    def mostrar(self):
        print(f"Crucero: {self.nombre} ({self.paisOrigen} , {self.paisDestino})")
        print("Pasajeros:")
        for p in self.pasajeros:
            p.mostrar()
        print(f"Total Pasajeros: {len(self.pasajeros)}")
        print(f"Costo total pasajes: {self.sumaCostos()}")

c1 = Crucero("Caribeño", "Bolivia", "Brasil")
c2 = Crucero("Pacífico", "Chile", "Perú")

p1 = Pasajero("Juan Vargas", 30, "M", 502, 500)
p2 = Pasajero("Martina Vasques", 25, "F", 603, 1000)
p3 = Pasajero("Wilmer Montero", 28, "M", 401, 925)
p4 = Pasajero("Ana Flores", 22, "F", 405, 750)
p5 = Pasajero("Carlos Rojas", 35, "M", 410, 600)

c1 = c1 + p1
c1 = c1 + p2
c1 = c1 + p3

c2 = c2 + p4
c2 = c2 + p5

c1.mostrar()
c2.mostrar()

print("¿Costo total igual entre c1 y c2? ", c1 == c2)

print("¿Misma cantidad de pasajeros? ", len(c1) == len(c2))

print("Crucero 1 - Hombres:", c1.contarGenero("M"), "Mujeres:", c1.contarGenero("F"))
print("Crucero 2 - Hombres:", c2.contarGenero("M"), "Mujeres:", c2.contarGenero("F"))
