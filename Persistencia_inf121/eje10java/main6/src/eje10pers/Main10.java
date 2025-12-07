package eje10pers;

import java.util.ArrayList;
import java.util.Scanner;

public class Main10 {


    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        GestorJugadores gestor = new GestorJugadores();

        int opcion;

        do {
            System.out.println(" VIDEOJUEGO DE ESTRATEGIA");
            System.out.println("1. Registrar jugador");
            System.out.println("2. Mostrar jugadores");
            System.out.println("3. Buscar jugador por nombre");
            System.out.println("4. Salir");
            System.out.print("Seleccione opción: ");
            opcion = sc.nextInt();
            sc.nextLine(); 

            switch (opcion) {
                case 1:
                    System.out.print("Nombre: ");
                    String nombre = sc.nextLine();
                    System.out.print("Nivel: ");
                    int nivel = sc.nextInt();
                    System.out.print("Puntaje: ");
                    int puntaje = sc.nextInt();

                    Jugador j = new Jugador(nombre, nivel, puntaje);
                    gestor.agregarJugador(j);

                    System.out.println("Jugador guardado con exito.\n");
                    break;

                case 2:
                    gestor.mostrarJugadores();
                    break;

                case 3:
                    System.out.print("Nombre del jugador a buscar: ");
                    String busqueda = sc.nextLine();
                    gestor.buscarPorNombre(busqueda);
                    break;

                case 4:
                    System.out.println("Chao");
                    break;

                default:
                    System.out.println("Opción inválida.\n");
            }

        } while (opcion != 4);
    }
}
         


    
   
