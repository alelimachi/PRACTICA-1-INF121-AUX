/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package principalbuzon15;

/**
 *
 * @author user
 */
public class PrincipalBuzon15 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        Buzon b1 = new Buzon(1);
        Buzon b2 = new Buzon(2);
        Buzon b3 = new Buzon(3);

        Carta c1 = new Carta("C123", "Querido amigo, te escribo con mucho amor y cariño.",
                             "Juan Álvarez", "Peter Chaves");
        Carta c2 = new Carta("C456", "Querido amigo, ella no te ama por lo tanto continúa la carta.",
                             "Pepe Mujica", "Wilmer Pérez");
        Carta c3 = new Carta("C789", "Saludos, espero verte pronto en el evento de amor y amistad.",
                             "Paty Vasques", "Pepe Mujica");

        b1.agregarCarta(c1);
        b1.agregarCarta(c2);
        b1.agregarCarta(c3);

        System.out.println("Pepe Mujica recibió: " + b1.contarCartasRecibidas("Pepe Mujica") + " carta(s)");

        System.out.println("\nEliminando carta con código C456");
        b1.eliminarPorCodigo("C456");
        b1.mostrarCartas();

        String remitente = "Juan Álvarez";
        if (b1.remitenteEnvio(remitente))
            System.out.println("\nEl remitente " + remitente + " ha enviado al menos una carta.");
        else
            System.out.println("El remitente " + remitente + " no ha enviado cartas.");
        System.out.println("Buscando la palabra clave 'amor' en las cartas:");
        b1.buscarPalabraClave("amor");
    }
}
