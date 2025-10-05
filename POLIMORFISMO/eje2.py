class Videojuego:
    def __init__(self, nombre, plataforma, jugadores=1):
        self.nombre = nombre
        self.plataforma = plataforma
        self.jugadores = jugadores

    def agregjugador(self):
        self.jugadores += 1

    def agregarjugad(self, cantidad):
        self.jugadores += cantidad

    def mostDat(self):
        print(f"Nombre: {self.nombre}, Plataforma: {self.plataforma} Jugadores: {self.jugadores}")

juego1 = Videojuego("FIFA", "XbOX", 2)
juego2 = Videojuego("TEKKEN", "PLAY STATION")

juego1.agregjugador()
juego2.agregarjugad(3)

juego1.mostDat()
juego2.mostDat()
