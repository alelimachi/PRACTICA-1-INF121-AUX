
package main15her;

public class Triatleta extends Nadador {
    private Ciclista ciclista;
    private Corredor corredor;

    public Triatleta(String estiloNatacion, String tipoBici, int distanciaPref) {
        super(estiloNatacion);
        this.ciclista = new Ciclista(tipoBici);
        this.corredor = new Corredor(distanciaPref);
    }

    public void pedalear() {
        ciclista.pedalear();
    }

    public void correr() {
        corredor.correr();
    }
}