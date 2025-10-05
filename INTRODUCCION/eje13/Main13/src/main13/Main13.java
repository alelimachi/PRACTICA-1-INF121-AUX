package main13;

public class Main13 {

    public static void main(String[] args) {
        Fruta f1 = new Fruta("Kiwi", "Subtropical", new String[] {"K", "C", "E"});
        
        String[] vitaminas2 = {"A", "C"};
        Fruta f2 = new Fruta("Naranja", "Tropical", vitaminas2);
        
        String[] vitaminas3 = new String[3];
        vitaminas3[0] = "A";
        vitaminas3[1] = "B";
        vitaminas3[2] = "C";
        Fruta f3 = new Fruta("Manzana", "Templado", vitaminas3);

        Fruta[] frutas = {f1, f2, f3};
        Fruta mayor = frutas[0];
        for (int i = 1; i < frutas.length; i++) {
            if (frutas[i].getNroVitaminas() > mayor.getNroVitaminas())
                mayor = frutas[i];
        }
        System.out.println("La fruta con más vitaminas es: " + mayor.getNombre() +
                           " (" + mayor.getNroVitaminas() + " vitaminas)");
        for (Fruta f : frutas) {
            if (f.getNombre().equalsIgnoreCase("Kiwi")) {
                f.mostrarVitaminas();
            }
        }

        for (Fruta f : frutas) {
            System.out.println(f.getNombre() + " tiene " + f.contarCitricas() + " vitaminas cítricas");
        }
        for (Fruta f : frutas) {
            f.ordenarVitaminas();
        }

        System.out.println("\nVitaminas ordenadas alfabéticamente:");
        for (Fruta f : frutas) {
            f.mostrarVitaminas();
        }
    }
}

