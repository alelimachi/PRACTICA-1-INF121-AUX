class Ropa:
    def __init__(self, tipo, material):
        self.tipo = tipo
        self.material= material

    def __str__(self):
        return "Ropa(tipo= " +self.tipo + ", material= " +self.material + ")"

class Ropero:
    def __init__(self, material, capacidad=20):
        self.material=material
        self.capacidad=capacidad
        self.prendas = []

    def agregarprenda(self, tipo, material):
        if len(self.prendas)>= self.capacidad:
            print("Ropero lleno: lo siento")
            return False
        nv = Ropa(tipo, material)
        self.prendas.append(nv)
        return True
    
    def agregarvarias(self, listastup):
        agreg = 0
        for tupla in listastup:
            tipo = tupla[0]
            mat = tupla[1]
            exito = self.agregarprenda(tipo, mat)
            if exito == True:
                agreg = agreg + 1
            else:
                break
        return agreg
    
    def mostrarprendas(self):
        print("Ropero (material: )", self.material, ",", len(self.prendas), "/", self.capacidad, ")")
        if len(self.prendas) == 0:
            print("No hay prendas ") 
            return
        i = 1
        for p in self.prendas:
            print("  ", i, ". tipo:", p.tipo, "- material: ", p.material)
            i = i + 1
            
    def eliminarpor_mat(self, material):
        ant = len(self.prendas)
        nuevas = []
        for p in self.prendas:
            if p.material != material:
                nuevas.append(p)
        self.prendas = nuevas
        elim = ant - len(self.prendas)
        print("Eliminadas: ", elim, "Prendas de material " + material + ".")
        return elim
    
    def elimnarpor_tip(self, tipo):
        ant = len(self.prendas)
        nuevas = []
        for p in self.prendas:
            if p.tipo != tipo:
                nuevas.append(p)
        self.prendas = nuevas
        elim = ant - len(self.prendas)
        print("Eliminadas: ", elim, "Prendas de material " + tipo + ".")
        return elim
    
    def mostrarmat(self, material):
        print("Prendas de material  "+material + " :")
        encontrado = []
        for p in self.prendas:
            if p.material == material:
                encontrado.append(p)
        if len(encontrado) == 0:
            print(" Ninguna.")
        else:
            for prenda in encontrado:
                print(" -", prenda.tipo, "(", prenda.material, ")")

    def mostratipo(self, tipo):
        print("Prendas de material  "+tipo+ " :")
        encontrado = []
        for p in self.prendas:
            if p.tipo == tipo:
                encontrado.append(p)
        if len(encontrado) == 0:
            print(" Ninguna.")
        else:
            for prenda in encontrado:
                print(" -", prenda.tipo, "(", prenda.material, ")")



miropero = Ropero(material="Madera", capacidad=20)

prendasagregar = [
    ("camisa", "algodón"),
    ("pantalon", "jean"),
    ("abrigo", "lana"),
    ("camisa", "seda"),
    ("short", "algodón"),
    ("vestido", "seda"),
    ("pantalon", "poliéster"),
    ("camisa", "algodón")
]

print("Agregando prendas")
agregadas = miropero.agregarvarias(prendasagregar)
print("Se agregaron", agregadas, "prendas.\n")

miropero.mostrarprendas()
print()

miropero.mostrarmat("algodón")
miropero.mostratipo("pantalon")
print()

miropero.eliminarpor_mat("algodón")
miropero.mostrarprendas()
print()

miropero.elimnarpor_tip("pantalon")
miropero.mostrarprendas()
print()

miropero.mostrarmat("seda")
miropero.mostratipo("camisa")

