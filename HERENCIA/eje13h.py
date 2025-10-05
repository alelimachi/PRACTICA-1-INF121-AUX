class Empleado:
    def __init__(self, nombre, sueldomes):
        self.nombre = nombre
        self.sueldomes = sueldomes

    def sueldo_total(self):
        return self.sueldomes

    def __str__(self):
        return f"Empleado - {self.nombre}, Sueldo Base: {self.sueldomes}"
    
class Administrativo(Empleado):
    def __init__(self, nombre, sueldomes, cargo):
        super().__init__(nombre, sueldomes)
        self.cargo = cargo

    def __str__(self):
        return f"Administrativo: {self.nombre}, Cargo: {self.cargo}, Sueldo Base: {self.sueldomes}"


class Chef(Empleado):
    def __init__(self, nombre, sueldomes, horaExtra, tipo, sueldoHora):
        super().__init__(nombre, sueldomes)
        self.horaExtra = horaExtra
        self.tipo = tipo
        self.sueldoHora = sueldoHora

    def sueldo_total(self):
        return self.sueldomes + self.horaExtra * self.sueldoHora

    def __str__(self):
        return (f"Chef: {self.nombre}, Tipo: {self.tipo}, "
                f"Sueldo Base: {self.sueldomes}, Total: {self.sueldo_total()}")


class Mesero(Empleado):
    def __init__(self, nombre, sueldomes, propina, horaExtra, sueldoHora):
        super().__init__(nombre, sueldomes)
        self.propina = propina
        self.horaExtra = horaExtra
        self.sueldoHora = sueldoHora

    def sueldo_total(self):
        return self.sueldomes + self.propina + self.horaExtra * self.sueldoHora

    def __str__(self):
        return (f"Mesero: {self.nombre}, Sueldo Base: {self.sueldomes}, "
                f"Propina: {self.propina}, Total: {self.sueldo_total()}")


# Lista de empleados
empleados = [
    Chef("Manuel", 3000, horaExtra=10, tipo="Pastelero", sueldoHora=50),
    Mesero("Alfredo", 2000, propina=300, horaExtra=5, sueldoHora=20),
    Mesero("Carlos", 2200, propina=250, horaExtra=8, sueldoHora=25),
    Administrativo("Jorge", 2500, "Gerente"),
    Administrativo("Ana", 2800, "Supervisor"),
]

X = 2500
print(f"\nEmpleados con sueldo mensual = {X}:")
for e in empleados:
    if e.sueldomes == X:
        print(e)

print("\nSueldo total de cada empleado:")
for e in empleados:
    print(f"{e.nombre}: {e.sueldo_total()}")
