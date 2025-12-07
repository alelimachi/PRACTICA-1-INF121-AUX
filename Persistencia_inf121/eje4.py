import json

class estudiante:
    def __init__(self, ru=0, nombre="", paterno="", materno="", edad=0):
        self.ru = ru
        self.nombre = nombre
        self.paterno = paterno
        self.materno = materno
        self.edad = edad

    def convertir_diccionario(self):
        return {
            "ru": self.ru,
            "nombre": self.nombre,
            "paterno": self.paterno,
            "materno": self.materno,
            "edad": self.edad
        }

    def cargar_desde_dic(self, datos):
        try:
            self.ru = datos["ru"]
            self.nombre = datos["nombre"]
            self.paterno = datos["paterno"]
            self.materno = datos["materno"]
            self.edad = datos["edad"]
        except KeyError as e:
            print(f"Error: clave faltante {e}")
            raise

    def mostrar(self):
        print(f"(ru:{self.ru}) {self.nombre} {self.paterno} {self.materno} – edad:{self.edad}")


class nota:
    def __init__(self, materia="", notafinal=0, estudiante_obj=None):
        self.materia = materia
        self.notafinal = notafinal
        self.estudiante = estudiante_obj if estudiante_obj else estudiante()

    def convertir_diccionario(self):
        return {
            "materia": self.materia,
            "notafinal": self.notafinal,
            "estudiante": self.estudiante.convertir_diccionario()
        }

    def cargar_desde_dic(self, d):
        try:
            self.materia = d["materia"]
            self.notafinal = d["notafinal"]
            est = estudiante()
            est.cargar_desde_dic(d["estudiante"])
            self.estudiante = est
        except KeyError as e:
            print(f"Error al cargar la nota: clave faltante {e}")
            raise

    def mostrar(self):
        print(f"[{self.materia}] nota:{self.notafinal}")
        self.estudiante.mostrar()


class archinota:
    def __init__(self):
        self.notas = []

    def addnota(self, n):
        self.notas.append(n)

    def mostrar(self):
        for n in self.notas:
            n.mostrar()

    def diccionario(self):
        return {"notas": [n.convertir_diccionario() for n in self.notas]}

    def cargar_desde_dic(self, datos):
        try:
            self.notas = []
            for n in datos["notas"]:
                no = nota()
                no.cargar_desde_dic(n)
                self.notas.append(no)
        except KeyError as e:
            print(f"Error: clave faltante {e}")
            raise
        except Exception as e:
            print(f"Error al cargar datos: {e}")
            raise

    def guardar(self, ruta):
        try:
            with open(ruta, "w") as f:
                json.dump(self.diccionario(), f, indent=4)
        except IOError as e:
            print(f"Error: {e}")
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
            print(f"Error al leer el archivo json")
            raise
        except Exception as e:
            print(f"Error al cargar el archivo: {e}")
            raise

    def promedio(self):
        try:
            if len(self.notas) == 0:
                return 0
            suma_total = 0
            for n in self.notas:
                suma_total += n.notafinal
            cantidad_notas = len(self.notas)
            return suma_total / cantidad_notas
        except Exception as e:
            print(f"Error al calcular el promedio: {e}")
            raise

    def mejores(self):
        try:
            if len(self.notas) > 0:
                max_nota = self.notas[0].notafinal
                for n in self.notas:
                    if n.notafinal > max_nota:
                        max_nota = n.notafinal

                for n in self.notas:
                    if n.notafinal == max_nota:
                        n.mostrar()
        except Exception as e:
            print(f"Error al obtener las mejores notas: {e}")
            raise
    def eliminarmateria(self, prefijo):
        try:
            nvnotas = []
            for n in self.notas:  
                if n.materia[:len(prefijo)] == prefijo:  
                    continue  
                nvnotas.append(n)  
            self.notas = nvnotas
            print(f"Materias que comienzan con ‘{prefijo}’ eliminadas.")
        except Exception as e:
            print(f"Error al eliminar la materia: {e}")
            raise

arch_notas = archinota()

e1 = estudiante(ru=178765, nombre="Ana", paterno="Perez", materno="Lopez", edad=20)
n1 = nota(materia="INF-111", notafinal=18.5, estudiante_obj=e1)
arch_notas.addnota(n1)

e2 = estudiante(ru=1886123, nombre="Luis", paterno="Quispe", materno="Lima", edad=21)
n2 = nota(materia="INF-112", notafinal=19.0, estudiante_obj=e2)
arch_notas.addnota(n2)

e3 = estudiante(ru=1834245, nombre="Miguel", paterno="Rojas", materno="Soto", edad=19)
n3 = nota(materia="INF-131", notafinal=19.0, estudiante_obj=e3)
arch_notas.addnota(n3)

archivo_notas = "notas.json"
try:
    arch_notas.guardar(archivo_notas)
    print(f"guardadas {len(arch_notas.notas)} notas en ‘{archivo_notas}’.")
except Exception as e:
    print(f"No se pudieron guardar las notas: {e}")

arch_notas_cargado = archinota()
try:
    arch_notas_cargado.cargar(archivo_notas)
except Exception as e:
    print(f"No se pudieron cargar las notas: {e}")
    
arch_notas_cargado.mostrar()

try:
    prom = arch_notas_cargado.promedio()
    print(f"\npromedio de notas: {prom:.2f}")
except Exception as e:
    print(f"No se pudo calcular el promedio: {e}")

print("\nestudiantes con la mejor nota:")
try:
    arch_notas_cargado.mejores()
except Exception as e:
    print(f"No se pudieron obtener las mejores notas: {e}")


print("\neliminando materias que comienzan con ‘INF’")
try:
    arch_notas_cargado.eliminarmateria("INF")
except Exception as e:
    print(f"No se pudieron eliminar las materias: {e}")


print("estado después de eliminar:")
arch_notas_cargado.mostrar()
try:
    arch_notas_cargado.guardar(archivo_notas)
    print(f"cambios guardados en ‘{archivo_notas}’\n")
except Exception as e:
    print(f"No se pudieron guardar los cambios: {e}")