
package main2exc;
public class NumeroInvalidoException extends Exception{
        public NumeroInvalidoException() {
        super("Valor no es numérico.");
    }
    public NumeroInvalidoException(String message) {
        super(message);
    }
}

