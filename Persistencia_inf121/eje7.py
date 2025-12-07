import json

class Persona:
    def __init__(self, nombre="", apellidop="", apellidom="", ci=0):
        self.nombre = nombre
        self.apellidop = apellidop
        self.apellidom = apellidom
        self.ci = ci

    def convertir_dic(self):
        return {
            "nombre": self.nombre,
            "apellidop": self.apellidop,
            "apellidom": self.apellidom,
            "ci": self.ci
        }

    def cargar_desde_dic(self, d):
        self.nombre = d["nombre"]
        self.apellidop = d["apellidop"]
        self.apellidom = d["apellidom"]
        self.ci = d["ci"]

    def mostrar(self):
        print(f"{self.ci}  {self.nombre} {self.apellidop} {self.apellidom}")


class Niño(Persona):
    def __init__(self, nombre="", apellidop="", apellidom="", ci=0, edad=0, peso="", talla=""):
        super().__init__(nombre, apellidop, apellidom, ci)
        self.edad = edad
        self.peso = peso   
        self.talla = talla 

    def convertir_dic(self):
        d = super().convertir_dic()
        d.update({
            "edad": self.edad,
            "peso": self.peso,
            "talla": self.talla
        })
        return d

    def cargar_desde_dic(self, d):
        super().cargar_desde_dic(d)
        self.edad = d["edad"]
        self.peso = d["peso"]
        self.talla = d["talla"]

    def mostrar(self):
        print(f"[{self.ci}] {self.nombre} {self.apellidop} {self.apellidom} "
              f"edad:{self.edad} peso:{self.peso} talla:{self.talla}")

class ArchNiño:
    def __init__(self):
        self.niños = []

    def crear(self, niño):
        self.niños.append(niño)

    def cargar(self, ruta):
        with open(ruta, "r") as f:
            d = json.load(f)
            lista = []
            for x in d["niños"]:
                n = Niño()
                n.cargar_desde_dic(x)
                lista.append(n)
            self.niños = lista

    def guardar(self, ruta):
        lista = []
        try:
            for n in self.niños:
                diccionario = n.convertir_dic() 
                lista.append(diccionario)
            with open(ruta, "w") as f:
                json.dump({"niños": lista}, f)
        except Exception as e:
            print(f"Error al guardar el archivo: {e}")

    def listar(self):
        for n in self.niños:
            n.mostrar()

    def contar_peso_talla_corr(self):
        cont = 0
        for n in self.niños:
            try:
                if n.peso.isdigit() and n.talla.isdigit():
                    peso = int(n.peso)
                    talla = int(n.talla)
                    if peso == talla + n.edad:
                        cont += 1
            except ValueError:
                continue 
        return cont

    def mostrar_no_adecuados(self):
        for n in self.niños:
            try:
                if n.peso.isdigit() and n.talla.isdigit():
                    peso = int(n.peso)
                    talla = int(n.talla)
                    if peso != talla + n.edad:
                        n.mostrar()
            except ValueError:
                pass  

    def promedio_edad(self):
        if len(self.niños) == 0:
            return 0
        return sum(n.edad for n in self.niños) / len(self.niños)

    def buscar_ci(self, ci):
        for n in self.niños:
            if n.ci == ci:
                return n
        return None

    def mostrar_talla_alta(self):
        if len(self.niños) == 0:
            return
        talla_max = -1
        niño_max = None
        for n in self.niños:
            try:
                talla = int(n.talla)
                if talla > talla_max:
                    talla_max = talla
                    niño_max = n
            except ValueError:
                pass 

        if niño_max:
            niño_max.mostrar()


archivo = ArchNiño()

archivo.crear(Niño("Felipe", "Loza", "Lopez", 9876549, 8, "30", "120"))
archivo.crear(Niño("Luis", "Rojas", "Mamani", 9165625, 7, "28", "118"))
archivo.crear(Niño("Mia", "Torrez", "Arias", 9165624, 9, "40", "130"))

archivo.guardar("niños.json")

archivo.cargar("niños.json")
archivo.listar()

archivo.mostrar_no_adecuados()

print("\nPromedio de edades:", archivo.promedio_edad())

n = archivo.buscar_ci(9165625)
n.mostrar()

print("\nNiño con la talla más alta:")
archivo.mostrar_talla_alta()
