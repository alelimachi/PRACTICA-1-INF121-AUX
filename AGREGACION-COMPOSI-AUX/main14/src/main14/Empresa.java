
package main14;
import java.util.ArrayList;
import java.util.Scanner;
public class Empresa {
     private String nombre;
    private ArrayList<Empleado> empleados;

    public Empresa(String nombre) {
        this.nombre = nombre;
        this.empleados = new ArrayList<>();
    }

    public void agregarEmpleado(Empleado e) {
        empleados.add(e);
    }

    public void mostrarInfo() {
        System.out.println("Empresa: " + nombre);
        System.out.println("Total empleados: " + empleados.size());
        for (int i = 0; i < empleados.size(); i++) {
            System.out.println((i + 1) + ". " + empleados.get(i));
        }
    }

    public Empleado buscarEmpleadoPorNombre(String nombre) {
        for (Empleado e : empleados) {
            if (e.getNombre().equalsIgnoreCase(nombre)) {
                return e;
            }
        }
        return null;
    }

    public boolean eliminarEmpleadoPorNombre(String nombre) {
        for (int i = 0; i < empleados.size(); i++) {
            if (empleados.get(i).getNombre().equalsIgnoreCase(nombre)) {
                empleados.remove(i);
                return true;
            }
        }
        return false;
    }

    public double promedioSalarial() {
        if (empleados.isEmpty()) return 0;
        double total = 0;
        for (Empleado e : empleados) total += e.getSalario();
        return total / empleados.size();
    }

    public ArrayList<Empleado> empleadosConSalarioMayorA(double valor) {
        ArrayList<Empleado> lista = new ArrayList<>();
        for (Empleado e : empleados) {
            if (e.getSalario() > valor) lista.add(e);
        }
        return lista;
    }
}
