"""
Create an endless generator that yields prime numbers. the generator must be able to produce a million primes in a few seconds
"""


def generate_primes(n):
    is_prime = [True] * (n + 1) 
    is_prime[0] = is_prime[1] = False 
    
    i = 2
    while i * i <= n:
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
        i += 1

    return [x for x in range(n + 1) if is_prime[x]]

class Primes:
    n = 16000000
    all_primes = generate_primes(n)
    
    @staticmethod
    def stream():
        yield from Primes.all_primes


generate_primes(16000000)