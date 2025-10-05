
package main15her;

public class Nadador {
    protected String estiloNatacion;

    public Nadador(String estiloNatacion) {
        this.estiloNatacion = estiloNatacion;
    }

    public void nadar() {
        System.out.println("Nadando estilo " + estiloNatacion);
    }
}
