class Persona:
    def __init__(self, nombre, apellido, edad, ci):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.ci = ci

    def ver(self):
        return f"{self.nombre} {self.apellido} (CI: {self.ci})"


class Speaker(Persona):
    def __init__(self, nombre, apellido, edad, ci, especialidad):
        super().__init__(nombre, apellido, edad, ci)
        self.especialidad = especialidad

    def ver(self):
        return super().ver() + f" - Especialidad: {self.especialidad}"


class Participante(Persona):
    def __init__(self, nombre, apellido, edad, ci, ticket):
        super().__init__(nombre, apellido, edad, ci)
        self.ticket = ticket

    def ver(self):
        return super().ver() + f" - Ticket: {self.ticket}"


class Charla:
    MAX_PART = 50
    def __init__(self, lugar, nombreCharla, speaker):
        self.lugar = lugar
        self.nombreCharla = nombreCharla
        self.s = speaker
        self.np = 0
        self.p = [None] * self.MAX_PART

    def add(self, part):
        if self.np < self.MAX_PART:
            self.p[self.np] = part
            self.np += 1
            return True
        return False

    def part(self):
        return self.p[:self.np]

    def ver(self):
        return f"Charla: {self.nombreCharla} Lugar: {self.lugar} Speaker: {self.s.nombre} {self.s.apellido}"


class Evento:
    MAX_CHAR = 50
    def __init__(self, nombre):
        self.nombre = nombre
        self.nc = 0
        self.c = [None] * self.MAX_CHAR

    def add(self, charla):
        if self.nc < self.MAX_CHAR:
            self.c[self.nc] = charla
            self.nc += 1
            return True
        return False

    def charlas(self):
        return self.c[:self.nc]

    def edad_prom(self):
        total = 0
        cant = 0
        for i in range(self.nc):
            ch = self.c[i]
            for j in range(ch.np):
                total += ch.p[j].edad
                cant += 1
        return total / cant if cant > 0 else 0

    def buscar(self, nombre, apellido):
        for i in range(self.nc):
            ch = self.c[i]
            if ch.s.nombre == nombre and ch.s.apellido == apellido:
                return f"{nombre} {apellido} es SPEAKER en '{ch.nombreCharla}'"
            for j in range(ch.np):
                if ch.p[j].nombre == nombre and ch.p[j].apellido == apellido:
                    return f"{nombre} {apellido} es PARTICIPANTE en '{ch.nombreCharla}'"
        return f"{nombre} {apellido} NO se encuentra en el evento."

    def ordenar(self):
        chs = [self.c[i] for i in range(self.nc)]
        for i in range(len(chs)-1):
            for j in range(len(chs)-i-1):
                if chs[j].np < chs[j+1].np:
                    chs[j], chs[j+1] = chs[j+1], chs[j]
        for i in range(len(chs)):
            self.c[i] = chs[i]
        for i in range(len(chs), self.MAX_CHAR):
            self.c[i] = None
        return chs

    def ver(self):
        return f"Evento: {self.nombre} | Charlas: {self.nc}"

sp1 = Speaker("Ana", "Ruiz", 40, 100, "IA")
sp2 = Speaker("Carlos", "Mendez", 55, 200, "Robótica")

ch1 = Charla("Auditorio A", "Introducción a INF-111", sp1)
ch2 = Charla("Sala 3", "INtroduccion a la IA", sp2)
ch3 = Charla("Auditorio B", "Procesamiento de Datos", sp1)

ev = Evento("2025")

ev.add(ch1)
ev.add(ch2)
ev.add(ch3)

print(ev.ver())
