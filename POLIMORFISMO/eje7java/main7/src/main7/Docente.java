
package main7;

class Docente extends Persona {
    public double sueldo;
    public String regProfesional;

    public Docente(String nombre, String paterno, String materno, int edad, double sueldo, String regProfesional) {
        super(nombre, paterno, materno, edad);
        this.sueldo = sueldo;
        this.regProfesional = regProfesional;
    }

    @Override
    public void mostrar() {
        super.mostrar();
        System.out.println("Sueldo: " + sueldo);
        System.out.println("Reg. Profesional: " + regProfesional);
    }
}

