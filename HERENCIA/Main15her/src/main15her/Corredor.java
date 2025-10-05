
package main15her;

public class Corredor {
    protected int distanciaPref;

    public Corredor(int distanciaPref) {
        this.distanciaPref = distanciaPref;
    }

    public void correr() {
        System.out.println("Corriendo una distancia de " + distanciaPref + " km");
    }
}

