class MP4:
    def __init__(self, marca, capacidad_gb):
        self.marca = marca
        self.capacidad = capacidad_gb * 1024 * 1024  # GB a KB
        self.canciones = []
        self.videos = []

    def espacio_ocupado(self):
        total = 0
        for c in self.canciones:
            total += c["peso"]
        for v in self.videos:
            total += v["peso"] * 1024
        return total
    
    def espacio_disponible(self):
        return self.capacidad - self.espacio_ocupado()

    def borrar_cancion(self, nombre, artista, peso):
        nueva_lista = []
        for c in self.canciones:
            if c["nombre"] == nombre and c["artista"] == artista and c["peso"] == peso:
                pass  
            else:
                nueva_lista.append(c)
        self.canciones = nueva_lista

    def __add__(self, cancion):
        repetida = False
        for c in self.canciones:
            if c["nombre"] == cancion["nombre"] and c["artista"] == cancion["artista"]:
                repetida = True
        if self.espacio_disponible() >= cancion["peso"]:
            if repetida == False:
                self.canciones.append(cancion)
        return self

    def __sub__(self, video):
        repetido = False
        for v in self.videos:
            if v["nombre"] == video["nombre"] and v["artista"] == video["artista"]:
                repetido = True
        if self.espacio_disponible() >= video["peso"] * 1024:
            if repetido == False:
                self.videos.append(video)
        return self

    def __str__(self):
        return f"MP4 {self.marca}\nCapacidad: {self.capacidad / 1024 / 1024:.2f} GB\nCanciones: {len(self.canciones)}\nVideos: {len(self.videos)}\nEspacio disponible: {self.espacio_disponible() / 1024 / 1024:.2f} GB\n"

mp4 = MP4("Sony", 1) 

c1 = {"nombre": "Back To Black", "artista": "Maddona", "peso": 100}
c2 = {"nombre": "Lost On You", "artista": "One Direction", "peso": 150}
v1 = {"nombre": "Duele el Corazon", "artista": "Enrique Iglesias", "peso": 50}
v2 = {"nombre": "Harmonica Andromeda", "artista": "KSHMR", "peso": 70}

mp4 = mp4 + c1
mp4 = mp4 + c2
mp4 = mp4 - v1
mp4 = mp4 - v2

print(mp4)

mp4.borrar_cancion("Back To Black", "Maddona", 100)
print("Después de borrar una canción:")
print(mp4)
