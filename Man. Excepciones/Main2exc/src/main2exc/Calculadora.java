
package main2exc;
public class Calculadora {
    public static int sumar(int a, int b) {
        return a + b;
    }

    public static int restar(int a, int b) {
        return a - b;
    }

    public static int multiplicar(int a, int b) {
        return a * b;
    }

    public static int dividir(int a, int b) throws ArithmeticException {
        if (b == 0) {
            throw new ArithmeticException("No se puede dividir entre cero.");
        }
        return a / b;
    }

    public static int convertir(String valor) throws NumeroInvalidoException {
        try {
            return Integer.parseInt(valor);
        } catch (NumberFormatException e) {
            throw new NumeroInvalidoException("El valor '" + valor + "' no es un número válido.");
        }
    }
}
   
