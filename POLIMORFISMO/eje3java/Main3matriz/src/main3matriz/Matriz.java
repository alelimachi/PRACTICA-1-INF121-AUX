
package main3matriz;


public class Matriz {
    public int[][] matriz;
    public Matriz() {
        matriz = new int[10][10];
        for (int i = 0; i < 10; i++) {
            matriz[i][i] = 1;  
        }
    }

    public Matriz(int[][] valores) {
        matriz = new int[10][10];
        for (int i = 0; i < 10; i++) {
            for (int j = 0; j < 10; j++) {
                matriz[i][j] = valores[i][j];
            }
        }
    }

    public Matriz sumar(Matriz otra) {
        Matriz resultado = new Matriz();
        for (int i = 0; i < 10; i++) {
            for (int j = 0; j < 10; j++) {
                resultado.matriz[i][j] = this.matriz[i][j] + otra.matriz[i][j];
            }
        }
        return resultado;
    }

    public Matriz restar(Matriz otra) {
        Matriz resultado = new Matriz();
        for (int i = 0; i < 10; i++) {
            for (int j = 0; j < 10; j++) {
                resultado.matriz[i][j] = this.matriz[i][j] - otra.matriz[i][j];
            }
        }
        return resultado;
    }

    public boolean igual(Matriz otra) {
        for (int i = 0; i < 10; i++) {
            for (int j = 0; j < 10; j++) {
                if (this.matriz[i][j] != otra.matriz[i][j]) {
                    return false;
                }
            }
        }
        return true;
    }
    public void mostrar() {
        for (int i = 0; i < 10; i++) {
            for (int j = 0; j < 10; j++) {
                System.out.print(matriz[i][j] + "\t");
            }
            System.out.println();
        }
        System.out.println();
    }
}
    
