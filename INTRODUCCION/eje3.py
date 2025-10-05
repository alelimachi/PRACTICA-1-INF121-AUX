class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def vender(self, cantidad):
        if cantidad <= self.stock:
            self.stock -= cantidad
            print(f"se vendieron{cantidad} {self.nombre}. Stock restante: {self.stock}")
        else:
            print("No hay suficiente Stock")
            
    def reabastecer(self, cantidad):
        self.stock += cantidad
        print(f"Se reabastecieron {cantidad} {self.nombre}. Stock Total: {self.stock}")


p1 = Producto("Laptop",4500,10)
p1.vender(3)
p1.reabastecer(5)
