public class Matematicas {

    public static void main(String[] args) {
        
        int n = 2, m = 4;

        double resultado = Math.pow(n, m);
        double raiz = Math.sqrt(resultado);

        System.out.println(resultado);
        System.out.println(raiz);
        System.out.println(Math.PI);


        double aleatorio = (int)(Math.random()*10+1);

        System.out.println(aleatorio);
    }
    
}
