
package eje10pers;
import java.util.ArrayList;

public class Jugador {
     private String nombre;
    private int nivel;
    private int puntaje;

    public Jugador() {}

    public Jugador(String nombre, int nivel, int puntaje) {
        this.nombre = nombre;
        this.nivel = nivel;
        this.puntaje = puntaje;
    }

    public String getNombre() {
        return nombre;
    }

    public int getNivel() {
        return nivel;
    }

    public int getPuntaje() {
        return puntaje;
    }

    @Override
    public String toString() {
        return "Nombre: " + nombre +  " Nivel: " + nivel + " Puntaje: " + puntaje;
    }
}
   
    
