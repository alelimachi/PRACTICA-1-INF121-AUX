
package main6exc;

public class Main6exc {

    public static void main(String[] args) {
        CuentaBancaria cuenta = new CuentaBancaria("767675", "Manuel Limachi", 1000);

        cuenta.mostrarInfo();

        try {
            cuenta.depositar(500);
            cuenta.mostrarInfo();
        } catch (Exception e) {
            System.out.println("Error al depositar: " + e.getMessage());
        }
        
        try {
            cuenta.depositar(-150);
        } catch (Exception e) {
            System.out.println("Error al depositar: " + e.getMessage());
        }

        try {
            cuenta.retirar(300);
            cuenta.mostrarInfo();
        } catch (Exception e) {
            System.out.println("Error al retirar: " + e.getMessage());
        }
        try {
            cuenta.retirar(5000);
        } catch (Exception e) {
            System.out.println("Error al retirar: " + e.getMessage());
        }
    }
}
    

  
