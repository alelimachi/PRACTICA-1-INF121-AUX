import json

class Alimento:
    def __init__(self, nombre="", fechavenc="", cantidad=0):
        self.nombre = nombre
        self.fechavenc = fechavenc
        self.cantidad = cantidad

    def convertir_dic(self):
        try:
            return {
                "nombre": self.nombre,
                "fechavenc": self.fechavenc,
                "cantidad": self.cantidad
            }
        except AttributeError as e:
            print(f"Error al convertir: {e}")
            return None 

    def cargar_desde_dic(self, d):
        try:
            self.nombre = d["nombre"]
            self.fechavenc = d["fechavenc"]
            self.cantidad = d["cantidad"]
        except KeyError as e:
            print(f"Error al cargar : {e}")
            return None

    def mostrar(self):
        print(f"[{self.nombre} vence:{self.fechavenc} cant:{self.cantidad}]")
        
class ArchRefri:
    def __init__(self, nombrearchivo):
        self.nombre = nombrearchivo
        self.alimentos = []

    def diccionario(self):
        lista = []  
        for a in self.alimentos:
            try:
                diccionario_alimento = a.convertir_dic()
                if diccionario_alimento:
                    lista.append(diccionario_alimento)
            except Exception as e:
                print(f"Error al convertir el alimento: {e}")
        return {"alimentos": lista}

    def guardar(self):
        try:
            with open(self.nombre, "w") as f:
                json.dump(self.diccionario(), f)
        except IOError as e:
            print(f"Error al guardar el archivo: {e}")

    def cargar(self):
        try:
            with open(self.nombre, "r") as f:
                d = json.load(f)
            self.alimentos = []
            for al in d["alimentos"]:
                a = Alimento()
                a.cargar_desde_dic(al)
                self.alimentos.append(a)
        except (IOError, KeyError) as e:
            print(f"Error al cargar el archivo: {e}")

    def crear(self, alimento):
        self.alimentos.append(alimento)

    def modificar(self, nombrebuscado, nuevafecha, nuevacant):
        for a in self.alimentos:
            if a.nombre == nombrebuscado:
                a.fechavenc = nuevafecha
                a.cantidad = nuevacant
                return True
        return False

    def eliminar(self, nombrebuscado):
        nueva = []
        for a in self.alimentos:
            if a.nombre != nombrebuscado:
                nueva.append(a)
        self.alimentos = nueva

    def caducados_antes(self, fechax):
        for a in self.alimentos:
            if a.fechavenc < fechax:
                a.mostrar()

    def eliminar_cero(self):
        nueva = []
        for a in self.alimentos:
            if a.cantidad != 0:
                nueva.append(a)
        self.alimentos = nueva


    def vencidos(self, fechahoy):
        for a in self.alimentos:
            if a.fechavenc < fechahoy:
                a.mostrar()

    def mayor_cantidad(self):
        if len(self.alimentos) == 0:
            print("No hay alimentos")
            return
        mayor = self.alimentos[0]
        for a in self.alimentos:
            if a.cantidad > mayor.cantidad:
                mayor = a
        print("Alimento con más cantidad:")
        mayor.mostrar()

    def listar(self):
        for a in self.alimentos:
            a.mostrar()

refri = ArchRefri("refri.json")

refri.crear(Alimento("yogurt", "2025-01-10", 5))
refri.crear(Alimento("queso", "2024-12-01", 0))
refri.crear(Alimento("manzana", "2025-02-03", 12))
refri.crear(Alimento("leche", "2024-11-20", 3))

refri.guardar()

refri.cargar()
refri.listar()
refri.caducados_antes("2024-12-31")

print("\n Eliminando cantidad 0")
refri.eliminar_cero()
refri.listar()

print("\n Alimentos vencidos (2024-12-31)")
refri.vencidos("2024-12-31")

print("\n Alimento con más cantidad")
refri.mayor_cantidad()
