class Facultad:
    def __init__(self, nombre, ubicacion):
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.participantes = []  
    
    def agregar_participante(self, participante):
        self.participantes.append(participante)
    
    def __str__(self):
        return f"Facultad: {self.nombre}, Ubicación: {self.ubicacion}"

class Fraternidad:
    def __init__(self, nombre, encargado):
        self.nombre = nombre
        self.encargado = encargado
        self.miembros = []  
    
    def agregar_miembro(self, participante):
        self.miembros.append(participante)
    
    def __str__(self):
        return f"Fraternidad: {self.nombre}, Encargado: {self.encargado}"

class Participante:
    def __init__(self, nombre, edad, facultad, fraternidad):
        self.nombre = nombre
        self.edad = edad
        self.facultad = facultad
        self.fraternidad = fraternidad
    
    def __str__(self):
        return f"Participante: {self.nombre}, Edad: {self.edad}, Facultad: {self.facultad.nombre}, Fraternidad: {self.fraternidad.nombre}"

fac_ciencias = Facultad("Facultad de Ciencias", "Edificio 1")
fac_Odontologia = Facultad("Facultad de Odontologia", "Edificio 2")

frat_mineritos= Fraternidad("mineritos", "Carlos Lima")
frat_Capos = Fraternidad("Capos", "Ana Quispe")

p1 = Participante("Juan Condori", 22, fac_ciencias, frat_mineritos)
p2 = Participante("Manuel Limachi", 19, fac_Odontologia, frat_Capos)
p3 = Participante("Carlos Quispe", 23, fac_ciencias, frat_mineritos)
p4 = Participante("Sofía Mallea", 18, fac_Odontologia, frat_Capos)
p5 = Participante("Luis Rodríguez", 24, fac_Odontologia, frat_Capos)

participantes = [p1, p2, p3, p4, p5]

for p in participantes:
    print(p)

def most_enc():
    for fraternidad in [frat_mineritos, frat_Capos]:
        print(f"Encargado de {fraternidad.nombre}: {fraternidad.encargado}")
most_enc()
