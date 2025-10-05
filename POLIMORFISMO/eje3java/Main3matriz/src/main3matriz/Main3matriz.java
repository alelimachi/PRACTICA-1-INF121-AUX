
package main3matriz;

public class Main3matriz {

    public static void main(String[] args) {
        Matriz m1 = new Matriz();
        System.out.println("Matriz 1:");
        m1.mostrar();

        int[][] valores = new int[10][10];
        for (int i = 0; i < 10; i++) {
            for (int j = 0; j < 10; j++) {
                valores[i][j] = i + j;
            }
        }
        Matriz m2 = new Matriz(valores);
        System.out.println("Matriz 2:");
        m2.mostrar();

        Matriz suma = m1.sumar(m2);
        System.out.println("Suma de m1 + m2:");
        suma.mostrar();

        Matriz resta = m2.restar(m1);
        System.out.println("Resta de m2 - m1:");
        resta.mostrar();

        System.out.println("¿m1 es igual a m2? " + m1.igual(m2));
    }
}
      
