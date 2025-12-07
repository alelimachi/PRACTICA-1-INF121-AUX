import json

class Medicamento:
    def __init__(self, id=0, nom="", tipo="", precio=0):
        self.id = id
        self.nom = nom
        self.tipo = tipo
        self.precio = precio

    def convertir_diccionario(self):
        return {
            "id": self.id,
            "nom": self.nom,
            "tipo": self.tipo,
            "precio": self.precio
        }

    def cargar_desde_dic(self, d):
        try:
            self.id = d["id"]
            self.nom = d["nom"]
            self.tipo = d["tipo"]
            self.precio = d["precio"]
        except KeyError as e:
            print(f"Error al cargar medicamento: {e}")
            raise

    def mostrar(self):
        print(f"[{self.id}] {self.nom} ({self.tipo}) Bs.{self.precio}")

class Farmacia:
    def __init__(self, nombre="", sucursal=0, direccion=""):
        self.nombre = nombre
        self.sucursal = sucursal
        self.direccion = direccion
        self.medicamentos = []

    def addMed(self, m):
        self.medicamentos.append(m)

    def mostrar(self):
        print(f"FARMACIA {self.nombre} SUC:{self.sucursal} ")
        print(f"Dirección: {self.direccion}")
        for m in self.medicamentos:
            m.mostrar()

    def convertir_diccionario(self):
        lista = []
        for m in self.medicamentos:
            lista.append(m.convertir_diccionario())
        return {
            "nombre": self.nombre,
            "sucursal": self.sucursal,
            "direccion": self.direccion,
            "medicamentos": lista
        }

    def cargar_desde_dic(self, d):
        try:
            self.nombre = d["nombre"]
            self.sucursal = d["sucursal"]
            self.direccion = d["direccion"]
            meds = []
            for m in d["medicamentos"]:
                me = Medicamento()
                me.cargar_desde_dic(m)
                meds.append(me)
            self.medicamentos = meds
        except KeyError as e:
            print(f"Error al cargar: {e}")
            raise
class ArchFarmacia:
    def __init__(self):
        self.farmacias = []

    def addFarmacia(self, f):
        self.farmacias.append(f)

    def mostrar(self):
        for f in self.farmacias:
            f.mostrar()

    def diccionario(self):
        arr = []
        for f in self.farmacias:
            arr.append(f.convertir_diccionario())
        return {"farmacias": arr}

    def cargar_desde_dic(self, d):
        lista = []
        try:
            for f in d["farmacias"]:
                fa = Farmacia()
                fa.cargar_desde_dic(f)
                lista.append(fa)
            self.farmacias = lista
        except KeyError as e:
            print(f"Error al cargar: {e}")
            raise

    def guardar(self, ruta):
        try:
            with open(ruta, "w") as f:
                json.dump(self.diccionario(), f, indent=4)
        except IOError as e:
            print(f"Error al guardar el archivo: {e}")
            raise

    def cargar(self, ruta):
        try:
            with open(ruta, "r") as f:
                d = json.load(f)
                self.cargar_desde_dic(d)
        except FileNotFoundError:
            print(f"El archivo {ruta} no fue encontrado.")
            raise
        except json.JSONDecodeError:
            print(f"Error al leer el archivo JSON.")
            raise
        except Exception as e:
            print(f"Error al cargar el archivo: {e}")
            raise
        
    def mostrarTosSucursal(self, suc):
        try:
            print(f"Medicamentos para la TOZ {suc}")
            for f in self.farmacias:
                if f.sucursal == suc:
                    for m in f.medicamentos:
                        if m.tipo == "tos":
                            m.mostrar()
        except Exception as e:
            print(f"Error al mostrar los medicamentos: {e}")
            raise

    def buscarTapsin(self):
        try:
            for f in self.farmacias:
                for m in f.medicamentos:
                    if m.nom.lower() == "tapsin":
                        print("Sucursal:", f.sucursal, " Direccion:", f.direccion)
        except Exception as e:
            print(f"Error al buscar Tapsin: {e}")
            raise

    def buscarPorTipo(self, tipo):
        try:
            print(f"Medicamentos de tipo {tipo}")
            for f in self.farmacias:
                for m in f.medicamentos:
                    if m.tipo == tipo:
                        print(m.nom, " ", f.nombre)
        except Exception as e:
            print(f"Error al buscar medicamentos por tipo: {e}")
            raise

    def ordenarDireccion(self):
        try:
            for i in range(len(self.farmacias) - 1):
                for j in range(i + 1, len(self.farmacias)):
                    if self.farmacias[i].direccion > self.farmacias[j].direccion:
                        self.farmacias[i], self.farmacias[j] = self.farmacias[j], self.farmacias[i]
        except Exception as e:
            print(f"Error al ordenar las farmacias: {e}")
            raise

    def moverTipo(self, tipo, sucA, sucB):
        try:
            mover = []
            for f in self.farmacias:
                if f.sucursal == sucA:
                    nuevos = []
                    for m in f.medicamentos:
                        if m.tipo == tipo:
                            mover.append(m)
                        else:
                            nuevos.append(m)
                    f.medicamentos = nuevos

            for f in self.farmacias:
                if f.sucursal == sucB:
                    f.medicamentos.extend(mover)
        except Exception as e:
            print(f"Error al mover medicamentos: {e}")
            raise

