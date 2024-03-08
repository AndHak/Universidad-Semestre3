public class Cadenas {

    public static void main(String[] args) {
        
        String cadena = "Curso Java";

        System.out.println(cadena.length());

        int longitud = cadena.length();

        System.out.println(cadena + " tiene " + longitud + " letras.");

        char primera_letra = cadena.charAt(0);

        System.out.println("La primera letra es: " + primera_letra);

        String cadena_mayusculas = cadena.toUpperCase();

        System.out.println("toUpperCase: " + cadena_mayusculas);

        System.out.println("toLowerCase: " + cadena_mayusculas.toLowerCase());
    }
    
}
