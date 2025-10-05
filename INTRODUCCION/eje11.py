class Cliente:
    def __init__(self, nombre, mesa):
        self.nombre = nombre 
        self.mesa = mesa
        print(f"Cliente {self.nombre} creado.")

    def getNombre(self):
        return self.nombre

    def set_productos(self, nombre):
        self.nombre = nombre

    def getMesa(self):
        return self.mesa

    def setMesa(self, mesa):
        self.mesa = mesa

    def __del__(self):
        print(f"Cliente {self.nombre}eliminado.")
        
class Pedido:
    def __init__(self, idPedido, estado):
        self.idPedido = idPedido
        self.estado = estado
        print(f"Pedido {self.idPedido} creado con estado {self.estado}.")

    def getIDPedido(self):
        return self.idPedido

    def setIDPedido(self, idPedido):
        self.idPedido = idPedido

    def getEstado(self):
        return self.estado

    def setEstado(self, estado):
        self.estado = estado

    def __del__(self):
        print(f"Pedido {self.idPedido} eliminado.")
    
Cliente1 = Cliente("Ana", 5)
Cliente2 = Cliente("Juan", 2)
pedido1 = Pedido(101, "Registrado")
pedido2 = Pedido(104, "Preparado")

pedido1.setEstado("Entregado")
print(f"Pedido 101 nuevo estado: {pedido1.getEstado()}")

