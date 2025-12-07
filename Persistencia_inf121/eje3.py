import json

class producto:
    def __init__(self, codigo, nombre, precio):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio

    def a_dict(self):
        return {
            "codigo": self.codigo,
            "nombre": self.nombre,
            "precio": self.precio
        }

    @staticmethod
    def desde_dict(d):
        return producto(d["codigo"], d["nombre"], d["precio"])

    def __str__(self):
        return f"producto(codigo={self.codigo}, nombre={self.nombre}, precio={self.precio})"


class archivoproducto:
    def __init__(self, noma):
        self.noma = noma
        self.creararchivo()

    def creararchivo(self):
        try:
            with open(self.noma, "r"):
                pass
        except FileNotFoundError:
            with open(self.noma, "w") as f:
                json.dump([], f)

    def cargarlista(self):
        with open(self.noma, "r") as f:
            datos = json.load(f)

        lista = []
        for d in datos:
            lista.append(producto.desde_dict(d))
        return lista

    def guardarlista(self, lista):
        datos = []
        for p in lista:
            datos.append(p.a_dict())

        with open(self.noma, "w") as f:
            json.dump(datos, f, indent=4)

    def guardarproducto(self, p):
        lista = self.cargarlista()
        lista.append(p)
        self.guardarlista(lista)

    def buscaproducto(self, c):
        lista = self.cargarlista()
        for p in lista:
            if p.codigo == c:
                return p
        return None

    def promedioprecios(self):
        lista = self.cargarlista()
        if len(lista) == 0:
            return 0

        suma = 0
        for p in lista:
            suma += p.precio

        return suma / len(lista)

    def productomascaro(self):
        lista = self.cargarlista()
        if len(lista) == 0:
            return None

        mayor = lista[0]
        for i in range(1, len(lista)):
            if lista[i].precio > mayor.precio:
                mayor = lista[i]

        return mayor


arch = archivoproducto("productos.json")

arch.guardarproducto(producto(1, "cuerda", 15.0))
arch.guardarproducto(producto(2, "caja", 120.0))
arch.guardarproducto(producto(3, "lana", 5.0))

print("buscar código 2:", arch.buscaproducto(2))
print("promedio:", arch.promedioprecios())
print("más caro:", arch.productomascaro())
