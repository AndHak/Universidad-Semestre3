public class CondicionesSwitch {

    public static void main(String[] args) {

        int x = 3;

        switch (x) {
            case 1:
            case 2:
            case 3:
                System.out.println("El valor de x esta entre 1 y 3");
                break;
            case 4:
            case 5:
                System.out.println("El valor esta entre 4 y 6");
                break;
            default:
                System.out.println("El valor es mayor que 6");

        }

    }
    
}
