class Producto:
    def __init__(self, codigo, nombre):
        self.codigo = codigo
        self.nombre = nombre

    def __str__(self):
        return f"Producto[codigo={self.codigo}, nombre={self.nombre}]"

class Medicamento(Producto):
    def __init__(self, codigo, nombre, tipo, precio):
        super().__init__(codigo, nombre)
        self.tipo = tipo
        self.precio = precio
        self.registro = None

    def agregarreg(self, fecha_reg, cantidad):
        self.registro = Registro(fecha_reg, cantidad)

    def __str__(self):
        info = f"Medicamento[{self.nombre}, tipo={self.tipo}, precio={self.precio}]"
        if self.registro:
            info += f"\n  {self.registro}"
        return info


class Registro:
    def __init__(self, fecha_reg, cantidad):
        self.fecha_reg = fecha_reg  
        self.cantidad = cantidad

    def __str__(self):
        return f"Registro[fecha={self.fecha_reg}, cantidad={self.cantidad}]"


class Almacen:
    def __init__(self, ubicacion, capacidad):
        self.ubicacion = ubicacion
        self.capacidad = capacidad
        self.productos = []

    def agregprod(self, producto):
        self.productos.append(producto)

    def __str__(self):
        return f"Almacen[{self.ubicacion}, capacidad={self.capacidad}, productos={len(self.productos)}]"

med1 = Medicamento("M001", "Paracetamol", "Resfrio", 15.5)
med1.agregarreg("2025-11-05", 100)

almacen = Almacen("Zona Sur", 500)
almacen.agregprod(med1)

print(almacen)
for prod in almacen.productos:
    print(prod)

    
        
