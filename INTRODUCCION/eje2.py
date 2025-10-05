class Bus:
    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.pasajeros_actuales = 0
        self.costopas = 1.50

    def sub_pasajeros(self, cantidad):
        if self.pasajeros_actuales + cantidad >= self.capacidad:
            self.pasajeros_actuales += self.capacidad
            print(f"subieron{cantidad} pasajeros. total: {self.pasajeros}")

        else:
            print("No hay espacio")

    def costo_pas(self):
        tot = self.pasajeros_actuales * self.costopas
        print(f"Se cobraron Bs.{tot:.2f} en pasajes")
        return tot

    def asientos_disp(self):
        disp = self.pasajeros_actuales = self.capacidad - self.pasajeros_actuales
        print(f"Asientos disponibles: {disp}")
        return disp

bus1 = Bus(capacidad=40)
bus1.sub_pasajeros(15)
bus1.sub_pasajeros(19)
bus1.asientos_disp()
bus1.costo_pas()
