package main14;

import java.util.ArrayList;
import java.util.Scanner;
public class Main14 {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Nombre de la empresa: ");
        String nombreEmpresa = sc.nextLine();
        Empresa empresa = new Empresa(nombreEmpresa);
        int opc;
        do {
            System.out.println("1.Agregar empleado");
            System.out.println("2.Mostrar empresa y empleados");
            System.out.println("3.Buscar empleado por nombre");
            System.out.println("4.Eliminar empleado por nombre");
            System.out.println("5.Promedio salarial");
            System.out.println("0.Salir");
            System.out.print("Elija una opción: ");
            opc= sc.nextInt();
            sc.nextLine();

            switch (opc) {
                case 1:
                    System.out.print("Nombre del empleado: ");
                    String nom = sc.nextLine();
                    System.out.print("Puesto: ");
                    String puesto = sc.nextLine();
                    System.out.print("Salario: ");
                    double sal = sc.nextDouble();
                    sc.nextLine();
                    empresa.agregarEmpleado(new Empleado(nom, puesto, sal));
                    System.out.println("Empleado agregado.");
                    break;

                case 2:
                    empresa.mostrarInfo();
                    break;

                case 3:
                    System.out.print("Nombre del empleado a buscar: ");
                    String nb = sc.nextLine();
                    Empleado encontrado = empresa.buscarEmpleadoPorNombre(nb);
                    if (encontrado != null) System.out.println(encontrado);
                    else System.out.println("Empleado no encontrado.");
                    break;

                case 4:
                    System.out.print("Nombre del empleado a eliminar: ");
                    String ne = sc.nextLine();
                    if (empresa.eliminarEmpleadoPorNombre(ne))
                        System.out.println("Empleado eliminado.");
                    else
                        System.out.println("Empleado no encontrado.");
                    break;

                case 5:
                    System.out.println("Promedio salarial: " + empresa.promedioSalarial());
                    break;
            }
        } while (opc != 0);

        System.out.println("CHAO");
    }
}
