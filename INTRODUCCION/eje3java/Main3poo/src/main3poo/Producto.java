
package main3poo;

public class Producto {
    private String nombre;
    private double precio;
    private int stock;

    public Producto(String nombre, double precio, int stock) {
        this.nombre = nombre;
        this.precio = precio;
        this.stock = stock;
    }
    public void vender(int cantidad) {
        if (cantidad <= stock) {
            stock -= cantidad;
            System.out.println("Se vendieron " + cantidad + " " + nombre + ". Stock restante: " + stock);
        } else {
            System.out.println("No hay suficiente stock");
        }
    }

    public void reabastecer(int cantidad) {
        stock += cantidad;
        System.out.println("Se reabastecieron " + cantidad + " " + nombre + ". Stock total: " + stock);
    }
}
