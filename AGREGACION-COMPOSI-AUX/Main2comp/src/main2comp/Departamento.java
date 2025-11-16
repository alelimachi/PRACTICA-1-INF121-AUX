package main2comp;
import java.util.ArrayList;

public class Departamento {
    private String nombre;
    private String area;
    private ArrayList<Empleado> empleados;  

    public Departamento(String nombre, String area) {
        this.nombre = nombre;
        this.area = area;
        this.empleados = new ArrayList<>();
    }

    public void mostrarEmpleados() {
        System.out.println("Departamento: " + nombre + " - " + area);

        if (empleados.isEmpty()) {
            System.out.println("  No hay empleados.");
            return;
        }

        int i = 1;
        for (Empleado e : empleados) {
            System.out.print(" " + i + ". ");
            e.mostrar();
            i++;
        }
    }

    public void agregarEmpleado(Empleado e) {
        empleados.add(e);
    }

    public void cambioSalario(double porcentaje) {
        for (Empleado e : empleados) {
            double nuevo = e.getSueldo() + e.getSueldo() * porcentaje / 100;
            e.cambiarSueldo(nuevo);
        }
        System.out.println("Sueldos actualizados en el dpto" + nombre);
    }

    public boolean contieneEmpleado(Empleado e) {
        return empleados.contains(e);
    }

    public void moverEmpleadosA(Departamento otroDepto) {
        int cantidad = empleados.size();

        for (Empleado e : empleados) {
            otroDepto.agregarEmpleado(e);
        }

        empleados.clear();
        System.out.println("Se movieron " + cantidad + " empleados de " + nombre +
                " a " + otroDepto.nombre);
    }
}
    
