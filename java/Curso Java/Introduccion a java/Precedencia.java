public class Precedencia {

    public static void main(String[] args) {
        
        int n = 2;
        int m = n++*3+2+(++n);

        System.out.println(m);

        n = 2;

        int x = ++n+2+3*n++;

        System.out.println(x);

    }
    
}
