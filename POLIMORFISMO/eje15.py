class Ordenador:
    def __init__(self, codigo, numero, ram, procesador, estado):
        self.codigo = codigo
        self.numero = numero
        self.ram = ram
        self.procesador = procesador
        self.estado = estado 

    def __str__(self):
        return f"PC[{self.codigo}] Nro {self.numero} RAM: {self.ram}GB " \
               f"CPU: {self.procesador}  Estado: {self.estado}"

class Laboratorio:
    def __init__(self, nombre, capacidad):
        self.nombre = nombre
        self.capacidad = capacidad
        self.ordenadores = []

    def agregar(self, ordenador: Ordenador):
        if len(self.ordenadores) < self.capacidad:
            self.ordenadores.append(ordenador)

    def informacion(self, tipo="todos"):
        if tipo == "estado":
            activos = []
            inactivos = []
            for pc in self.ordenadores:
                if pc.estado == "activo":
                    activos.append(pc)
                else:
                    inactivos.append(pc)
            print("\nActivos:")
            for pc in activos:
                print(" ", pc)
            print("Inactivos:")
            for pc in inactivos:
                print(" ", pc)
        elif tipo == "ram":
            for pc in self.ordenadores:
                if pc.ram > 8:
                    print(pc)
        else:  
            print(f"\nLaboratorio {self.nombre}:")
            for pc in self.ordenadores:
                print(" ", pc)

    def __str__(self):
        return f"Laboratorio {self.nombre} Capacidad: {self.capacidad}" \
               f"Ordenadores: {len(self.ordenadores)}"

def trasladar(lab1: Laboratorio, lab2: Laboratorio):
    print("Antes del traslado")
    lab1.informacion()
    lab2.informacion()
    while lab1.ordenadores:
        pc = lab1.ordenadores.pop()
        lab2.agregar(pc)
    print(" Después del traslado ")
    lab1.informacion()
    lab2.informacion()

pc1 = Ordenador("A1", 101, 4, "i3", "activo")
pc2 = Ordenador("A2", 102, 16, "i7", "activo")
pc3 = Ordenador("A3", 103, 8, "i5", "inactivo")
pc4 = Ordenador("A4", 104, 12, "Ryzen 5", "activo")
pc5 = Ordenador("A5", 105, 6, "i3", "inactivo")
pc6 = Ordenador("A6", 106, 32, "i9", "activo")

lab1 = Laboratorio("Lasin 1", 10)
lab2 = Laboratorio("Lasin 2", 10)

for pc in [pc1, pc2, pc3, pc4, pc5, pc6]:
    lab1.agregar(pc)

lab1.informacion("estado")

print("PC con más de 8GB RAM:")
lab1.informacion("ram")

trasladar(lab1, lab2)
