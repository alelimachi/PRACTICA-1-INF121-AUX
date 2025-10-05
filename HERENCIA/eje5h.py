class Vehiculo:
    def __init__(self, conductor, placa, id_vehiculo):
        self.conductor = conductor
        self.placa = placa
        self.id = id_vehiculo

    def mostrar_info(self):
        return f"Placa: {self.placa}, Conductor: {self.conductor}"

    def cambiar_conductor(self, nuevo_conductor):
        self.conductor = nuevo_conductor


class Bus(Vehiculo):
    def __init__(self, conductor, placa, id_vehiculo, capacidad, sindicato):
        Vehiculo.__init__(self, conductor, placa, id_vehiculo)
        self.capacidad = capacidad
        self.sindicato = sindicato


class Auto(Vehiculo):
    def __init__(self, conductor, placa, id_vehiculo, caballos_fuerza, descapotable):
        Vehiculo.__init__(self, conductor, placa, id_vehiculo)
        self.caballos_fuerza = caballos_fuerza
        self.descapotable = descapotable


class Moto(Vehiculo):
    def __init__(self, conductor, placa, id_vehiculo, cilindro, casco):
        Vehiculo.__init__(self, conductor, placa, id_vehiculo)
        self.cilindro = cilindro
        self.casco = casco


# ----------- PRUEBA -----------
bus = Bus("Juan", "123-XYZ", 1, 50, "Sindicato A")
auto = Auto("Ana", "456-ABC", 2, 120, True)
moto = Moto("Luis", "789-QWE", 3, 250, True)

print("Información de los vehículos:")
print("Bus:", bus.mostrar_info())
print("Auto:", auto.mostrar_info())
print("Moto:", moto.mostrar_info())

auto.cambiar_conductor("Pedro")
print("\nDespués del cambio de conductor del auto:")
print("Auto:", auto.mostrar_info())
