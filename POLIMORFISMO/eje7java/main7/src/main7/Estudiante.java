
package main7;

class Estudiante extends Persona {
    public String ru;
    public String matricula;

    public Estudiante(String nombre, String paterno, String materno, int edad, String ru, String matricula) {
        super(nombre, paterno, materno, edad);
        this.ru = ru;
        this.matricula = matricula;
    }

    @Override
    public void mostrar() {
        super.mostrar();
        System.out.println("RU: " + ru);
        System.out.println("Matrícula: " + matricula);
    }

    public void modificarEdad(int nuevaEdad) {
        this.edad = nuevaEdad;
    }

    public static double promedio(Estudiante[] estudiantes) {
        int suma = 0;
        for (Estudiante e : estudiantes) {
            suma += e.getEdad();
        }
        return (double) suma / estudiantes.length;
    }
}

