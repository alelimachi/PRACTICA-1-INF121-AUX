
package main1;

// JefePolicia.java
public class JefePolicia extends Persona implements Empleado, Policia {
    private double sueldo;
    private String cargo;
    private String grado;
    private String unidad;

    public JefePolicia(String nombre, int edad, double sueldo, String cargo, String grado, String unidad) {
        super(nombre, edad);
        this.sueldo = sueldo;
        this.cargo = cargo;
        this.grado = grado;
        this.unidad = unidad;
    }

    // Métodos de Empleado
    public double getSueldo() {
        return sueldo;
    }

    public String getCargo() {
        return cargo;
    }

    // Métodos de Policia
    public String getGrado() {
        return grado;
    }

    public String getUnidad() {
        return unidad;
    }

    public void mostrarDatos() {
        System.out.println("Nombre: " + nombre);
        System.out.println("Edad: " + edad);
        System.out.println("Cargo: " + cargo);
        System.out.println("Grado: " + grado);
        System.out.println("Unidad: " + unidad);
        System.out.println("Sueldo: " + sueldo);
        System.out.println();
    }
}

