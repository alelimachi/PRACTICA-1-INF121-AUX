package main6exc;

public class CuentaBancaria {
    private String numeroCuenta;
    private String titular;
    private double saldo;

    public CuentaBancaria(String numeroCuenta, String titular, double saldo) {
        this.numeroCuenta = numeroCuenta;
        this.titular = titular;
        this.saldo = saldo;
    }

    public void depositar(double monto) throws IllegalArgumentException {
        if (monto <= 0) {
            throw new IllegalArgumentException("El monto del deposito debe ser positivo.");
        }
        saldo += monto;
    }

    public void retirar(double monto) throws IllegalArgumentException, FondosInsuficientesException {
        if (monto <= 0) {
            throw new IllegalArgumentException("El monto a retirar debe ser positivo.");
        }

        if (monto > saldo) {
            throw new FondosInsuficientesException("Fondos insuficientes.");
        }

        saldo -= monto;
    }

    public void mostrarInfo() {
        System.out.println("Número de cuenta: " + numeroCuenta);
        System.out.println("Titular: " + titular);
        System.out.println("Saldo actual: " + saldo);
    }
}
    