fa1 = Farmacia(nombre="FarmaciaBolivia", sucursal=1, direccion="av. Arce ")
fa1.addMed(Medicamento(id=5654, nom="tapsin", tipo="tos", precio=25))
fa1.addMed(Medicamento(id=2878, nom="jarabex", tipo="tos", precio=18))
fa1.addMed(Medicamento(id=3876, nom="antidol", tipo="dolor", precio=12.5))

fa2 = Farmacia(nombre="farmaciaChavez", sucursal=2, direccion="Av Buenos Aires calle 6")
fa2.addMed(Medicamento(id=4989, nom="aspirina", tipo="dolor", precio=9))
fa2.addMed(Medicamento(id=5675, nom="tapsin", tipo="tos", precio=24))
fa2.addMed(Medicamento(id=6123, nom="respira", tipo="tos", precio=20))

fa3 = Farmacia(nombre="Farmacorp", sucursal=3, direccion="av. 6 de Marzo calle 3")
fa3.addMed(Medicamento(id=7786, nom="loratadina", tipo="alergia", precio=15))
fa3.addMed(Medicamento(id=8876, nom="jarabex", tipo="tos", precio=17))

arch_farm = ArchFarmacia()
arch_farm.addFarmacia(fa1)
arch_farm.addFarmacia(fa2)
arch_farm.addFarmacia(fa3)

archivo_farm = "farmacias.json"
arch_farm.guardar(archivo_farm)
print(f"guardadas {len(arch_farm.farmacias)} farmacias en ‘{archivo_farm}’.")

arch_farm_cargado = ArchFarmacia()
arch_farm_cargado.cargar(archivo_farm)
print("\nlistado de farmacias cargadas:")
arch_farm_cargado.mostrar()

sucursal_consulta = 1
print(f"\nmedicamentos para la tos en sucursal {sucursal_consulta}:")
arch_farm_cargado.mostrarTosSucursal(sucursal_consulta)

arch_farm_cargado.buscarTapsin()

tipo_buscar = "tos"
print(f"\n medicamentos por tipo ‘{tipo_buscar}’:")
arch_farm_cargado.buscarPorTipo(tipo_buscar)
arch_farm_cargado.ordenarDireccion()
arch_farm_cargado.guardar(archivo_farm)
arch_farm_cargado.mostrar()
suca = 1
sucb = 3

print(f"\n moviendo medicamentos tipo ‘{tipo_buscar}’ de sucursal {suca} a sucursal {sucb} …")
arch_farm_cargado.moverTipo(tipo_buscar, suca, sucb)

arch_farm_cargado.guardar(archivo_farm)
arch_farm_cargado.mostrar()


