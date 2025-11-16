class Doctor:
    def __init__(self, nombre, especialidad):
        self.nombre = nombre
        self.especialidad = especialidad  
    
    def __str__(self):
        return f"Dr. {self.nombre} - Especialidad: {self.especialidad}"

class Hospital:
    def __init__(self, nombre):
        self.nombre = nombre
        self.doctores = []
    
    def agreg_doctor(self, doctor):
        self.doctores.append(doctor)
    
    def mostrar_doctores(self):
        print(f"\nDoctores en el hospital {self.nombre}:")
        for doctor in self.doctores:
            print(doctor)

d1 = Doctor("Cristina Chang", "Cardiología")
d2 = Doctor("Alex Karev", "Pediatría")
d3 = Doctor("George O'Malley", "Traumatología")
d4 = Doctor("Sheppard", "Neurología")

h1 = Hospital("Hospital de Seattle")
h2 = Hospital("Hospital San José")

h1.agreg_doctor(d1)
h1.agreg_doctor(d2)
h2.agreg_doctor(d3)
h2.agreg_doctor(d4)
h2.agreg_doctor(d1)

h1.mostrar_doctores()
h2.mostrar_doctores()