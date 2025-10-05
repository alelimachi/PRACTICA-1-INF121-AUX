class Persona:
    def __init__(self, nombre, paterno, materno, edad, ci):
        self.nombre = nombre
        self.paterno = paterno
        self.materno = materno
        self.edad = edad
        self.ci = ci

    def mostDat(self):
        print(f"{self.nombre} {self.paterno} {self.materno}, Edad: {self.edad}, CI: {self.ci}")

    def mayedad(self):
        return self.edad >= 18

    def modedad(self, nuevo):
        self.edad = nuevo
        print(f"La edad de {self.nombre} fue modificado a {self.edad}")

    def mismoAp(self, otra_pers):
        return self.paterno == otra_pers.paterno


p1 = Persona("Manuel", "Limachi", "Quispe", 23, "9165625")
p2 = Persona("Juan", "Lima", "Perez", 10, "9784743")

p1.mostDat()
p2.mostDat()
print("¿p1 es mayor de edad?", p1.mayedad())
print("¿p2 es mayor de edad?", p2.mayedad())
print("¿Tiene el mismo apellido paterno?", p1.mismoAp(p2))

