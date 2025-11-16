
package main2exc;

import java.util.Scanner;
public class Main2exc {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        try {
            System.out.print("Ingrese número 1: ");
            int n1 = Calculadora.convertir(sc.nextLine());

            System.out.print("Ingrese número 2: ");
            int n2 = Calculadora.convertir(sc.nextLine());

            System.out.println("\n=== OPERACIONES ===");
            System.out.println("Suma: " + Calculadora.sumar(n1, n2));
            System.out.println("Resta: " + Calculadora.restar(n1, n2));
            System.out.println("Multiplicación: " + Calculadora.multiplicar(n1, n2));
            
            try {
                System.out.println("División: " + Calculadora.dividir(n1, n2));
            } catch (ArithmeticException e) {
                System.out.println("Error en división: " + e.getMessage());
            }

        } catch (NumeroInvalidoException e) {
            System.out.println("Error: " + e.getMessage());
        }
    }
}

    