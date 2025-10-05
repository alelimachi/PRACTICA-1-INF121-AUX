
package principalbuzon15;

import java.util.ArrayList;

public class Buzon {
    public int nro;
    public ArrayList<Carta> cartas;

    public Buzon(int nro) {
        this.nro = nro;
        this.cartas = new ArrayList<>();
    }

    // Agregar carta
    public void agregarCarta(Carta c) {
        cartas.add(c);
    }

    public int contarCartasRecibidas(String destinatario) {
        int cont = 0;
        for (Carta c : cartas) {
            if (c.getDestinatario().equalsIgnoreCase(destinatario))
                cont++;
        }
        return cont;
    }

    public void eliminarPorCodigo(String codigo) {
        cartas.removeIf(c -> c.getCodigo().equalsIgnoreCase(codigo));
    }

    public boolean remitenteEnvio(String remitente) {
        for (Carta c : cartas) {
            if (c.getRemitente().equalsIgnoreCase(remitente))
                return true;
        }
        return false;
    }

    // Buscar palabra clave en descripción y mostrar coincidencias
    public void buscarPalabraClave(String palabra) {
        for (Carta c : cartas) {
            if (c.getDescripcion().toLowerCase().contains(palabra.toLowerCase())) {
                System.out.println("Coincidencia encontrada:");
                c.mostrar();
            }
        }
    }

    public void mostrarCartas() {
        System.out.println("BUZÓN Nº " + nro + " =");
        for (Carta c : cartas) {
            c.mostrar();
        }
    }
}
