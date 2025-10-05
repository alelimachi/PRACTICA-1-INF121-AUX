class Persona:
    def __init__(self, nombre, paterno, materno, edad):
        self._nombre = nombre
        self._paterno = paterno
        self._materno = materno
        self._edad = edad

    def mostrar(self):
        return f"{self._nombre} {self._paterno} {self._materno} Edad: {self._edad}"


class Docente(Persona):
    def __init__(self, nombre, paterno, materno, edad, sueldo, reg_profesional):
        super().__init__(nombre, paterno, materno, edad)
        self.sueldo = sueldo
        self.reg_profesional = reg_profesional

    def mostrar(self):
        return super().mostrar() + f" Sueldo: {self.sueldo}, Reg: {self.reg_profesional}"


class Estudiante(Persona):
    def __init__(self, nombre, paterno, materno, edad, ru, matricula):
        super().__init__(nombre, paterno, materno, edad)
        self.ru = ru
        self.matricula = matricula

    def mostrar(self):
        return super().mostrar() + f"  RU: {self.ru}, Matrícula: {self.matricula}"

    def modificarEdad(self, nueva_edad):
        self._edad = nueva_edad

    def get_edad(self):
        return self._edad
    
e1 = Estudiante("Ana", "López", "Vega", 20, "20201234", "MAT123")
e2 = Estudiante("Carlos", "Reyes", "Mamani", 22, "20205678", "MAT456")
d1 = Docente("Luis", "Torres", "Rojas", 22, 5500, "R123")

print(e1.mostrar())
print(e2.mostrar())
print(d1.mostrar())

prom = (e1.get_edad() + e2.get_edad()) / 2
print("Promedio edad estudiantes:", prom)

e1.modificarEdad(25)
print("Edad modificada de Ana:", e1.get_edad())

if e1.get_edad() == d1._edad:
    print("Ana tiene la misma edad que el docente.")
elif e2.get_edad() == d1._edad:
    print("Manuel tiene la misma edad que el docente.")
else:
    print("Ningún estudiante tiene la misma edad que el docente.")
