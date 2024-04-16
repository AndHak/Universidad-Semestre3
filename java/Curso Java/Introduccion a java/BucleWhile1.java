import java.util.Scanner;

public class BucleWhile1 {
    
    public static void main(String[] args) {
        
        Scanner teclado = new Scanner(System.in);

        int num = 0;
        System.out.println("Introduce un numero distinto de cero");
        num = teclado.nextInt();

        while (num != 0) {
            System.out.println("Introduce un numero distinto de cero");
            num = teclado.nextInt();
        }

        int num2 = 0;
        do {
            System.out.println("Introduce un numero no par");
            num2 = teclado.nextInt();

        } while (num2 % 2 != 0);
            

        teclado.close();
    }
}
