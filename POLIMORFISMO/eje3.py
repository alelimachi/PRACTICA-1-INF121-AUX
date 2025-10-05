class Matriz:
    def __init__(self, matriz=None):
        self.matriz = [[0] * 10 for _ in range(10)]
        if matriz is None:
            for i in range(10):
                self.matriz[i][i] = 1 
        else:
            for i in range(10):
                for j in range(10):
                    self.matriz[i][j] = matriz[i][j]

    def sumar(self, otra):
        resultado = Matriz()
        for i in range(10):
            for j in range(10):
                resultado.matriz[i][j] = self.matriz[i][j] + otra.matriz[i][j]
        return resultado

    def restar(self, otra):
        resultado = Matriz()
        for i in range(10):
            for j in range(10):
                resultado.matriz[i][j] = self.matriz[i][j] - otra.matriz[i][j]
        return resultado

    def igual(self, otra):
        for i in range(10):
            for j in range(10):
                if self.matriz[i][j] != otra.matriz[i][j]:
                    return False
        return True

    def mostrar(self):
        for fila in self.matriz:
            print(fila)

m1 = Matriz()
print("Matriz 1:")
m1.mostrar()

valores = [[i + j for j in range(10)] for i in range(10)]
m2 = Matriz(valores)
print("Matriz 2:")
m2.mostrar()

suma = m1.sumar(m2)
print("Suma de m1 + m2:")
suma.mostrar()

resta = m2.restar(m1)
print("Resta de m2 - m1:")
resta.mostrar()

print("¿m1 es igual a m2?", m1.igual(m2))


