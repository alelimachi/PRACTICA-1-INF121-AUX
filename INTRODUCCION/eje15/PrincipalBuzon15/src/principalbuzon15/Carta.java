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
public class Carta {
    public String codigo;
    public String descripcion;
    public String remitente;
    public String destinatario;

    // Constructor
    public Carta(String codigo, String descripcion, String remitente, String destinatario) {
        this.codigo = codigo;
        this.descripcion = descripcion;
        this.remitente = remitente;
        this.destinatario = destinatario;
    }

    // Getters
    public String getCodigo() { return codigo; }
    public String getDescripcion() { return descripcion; }
    public String getRemitente() { return remitente; }
    public String getDestinatario() { return destinatario; }

    // Mostrar información
    public void mostrar() {
        System.out.println("Código: " + codigo);
        System.out.println("Remitente: " + remitente);
        System.out.println("Destinatario: " + destinatario);
        System.out.println("Descripción: " + descripcion);
    }
}
    
