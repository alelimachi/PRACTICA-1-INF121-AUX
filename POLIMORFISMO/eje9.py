class Estudiante:
    def __init__(self, nombre, apellidos, p1, p2, ex):
        self.nombre = nombre
        self.apellidos = apellidos
        self.parcial1 = p1
        self.parcial2 = p2
        self.exFinal = ex

    def notaFinal(self):
        """Suma simple"""
        return self.parcial1 + self.parcial2 + self.exFinal

    def notaFinal100(self):
        return self.parcial1 * 0.3 + self.parcial2 * 0.3 + self.exFinal * 0.4

    def aprobo(self):
        return self.notaFinal100() >= 51

    def aproboMin(self, notaMinima):
        return self.notaFinal100() >= notaMinima

    def aproboConExamen(self, notaMinima, notaExFinal):
        return self.notaFinal100() >= notaMinima and self.exFinal >= notaExFinal

    def mostrar(self):
        print(f"Estudiante: {self.nombre} {self.apellidos}")
        print(f"Parcial1: {self.parcial1}, Parcial2: {self.parcial2}, ExFinal: {self.exFinal}")

    def mostrarConNota(self):
        self.mostrar()
        print(f"Nota Final (sobre 100): {self.notaFinal100()}")

e1 = Estudiante("Juan", "Perez", 60, 70, 80)
e2 = Estudiante("Maria", "Lopez", 40, 50, 60)
e3 = Estudiante("Luis", "Mamani", 30, 25, 70)

e1.mostrarConNota()
print("¿Aprobó? ", e1.aprobo())

e2.mostrarConNota()
print("¿Aprobó con 51? ", e2.aproboMin(51))

e3.mostrarConNota()
print("¿Aprobó con nota mínima 51 y ExFinal >=30? ", e3.aproboConExamen(51, 30))