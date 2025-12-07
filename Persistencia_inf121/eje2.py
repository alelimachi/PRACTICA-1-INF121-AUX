import json

class trabajador:
    def __init__(self, nombre, carnet, salario):
        self.nombre = nombre
        self.carnet = carnet
        self.salario = salario

    def a_dict(self):
        return {
            "nombre": self.nombre,
            "carnet": self.carnet,
            "salario": self.salario
        }

    @staticmethod
    def desde_dict(d):
        return trabajador(d["nombre"], d["carnet"], d["salario"])

    def __str__(self):
        return f"trabajador(nombre={self.nombre}, carnet={self.carnet}, salario={self.salario})"

class archivotrabajador:
    def __init__(self, nombrearch):
        self.nombrearch = nombrearch
        self.creararchivo()

    def creararchivo(self):
        try:
            with open(self.nombrearch, "r"):
                pass
        except FileNotFoundError:
            with open(self.nombrearch, "w") as f:
                json.dump([], f)

    def cargarlista(self):
        with open(self.nombrearch, "r") as f:
            datos = json.load(f)

        lista = []
        for d in datos:
            lista.append(trabajador.desde_dict(d))

        return lista

    def guardarlista(self, lista):
        datos = []
        for t in lista:
            datos.append(t.a_dict())

        with open(self.nombrearch, "w") as f:
            json.dump(datos, f, indent=4)

    def guardartrabajador(self, t):
        lista = self.cargarlista()
        lista.append(t)
        self.guardarlista(lista)

    def aumentarsalario(self, aumento, carnet):
        lista = self.cargarlista()

        for t in lista:
            if t.carnet == carnet:
                t.salario += aumento

        self.guardarlista(lista)

    def buscarmayor(self):
        lista = self.cargarlista()
        if len(lista) == 0:
            return None

        mayor = lista[0]
        for i in range(1, len(lista)):
            if lista[i].salario > mayor.salario:
                mayor = lista[i]

        return mayor

    def ordenar(self):
        lista = self.cargarlista()
        n = len(lista)

        for i in range(n):
            for j in range(i + 1, n):
                if lista[i].salario > lista[j].salario:
                    lista[i], lista[j] = lista[j], lista[i]

        self.guardarlista(lista)

arch = archivotrabajador("trabajadores.json")

arch.guardartrabajador(trabajador("juan", 9156253, 2500))
arch.guardartrabajador(trabajador("maria", 10929212, 3100))
arch.guardartrabajador(trabajador("pedro", 9165627, 2800))

arch.aumentarsalario(300, 102)

print(arch.buscarmayor())

arch.ordenar()



