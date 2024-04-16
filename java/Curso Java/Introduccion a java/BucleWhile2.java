import java.util.Scanner;

public class BucleWhile2 {
    public static void main(String[] args) {

        Scanner teclado = new Scanner(System.in);

        System.out.println("Suma de fibonaccis");
        int suma = 0;
        int num = 0;
        System.out.println("Introduce un numero fibonacci (0 para cancelar):");
        num = teclado.nextInt();

        while (num != 0) {
            if (num < 0) {
                System.out.println("No digite numeros negativos");
            }
            else {
                int a = 0;
                int b = 1;
                int secuencia = 1;
                while (secuencia <= num) {
                    if (secuencia == num) {
                        suma += num;
                        break;
                    }
                    secuencia = a + b;
                    a = b;
                    b = secuencia;
                }
            } 
            System.out.println("Introduce un numero fibonacci (0 para cancelar):");
            num = teclado.nextInt();

        }
        
        System.out.println("La suma es: "+suma);
        teclado.close();
    }
}
