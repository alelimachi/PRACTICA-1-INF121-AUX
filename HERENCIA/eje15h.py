class Nadador:
    def __init__(self, estiloNatacion):
        self.estiloNatacion = estiloNatacion

    def nadar(self):
        print(f"Nadando estilo {self.estiloNatacion}")

class Ciclista:
    def __init__(self, tipoBici):
        self.tipoBici = tipoBici

    def pedalear(self):
        print(f"Pedaleando en bicicleta tipo {self.tipoBici}")

class Corredor:
    def __init__(self, distanciaPref):
        self.distanciaPref = distanciaPref

    def correr(self):
        print(f"Corriendo una distancia de {self.distanciaPref} km")

class Triatleta(Nadador, Ciclista, Corredor):
    def __init__(self, estiloNatacion, tipoBici, distanciaPref):
        Nadador.__init__(self, estiloNatacion)
        Ciclista.__init__(self, tipoBici)
        Corredor.__init__(self, distanciaPref)

tri = Triatleta("Libre", "Ruta", 5)

tri.nadar()
tri.pedalear()
tri.correr()
