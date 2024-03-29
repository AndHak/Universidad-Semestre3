"""
A Hamming number is a positive integer of the form 2i3j5k, for some non-negative integers i, j, and k.

Write a function that computes the nth smallest Hamming number.

Specifically:

The first smallest Hamming number is 1 = 203050
The second smallest Hamming number is 2 = 213050
The third smallest Hamming number is 3 = 203150
The fourth smallest Hamming number is 4 = 223050
The fifth smallest Hamming number is 5 = 203051
The 20 smallest Hamming numbers are given in the Example test fixture.
"""

def hamming(n):
    i, j, k = 0, 0, 0
    hamming_numbers = [1]
    
    while len(hamming_numbers) < n:
        next_hamming = min(hamming_numbers[i] * 2, hamming_numbers[j] * 3, hamming_numbers[k] * 5)
        hamming_numbers.append(next_hamming)
        
        if next_hamming == hamming_numbers[i] * 2:
            i += 1
        if next_hamming == hamming_numbers[j] * 3:
            j += 1
        if next_hamming == hamming_numbers[k] * 5:
            k += 1
            
    return hamming_numbers[-1]


print(hamming(1))
print(hamming(2))
print(hamming(3))
print(hamming(4))
print(hamming(5))
print(hamming(10))
print(hamming(11))
print(hamming(12))
        

