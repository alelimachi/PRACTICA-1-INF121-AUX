package eje10pers;
import com.google.gson.Gson;
import com.google.gson.reflect.TypeToken;
import java.io.FileReader;
import java.io.FileWriter;
import java.util.ArrayList;
import java.util.List;


public class GestorJugadores {
     private final String archivo = "jugadores.txt";
    private final Gson gson = new Gson();

    public List<Jugador> cargar() {
        try (FileReader fr = new FileReader(archivo)) {
            return gson.fromJson(fr, new TypeToken<List<Jugador>>() {}.getType());
        } catch (Exception e) {
            return new ArrayList<>();
        }
    }

    public void guardar(List<Jugador> lista) {
        try (FileWriter fw = new FileWriter(archivo)) {
            gson.toJson(lista, fw);
        } catch (Exception e) {
            System.out.println("Error al guardar datos");
        }
    }

    public void agregarJugador(Jugador j) {
        List<Jugador> lista = cargar();
        lista.add(j);
        guardar(lista);
    }

    public void mostrarJugadores() {
        List<Jugador> lista = cargar();

        if (lista.size() == 0) {
            System.out.println("\nNo hay jugadores registrados.\n");
            return;
        }

        System.out.println("\n LISTA DE JUGADORES");
        for (Jugador j : lista) {
            System.out.println(j);
        }
        System.out.println();
    }

    public void buscarPorNombre(String nombre) {
        List<Jugador> lista = cargar();

        for (Jugador j : lista) {
            if (j.getNombre().equalsIgnoreCase(nombre)) {
                System.out.println("\nJugador encontrado:");
                System.out.println(j);
                return;
            }
        }

        System.out.println("\nJugador no encontrado.\n");
    }
}
   


