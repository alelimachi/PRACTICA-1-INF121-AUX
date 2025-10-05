class Politico:
    def __init__(self, profesion, anios_exp):
        self.profesion = profesion
        self.anios_exp = anios_exp


class Partido:
    def __init__(self, nombre_partido, rol):
        self.nombre_partido = nombre_partido
        self.rol = rol


class Presidente(Politico, Partido):
    def __init__(self, nombre, apellido, profesion, anios_exp, nombre_partido, rol):
        Politico.__init__(self, profesion, anios_exp)
        Partido.__init__(self, nombre_partido, rol)
        self.nombre = nombre
        self.apellido = apellido

    def mostrar(self):
        return f"{self.nombre} {self.apellido} | Partido: {self.nombre_partido} | Profesión: {self.profesion}"
    
p1 = Presidente("Luis", "Arce", "Economista", 15, "MAS", "Presidente")
p2 = Presidente("Tuto", "Quiroga", "Economista", 8, "Libre", "Postulante")
p3 = Presidente("Eva", "Copa", "Socióloga", 8, "Jallalla", "Presidenta")

presidentes = [p1, p2, p3]
for pres in presidentes:
    print(pres.mostrar())

buscar_nombre = "Carlos"
for pres in presidentes:
    if pres.nombre == buscar_nombre:
        print(f"\nPresidente encontrado: {pres.nombre} {pres.apellido}")
        print("Partido:", pres.nombre_partido)
        print("Profesión:", pres.profesion)
