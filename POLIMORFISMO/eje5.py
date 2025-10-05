class Celular:
    def __init__(self, nroTel, dueño, espacio=64, ram=4, nroApp=0):
        self.nroTel = nroTel
        self.dueño = dueño
        self.espacio = espacio
        self.ram = ram
        self.nroApp = nroApp

    def mostrar(self):
        print(f"Tel: {self.nroTel}, Dueño: {self.dueño}, Espacio: {self.espacio}GB, RAM: {self.ram}GB, Apps: {self.nroApp}")

    def __add__(self, otro):  
        if isinstance(otro, int):
            return Celular(self.nroTel, self.dueño, self.espacio, self.ram, self.nroApp + otro)
        return self

    def __sub__(self, otro):  
        if isinstance(otro, int):
            return Celular(self.nroTel, self.dueño, self.espacio - otro, self.ram, self.nroApp)
        return self

c1 = Celular("789456", "Ana", 64, 4, 5)
c1.mostrar()

c2 = c1 + 10  
c3 = c1 - 5    

c2.mostrar()
c3.mostrar()