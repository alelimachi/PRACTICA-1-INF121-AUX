
package main2;

public class Main2 {

    public static void main(String[] args) {
        Bus bus1 = new Bus(40);
        bus1.subirPasajeros(15);
        bus1.subirPasajeros(19);
        bus1.asientosDisponibles();
        bus1.calcularCostoPasajes();
    }
}


