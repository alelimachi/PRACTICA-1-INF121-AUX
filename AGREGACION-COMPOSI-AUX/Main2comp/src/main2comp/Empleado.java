package main2comp;

public class Empleado {
    private String nombre;
    private String cargo;
    private double sueldo;

    public Empleado(String nombre, String cargo, double sueldo) {
        this.nombre = nombre;
        this.cargo = cargo;
        this.sueldo = sueldo;
    }

    public void mostrar() {
        System.out.println("Nombre: " + nombre + " Cargo: " + cargo + " Sueldo: " + sueldo);
    }

    public void cambiarSueldo(double nuevo) {
        this.sueldo = nuevo;
    }

    public double getSueldo() {
        return sueldo;
    }

    public String getNombre() {
        return nombre;
    }
}
    
