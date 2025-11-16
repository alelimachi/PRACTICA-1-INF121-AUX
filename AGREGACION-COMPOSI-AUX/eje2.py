class Empleado:
    def __init__(self, nom, cargo, sueldo):
        self.nom = nom
        self.cargo = cargo
        self.sueldo = sueldo

    def ver(self):
        print("Nombre:", self.nom, "Cargo:", self.cargo, "Sueldo:", self.sueldo)

    def cambia(self, nuevo):
        self.sueldo = nuevo


class Departamento:
    def __init__(self, nom, area):
        self.nom = nom
        self.area = area
        self.emp = []

    def ver(self):
        print("Departamento:", self.nom, "-", self.area)
        if len(self.emp) == 0:
            print(" Sin empleados.")
            return
        for i in range(len(self.emp)):
            print("", i+1, ". ", end="")
            self.emp[i].ver()

    def add(self, e):
        self.emp.append(e)

    def subir(self, porc):
        for e in self.emp:
            nuevo = e.sueldo + e.sueldo * porc / 100
            e.cambia(nuevo)
        print("Sueldos actualizados en", self.nom)

    def tiene(self, e):
        return e in self.emp

    def mover(self, otro):
        cant = len(self.emp)
        for e in self.emp:
            otro.add(e)
        self.emp = []
        print("Movidos", cant, "empleados de", self.nom, "a", otro.nom)

d1 = Departamento("Recursos Humanos", "Administración")
d2 = Departamento("Contabilidad", "Finanzas")

e1 = Empleado("Ana", "Secretaria", 3500)
e2 = Empleado("Luis", "Analista", 4200)
e3 = Empleado("María", "Jefa", 5800)
e4 = Empleado("Carlos", "Asistente", 3000)
e5 = Empleado("Elena", "Contadora", 4500)

d1.add(e1)
d1.add(e2)
d1.add(e3)
d1.add(e4)
d1.add(e5)

print("Empleados Dpto 1")
d1.ver()
print()

print("Empleados Dpto 2")
d2.ver()
print()

d1.subir(10)
d1.ver()
print()

if d2.tiene(e3):
    print(e3.nom, "está en", d2.nom)
else:
    print(e3.nom, "NO está en", d2.nom)
print()

d1.mover(d2)
print()

print("NUEVOS DEPTOS")
d1.ver()
print()
d2.ver()
