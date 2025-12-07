import json

class Charango:
    def __init__(self, material, nrocuerdas, cuerdas):
        self.material = material
        self.nrocuerdas = nrocuerdas
        self.cuerdas = []

        for i in range(10):
            if i < len(cuerdas):
                self.cuerdas.append(cuerdas[i])
            else:
                self.cuerdas.append(False)

    def contar_false(self):
        con = 0
        for estado in self.cuerdas:
            if estado is False:
                con += 1
        return con

    def todas_true(self):
        for estado in self.cuerdas:
            if estado is False:
                return False
        return True

    def to_data(self):
        return {
            "material": self.material,
            "nrocuerdas": self.nrocuerdas,
            "cuerdas": self.cuerdas
        }

    @staticmethod
    def desde_dict(dic):
        return Charango(dic["material"], dic["nrocuerdas"], dic["cuerdas"])

    def __str__(self):
        return f"Charango(material={self.material}, nroCuerdas={self.nrocuerdas}, cuerdas={self.cuerdas})"


class ArchivoCharango:
    def __init__(self, nombre):
        self.nombre = nombre
        self.crear_archivo()

    def crear_archivo(self):
        try:
            with open(self.nombre, "r") as f:
                pass
        except FileNotFoundError:
            with open(self.nombre, "w") as f:
                json.dump([], f)

    def cargar_lista(self):
        with open(self.nombre, "r") as f:
            datos = json.load(f)

        lista = []
        for d in datos:
            lista.append(Charango.desde_dict(d))
        return lista

    def guardar_lista(self, lista):
        datos = []
        for c in lista:
            datos.append(c.to_data())  
        with open(self.nombre, "w") as f:
            json.dump(datos, f, indent=4)

    def guardar_charango(self, c):
        lista = self.cargar_lista()
        lista.append(c)
        self.guardar_lista(lista)

    def eliminar_con_false_8(self):
        lista = self.cargar_lista()
        nv_lista = []
        for c in lista:
            cant = c.contar_false()
            if cant <= 8:
                nv_lista.append(c)

        self.guardar_lista(nv_lista)

    def listar_material(self, mat):
        lista = self.cargar_lista()
        res = []
        for c in lista:
            if c.material.lower() == mat.lower():
                res.append(c)
        return res

    def buscar_10cuerdas(self):
        lista = self.cargar_lista()
        res = []
        for c in lista:
            if c.todas_true():
                res.append(c)
        return res

    def ordenar_material(self):
        lista = self.cargar_lista()
        for i in range(len(lista)):
            for j in range(i + 1, len(lista)):
                if lista[i].material.lower() > lista[j].material.lower():
                    lista[i], lista[j] = lista[j], lista[i]
        self.guardar_lista(lista)


arch = ArchivoCharango("Charango.json")

c1 = Charango("Roble", 10, [True]*10)
c2 = Charango("Nogal", 10, [True, False, False, False, False, False, False, False, False, False])
c3 = Charango("Cedro", 10, [True]*5 + [False]*5)

arch.guardar_charango(c1)
arch.guardar_charango(c2)
arch.guardar_charango(c3)

print("Listado Cedro:")
for x in arch.listar_material("cedro"):
    print(x)

print("\n10 cuerdas true:")
for x in arch.buscar_10cuerdas():
    print(x)
arch.ordenar_material()
