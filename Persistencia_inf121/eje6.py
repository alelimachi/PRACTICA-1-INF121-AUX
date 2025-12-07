import json

class Libro:
    def __init__(self, codlibro="", titulo="", precio=0):
        self.codlibro = codlibro
        self.titulo = titulo
        self.precio = precio

    def convertir_dic(self):
        return {
            "codlibro": self.codlibro,
            "titulo": self.titulo,
            "precio": self.precio
        }

    def from_dict(self, d):
        self.codlibro = d["codlibro"]
        self.titulo = d["titulo"]
        self.precio = d["precio"]

    def mostrar(self):
        print(f"[{self.codlibro}] {self.titulo}  bs.{self.precio}")


class Prestamo:
    def __init__(self, codcliente="", codlibro="", fecha="", cantidad=0):
        self.codcliente = codcliente
        self.codlibro = codlibro
        self.fecha = fecha
        self.cantidad = cantidad

    def convertir_dic(self):
        return {
            "codcliente": self.codcliente,
            "codlibro": self.codlibro,
            "fecha": self.fecha,
            "cantidad": self.cantidad
        }

    def from_dict(self, d):
        self.codcliente = d["codcliente"]
        self.codlibro = d["codlibro"]
        self.fecha = d["fecha"]
        self.cantidad = d["cantidad"]

    def mostrar(self):
        print(f"[cliente {self.codcliente}] libro {self.codlibro} → {self.cantidad} unidades ({self.fecha})")


class Cliente:
    def __init__(self, codcliente="", ci="", nombre="", apellido=""):
        self.codcliente = codcliente
        self.ci = ci
        self.nombre = nombre
        self.apellido = apellido

    def convertir_dic(self):
        return {
            "codcliente": self.codcliente,
            "ci": self.ci,
            "nombre": self.nombre,
            "apellido": self.apellido
        }

    def from_dict(self, d):
        self.codcliente = d["codcliente"]
        self.ci = d["ci"]
        self.nombre = d["nombre"]
        self.apellido = d["apellido"]

    def mostrar(self):
        print(f"[{self.codcliente}] {self.nombre} {self.apellido}  ci:{self.ci}")


class ArchLibro:
    def __init__(self, nombre):
        self.nombre = nombre
        self.libros = []

    def guardar(self):
        datos = {"libros": []}
        for l in self.libros:
            datos["libros"].append(l.convertir_dic())

        with open(self.nombre, "w") as f:
            json.dump(datos, f)

    def cargar(self):
        with open(self.nombre, "r") as f:
            data = json.load(f)

        self.libros = []
        for d in data["libros"]:
            l = Libro()
            l.from_dict(d)
            self.libros.append(l)

    def crear(self, libro):
        self.libros.append(libro)

    def listar(self):
        for l in self.libros:
            l.mostrar()


class ArchPrestamo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.prestamos = []

    def guardar(self):
        datos = {"prestamos": []}
        for p in self.prestamos:
            datos["prestamos"].append(p.convertir_dic())

        with open(self.nombre, "w") as f:
            json.dump(datos, f)

    def cargar(self):
        with open(self.nombre, "r") as f:
            data = json.load(f)

        self.prestamos = []
        for d in data["prestamos"]:
            p = Prestamo()
            p.from_dict(d)
            self.prestamos.append(p)

    def crear(self, p):
        self.prestamos.append(p)

    def listar(self):
        for p in self.prestamos:
            p.mostrar()


class ArchCliente:
    def __init__(self, nombre):
        self.nombre = nombre
        self.clientes = []

    def guardar(self):
        datos = {"clientes": []}
        for c in self.clientes:
            datos["clientes"].append(c.convertir_dic())

        with open(self.nombre, "w") as f:
            json.dump(datos, f)

    def cargar(self):
        with open(self.nombre, "r") as f:
            data = json.load(f)

        self.clientes = []
        for d in data["clientes"]:
            c = Cliente()
            c.from_dict(d)
            self.clientes.append(c)

    def crear(self, c):
        self.clientes.append(c)

    def listar(self):
        for c in self.clientes:
            c.mostrar()


def libros_entre_precios(archlibro, x, y):
    for l in archlibro.libros:
        if x <= l.precio <= y:
            l.mostrar()

def ingreso_libro(archprestamo, archlibro, codlibro):
    precio = 0
    for l in archlibro.libros:
        if l.codlibro == codlibro:
            precio = l.precio
            break

    total = 0
    for p in archprestamo.prestamos:
        if p.codlibro == codlibro:
            total += p.cantidad * precio

    print(f"Ingreso total del libro {codlibro}: bs.{total}")


def libros_no_vendidos(archlibro, archprestamo):
    prestados = set()

    for p in archprestamo.prestamos:
        prestados.add(p.codlibro)
    for l in archlibro.libros:
        encontrado = False
        for codigo in prestados:  
            if l.codlibro == codigo:
                encontrado = True
        if encontrado == False:   
            print("Nunca prestado:", end=" ")
            l.mostrar()

def clientes_de_libro(archcliente, archprestamo, codlibro):
    clientes = set()

    for p in archprestamo.prestamos:
        if p.codlibro == codlibro:
            clientes.add(p.codcliente)

    for c in archcliente.clientes:
        pertenece = c.codcliente in clientes

        if pertenece:
            c.mostrar()

def libro_mas_prestado(archprestamo, archlibro):
    conteo = {}
    for p in archprestamo.prestamos:
        conteo[p.codlibro] = conteo.get(p.codlibro, 0) + p.cantidad

    if not conteo:
        print("No hay prestamos")
        return

    cod = max(conteo, key=conteo.get)

    for l in archlibro.libros:
        if l.codlibro == cod:
            print("Libro más prestado:")
            l.mostrar()


def cliente_mas_prestamos(archcliente, archprestamo):
    conteo = {}
    for p in archprestamo.prestamos:
        conteo[p.codcliente] = conteo.get(p.codcliente, 0) + p.cantidad

    cod = max(conteo, key=conteo.get)

    for c in archcliente.clientes:
        if c.codcliente == cod:
            print("Cliente con más préstamos:")
            c.mostrar()


archl = ArchLibro("libros.json")
archc = ArchCliente("clientes.json")
archp = ArchPrestamo("prestamos.json")

archl.crear(Libro("12435212", "Algebra I", 120))
archl.crear(Libro("12236524", "Cálculo I", 90))
archl.crear(Libro("35463521", "Álgebra lineal", 150))

archc.crear(Cliente("4231", "1012832", "Juan", "Quispe"))
archc.crear(Cliente("2121", "9165623", "Ana", "Peres"))
archc.crear(Cliente("2123", "7898632", "Manuel", "Limachi"))

archp.crear(Prestamo("1234", "l1", "2024-09-01", 2))
archp.crear(Prestamo("2343", "l1", "2024-09-03", 1))
archp.crear(Prestamo("1236", "l2", "2024-09-10", 1))
archp.crear(Prestamo("9859", "l2", "2024-09-11", 3))

archl.guardar()
archc.guardar()
archp.guardar()

archl.cargar()
archc.cargar()
archp.cargar()

libros_entre_precios(archl, 100, 150)
ingreso_libro(archp, archl, "l1")
libros_no_vendidos(archl, archp)
clientes_de_libro(archc, archp, "l2")
libro_mas_prestado(archp, archl)
cliente_mas_prestamos(archc, archp)

