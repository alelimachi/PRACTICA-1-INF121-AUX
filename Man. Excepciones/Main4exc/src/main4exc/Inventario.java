package main4exc;

public class Inventario {
    private Producto[] productos;
    private int cantidad;
    private final int MAX = 100;

    public Inventario() {
        productos = new Producto[MAX];
        cantidad = 0;
    }

    public void agregarProducto(Producto p) throws ProductoYaExisteException, IllegalArgumentException {

        if (p.getPrecio() < 0 || p.getStock() < 0) {
            throw new IllegalArgumentException("Precio o stock no pueden ser negativos.");
        }

        for (int i = 0; i < cantidad; i++) {
            if (productos[i].getCodigo().equals(p.getCodigo())) {
                throw new ProductoYaExisteException("El código " + p.getCodigo() + " ya existe.");
            }
        }

        if (cantidad < MAX) {
            productos[cantidad] = p;
            cantidad++;
        }
    }

    public Producto buscarProducto(String codigo) throws ProductoNoEncontradoException {
        for (int i = 0; i < cantidad; i++) {
            if (productos[i].getCodigo().equals(codigo)) {
                return productos[i];
            }
        }
        throw new ProductoNoEncontradoException("Producto con código " + codigo + " no encontrado.");
    }
    
    public void venderProducto(String codigo, int cant) 
            throws ProductoNoEncontradoException, StockInsuficienteException {

        Producto p = buscarProducto(codigo);

        if (p.getStock() < cant) {
            throw new StockInsuficienteException(
                "Stock insuficiente para " + p.getNombre() + 
                ". Disponible: " + p.getStock() +
                ", solicitado: " + cant
            );
        }

        p.reducirStock(cant);
    }

    public void listarProductos() {
        System.out.println("\n INVENTARIO");
        for (int i = 0; i < cantidad; i++) {
            System.out.println(productos[i]);
        }
    }
}
    
