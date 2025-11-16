
package main4exc;

public class Main4exc {

    public static void main(String[] args) {
          Inventario inv = new Inventario();

        try {
            Producto p1 = new Producto("01", "Laptop", 1200.5, 5);
            Producto p2 = new Producto("02", "Mouse", 25.0, 50);
            Producto p3 = new Producto("03", "Teclado", 45.99, 30);

            inv.agregarProducto(p1);
            inv.agregarProducto(p2);
            inv.agregarProducto(p3);

            try {
                inv.agregarProducto(new Producto("01", "Otro", 100, 1));
            } catch (ProductoYaExisteException e) {
                System.out.println("\nOK → " + e.getMessage());
            }

            inv.listarProductos();

            try {
                Producto buscado = inv.buscarProducto("02");
                System.out.println("\nEncontrado " + buscado);

                inv.buscarProducto("ZZZ");
            } catch (ProductoNoEncontradoException e) {
                System.out.println("OK " + e.getMessage());
            }

            inv.venderProducto("A001", 2);
            System.out.println("\nVenta realizada. Nuevo stock A001: "
                    + inv.buscarProducto("A001").getStock());

            try {
                inv.venderProducto("03", 100);
            } catch (StockInsuficienteException e) {
                System.out.println("OK " + e.getMessage());
            }

            try {
                inv.venderProducto("XYZ", 1);
            } catch (ProductoNoEncontradoException e) {
                System.out.println("OK " + e.getMessage());
            }

            inv.listarProductos();

        } catch (Exception e) {
            System.out.println("Error general: " + e.getMessage());
        }
    }
}
  