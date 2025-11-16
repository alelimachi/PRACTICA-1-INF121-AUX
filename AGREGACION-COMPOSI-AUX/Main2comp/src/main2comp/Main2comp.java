
package main2comp;

public class Main2comp {

    public static void main(String[] args) {
        Departamento dep1 = new Departamento("Recursos Humanos", "Administración");
        Departamento dep2 = new Departamento("Contabilidad", "Finanzas");

        Empleado emp1 = new Empleado("Ana", "Secretaria", 3500);
        Empleado emp2 = new Empleado("Luis", "Analista", 4200);
        Empleado emp3 = new Empleado("María", "Jefa", 5800);
        Empleado emp4 = new Empleado("Carlos", "Asistente", 3000);
        Empleado emp5 = new Empleado("Elena", "Contadora", 4500);
        
        dep1.agregarEmpleado(emp1);
        dep1.agregarEmpleado(emp2);
        dep1.agregarEmpleado(emp3);
        dep1.agregarEmpleado(emp4);
        dep1.agregarEmpleado(emp5);

        dep1.mostrarEmpleados();
        System.out.println();

        dep2.mostrarEmpleados();
        System.out.println();

        dep1.cambioSalario(10);
        dep1.mostrarEmpleados();
        System.out.println();

        Empleado empleadoAVerificar = emp3;

        if (dep2.contieneEmpleado(empleadoAVerificar)) {
            System.out.println(empleadoAVerificar.getNombre() + " también está en " + dep2);
        } else {
            System.out.println(empleadoAVerificar.getNombre() + " no pertenece a " + dep2);
        }

        System.out.println();

        dep1.moverEmpleadosA(dep2);
        System.out.println();

        dep1.mostrarEmpleados();
        System.out.println();
        dep2.mostrarEmpleados();
    }
}

