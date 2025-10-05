
package main15her;

public class Ciclista {
    protected String tipoBici;

    public Ciclista(String tipoBici) {
        this.tipoBici = tipoBici;
    }

    public void pedalear() {
        System.out.println("Pedaleando en bicicleta tipo " + tipoBici);
    }
}
