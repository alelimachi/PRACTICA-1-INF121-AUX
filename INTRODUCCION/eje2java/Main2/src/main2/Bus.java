
package main2;

public class Bus {
    public int capacidad;
    public int pasajerosActuales;
    public double costoPas;

    public Bus(int capacidad) {
        this.capacidad = capacidad;
        this.pasajerosActuales = 0;
        this.costoPas = 1.50;
    }

    public void subirPasajeros(int cantidad) {
        if (pasajerosActuales + cantidad <= capacidad) {
            pasajerosActuales += cantidad;
            System.out.println("Subieron " + cantidad + " pasajeros. Total: " + pasajerosActuales);
        } else {
            System.out.println("No hay espacio suficiente para " + cantidad + " pasajeros.");
        }
    }

    public double calcularCostoPasajes() {
        double total = pasajerosActuales * costoPas;
        System.out.printf("Se cobraron Bs.%.2f en pasajes%n", total);
        return total;
    }

    public int asientosDisponibles() {
        int disponibles = capacidad - pasajerosActuales;
        System.out.println("Asientos disponibles: " + disponibles);
        return disponibles;
    }
    
}
