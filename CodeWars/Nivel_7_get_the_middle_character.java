public class Nivel_7_get_the_middle_character {
    public static String getMiddle(String s) {
        int middle = s.length() / 2;
        if (s.length() % 2 == 0) {
            return s.substring(middle - 1, middle + 1);
        } else {
            return s.substring(middle, middle + 1);
        }
    }
}
