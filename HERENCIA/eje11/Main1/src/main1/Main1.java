
package main1;

public class Main1 {

    public static void main(String[] args) {
        JefePolicia j1 = new JefePolicia("Carlos", 45, 5500, "Mayor", "Mayor", "Unidad A");
        JefePolicia j2 = new JefePolicia("Lucía", 40, 6200, "Teniente", "Subteniente", "Unidad B");
        JefePolicia j3 = new JefePolicia("Carlos", 50, 4800, "Teniente", "Teniente", "Unidad A");

        System.out.println("DATOS DE LOS JEFES:");
        j1.mostrarDatos();
        j2.mostrarDatos();
        j3.mostrarDatos();
       
        JefePolicia mayorSueldo = j1;
        if (j2.getSueldo() > mayorSueldo.getSueldo()) {
            mayorSueldo = j2;
        }
        if (j3.getSueldo() > mayorSueldo.getSueldo()) {
            mayorSueldo = j3;
        }
        System.out.println("Jefe mayor sueldo: " + mayorSueldo.getNombre() + " (Bs" + mayorSueldo.getSueldo() + ")\n");

        if (j1.getGrado().equals(j2.getGrado())) {
            System.out.println("j1 y j2 tienen el mismo grado.");
        } else {
            System.out.println("j1 y j2 no tienen el mismo grado.");
        }

        if (j1.getNombre().equals(j3.getNombre())) {
            System.out.println("j1 y j3 tienen el mismo nombre.");
        } else {
            System.out.println("j1 y j3 tienen diferente nombre.");
        }
    }
        
}
  
