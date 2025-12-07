import json

class Animal:
    def __init__(self, especie="", nombre="", cantidad=0):
        self.especie = especie
        self.nombre = nombre
        self.cantidad = cantidad

    def convertir_dic(self):
        return {
            "especie": self.especie,
            "nombre": self.nombre,
            "cantidad": self.cantidad
        }

    def cargar_desde_dic(self, d):
        self.especie = d["especie"]
        self.nombre = d["nombre"]
        self.cantidad = d["cantidad"]

    def mostrar(self):
        print(f"[{self.especie} {self.nombre} cant:{self.cantidad}]")

class Zoologico:
    def __init__(self, id=0, nombre=""):
        self.id = id
        self.nombre = nombre
        self.animales = []

    def convertir_dic(self):
        lista_animales = []
        for a in self.animales:
            lista_animales.append(a.convertir_dic())
        return {
            "id": self.id,
            "nombre": self.nombre,
            "animales": lista_animales
        }

    def cargar_desde_dic(self, d):
        self.id = d["id"]
        self.nombre = d["nombre"]
        self.animales = []
        for x in d["animales"]:
            a = Animal()
            a.cargar_desde_dic(x)
            self.animales.append(a)

    def mostrar(self):
        print(f"Zoo [{self.id} {self.nombre}]")
        for a in self.animales:
            a.mostrar()

class ArchZoo:
    def __init__(self, nombrearchivo):
        self.nombre = nombrearchivo
        self.zoos = []

    def dic(self):
        zoos_list = []
        for z in self.zoos:
            zoos_list.append(z.convertir_dic())
        return {"zoos": zoos_list}

    def guardar(self):
        try:
            with open(self.nombre, "w") as f:
                json.dump(self.dic(), f)
        except IOError as e:
            print(f"Error al guardar el archivo: {e}")

    def cargar(self):
        try:
            with open(self.nombre, "r") as f:
                d = json.load(f)
            self.zoos = []
            for z in d["zoos"]:
                zz = Zoologico()
                zz.cargar_desde_dic(z)
                self.zoos.append(zz)
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error al cargar el archivo: {e}")

    def crear(self, zoo):
        self.zoos.append(zoo)

    def modificar(self, idbuscar, nuevonombre):
        for z in self.zoos:
            if z.id == idbuscar:
                z.nombre = nuevonombre
                return True
        return False

    def eliminar(self, ideliminar):
        nueva = []
        for z in self.zoos:
            if z.id != ideliminar:
                nueva.append(z)
        self.zoos = nueva

    def mayor_variedad(self):
        if not self.zoos:
            print("No hay zoológicos.")
            return
        mayor = self.zoos[0]
        for z in self.zoos:
            if len(z.animales) > len(mayor.animales):
                mayor = z
        print("Zoo con mayor variedad:")
        mayor.mostrar()

    def eliminar_vacios(self):
        nueva = []
        for z in self.zoos:
            if len(z.animales) != 0:
                nueva.append(z)
        self.zoos = nueva

    def animales_especie(self, esp):
        for z in self.zoos:
            for a in z.animales:
                if a.especie == esp:
                    print(f"Zoo {z.nombre}:")
                    a.mostrar()

    def mover(self, idx, idy):
        zx = None
        zy = None
        for z in self.zoos:
            if z.id == idx:
                zx = z
            if z.id == idy:
                zy = z
        if zx and zy:
            zy.animales.extend(zx.animales)
            zx.animales = []
        else:
            print("No se pudo realizar el movimiento.")

arch = ArchZoo("zoo.json")

z1 = Zoologico(1, "La Paz")
z1.animales.append(Animal("Felino", "Tigre", 2))
z1.animales.append(Animal("Ave", "Aguila", 5))

z2 = Zoologico(2, "Santa Cruz")
z2.animales.append(Animal("Reptil", "Iguana", 3))

z3 = Zoologico(3, "Cochabamba")
arch.crear(z1)
arch.crear(z2)
arch.crear(z3)
arch.guardar()
arch.cargar()

arch.mayor_variedad()
arch.eliminar_vacios()
arch.guardar()
arch.cargar()
arch.animales_especie("Felino")
arch.mover(2, 1)
arch.guardar()
