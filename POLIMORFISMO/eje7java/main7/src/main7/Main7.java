
package main7;

public class Main7 {

    public static void main(String[] args) {

        Estudiante e1 = new Estudiante("Ana", "Gomez", "Lopez", 20, "RU123", "INF-111");
        Estudiante e2 = new Estudiante("Luis", "Perez", "Mamani", 22, "RU456", "INF-121");
        Docente d1 = new Docente("Carlos", "Rojas", "Flores", 22, 5500, "INF-115");

        System.out.println("Est 1:");
        e1.mostrar();
        System.out.println("Est 2:");
        e2.mostrar();
        System.out.println("DOCENTE:");
        d1.mostrar();

        Estudiante[] estudiantes = {e1, e2};
        System.out.println("Promedio de edad de los estudiantes: " + Estudiante.promedio(estudiantes));

        e1.modificarEdad(25);
        System.out.println("Edad modificada de Est 1:");
        e1.mostrar();

        if (e2.getEdad() == d1.getEdad()) {
            System.out.println("\nEl est 2 tiene la misma edad que el docente.");
        } else {
            System.out.println("\nEl est 2 no tiene la misma edad que el docente.");
        }
    }
}

    
