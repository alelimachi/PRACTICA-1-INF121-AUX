class Parada:
    def __init__(self, nombreP="Sin nombre"):
        self.nombreP = nombreP
        self.admins = []
        self.autos = []   

    def adicionar(self, admin):
        if isinstance(admin, str):  
            if len(self.admins) < 10:
                self.admins.append(admin)

    def adicionar_auto(self, modelo, conductor, placa):
        if len(self.autos) < 10:
            self.autos.append([modelo, conductor, placa])
            
    def mostrar(self):
        print(f"Parada: {self.nombreP}")
        print("Administradores:")
        for a in self.admins:
            print("-", a)
        print("Autos:")
        for auto in self.autos:
            print(f"Modelo: {auto[0]}, Conductor: {auto[1]}, Placa: {auto[2]}")

p1 = Parada("Parada Central")
p1.adicionar("Luis")
p1.adicionar("Marta")
p1.adicionar_auto("Toyota", "Carlos", "HTR-123")
p1.adicionar_auto("Nissan", "Jorge", "HIN-234")
p1.mostrar()