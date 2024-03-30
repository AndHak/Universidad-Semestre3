import java.util.ArrayList;
import java.util.List;

public class Nivel3PrimeStreaming {
    private static boolean[] generatePrimes(int n) {
        boolean[] isPrime = new boolean[n + 1];
        for (int i = 2; i <= n; i++) {
            isPrime[i] = true;
        }
        isPrime[0] = isPrime[1] = false;
        
        int i = 2;
        while (i * i <= n) {
            if (isPrime[i]) {
                for (int j = i * i; j <= n; j += i) {
                    isPrime[j] = false;
                }
            }
            i++;
        }
        
        return isPrime;
    }
    
    private static List<Integer> generatePrimesList(int n) {
        boolean[] isPrime = generatePrimes(n);
        List<Integer> primes = new ArrayList<>();
        for (int i = 0; i <= n; i++) {
            if (isPrime[i]) {
                primes.add(i);
            }
        }
        return primes;
    }
    
    public static List<Integer> stream() {
        int n = 16000000;
        return generatePrimesList(n);
    }
}
