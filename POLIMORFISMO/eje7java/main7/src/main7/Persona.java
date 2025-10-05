
package main7;

public class Persona {
    public String nombre;
    public String paterno;
    public String materno;
    public int edad;

    public Persona(String nombre, String paterno, String materno, int edad) {
        this.nombre = nombre;
        this.paterno = paterno;
        this.materno = materno;
        this.edad = edad;
    }

    public void mostrar() {
        System.out.println("Nombre: " + nombre + " " + paterno + " " + materno);
        System.out.println("Edad: " + edad);
    }

    public int getEdad() {
        return edad;
    }
}

    

