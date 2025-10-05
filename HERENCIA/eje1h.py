class Persona:
    def __init__(self, nombre, apellido, id_persona):
        self.nombre = nombre
        self.apellido = apellido
        self.id_persona = id_persona

    def __str__(self):
        return f"{self.nombre} {self.apellido} id: {self.id_persona})"

class Cliente(Persona):
    def __init__(self, nombre, apellido, id_persona, nro_compra, id_cliente):
        super().__init__(nombre, apellido, id_persona)
        self.nro_compra = nro_compra
        self.id_cliente = id_cliente

    def __str__(self):
        return super().__str__() + f" Cliente id: {self.id_cliente}, Compras: {self.nro_compra}"


class Jefe(Persona):
    def __init__(self, nombre, apellido, id_persona, sucursal, tipo):
        super().__init__(nombre, apellido, id_persona)
        self.sucursal = sucursal
        self.tipo = tipo

    def __str__(self):
        return super().__str__() + f" Jefe de {self.sucursal}, Tipo: {self.tipo}"


cliente1 = Cliente("Laura", "Gonzales", "101", 5, "123")
jefe1 = Jefe("Marco", "Lopez", "J202", "Sucursal Central", "General")

print(cliente1)
print(jefe1)