public class Nivel_6_highest_scoring_word {
    public static String high(String x) {
        String letters = "abcdefghijklmnopqrstuvwxyz";
        int highest = 0;
        String highestWord = "";

        String[] words = x.split("\\s+");
        for (String word : words) {
            int score = 0;
            for (char letter : word.toCharArray()) {
                score += letters.indexOf(letter) + 1;
            }
            if (score > highest) {
                highest = score;
                highestWord = word;
            }
        }

        return highestWord;
    }

}
