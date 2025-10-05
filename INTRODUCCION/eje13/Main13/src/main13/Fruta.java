package main13;

public class Fruta {
    public String nombre;
    public String tipo;
    public int nroVitaminas;
    public String[] v; 

    public Fruta(String nombre, String tipo, String[] vitaminas) {
        this.nombre = nombre;
        this.tipo = tipo;
        this.v = vitaminas;
        this.nroVitaminas = vitaminas.length;
    }

    public String getNombre() {
        return nombre;
    }

    public int getNroVitaminas() {
        return nroVitaminas;
    }

    // Mostrar vitaminas
    public void mostrarVitaminas() {
        System.out.print("Vitaminas de " + nombre + ": ");
        for (int i = 0; i < nroVitaminas; i++) {
            System.out.print(v[i]);
            if (i < nroVitaminas - 1)
                System.out.print(", ");
        }
        System.out.println();
    }

    public int contarCitricas() {
        int cont = 0;
        for (String vit : v) {
            if (vit.equalsIgnoreCase("C"))
                cont++;
        }
        return cont;
    }

    public void ordenarVitaminas() {
        for (int i = 0; i < nroVitaminas - 1; i++) {
            for (int j = i + 1; j < nroVitaminas; j++) {
                if (v[i].compareToIgnoreCase(v[j]) > 0) {
                    String aux = v[i];
                    v[i] = v[j];
                    v[j] = aux;
                }
            }
        }
    }
    
}
