"""
Simple, given a string of words, return the length of the shortest word(s).

String will never be empty and you do not need to account for different data types.
"""

def find_short(s):
    words = s.split()
    smallest = float('inf')
    for word in words:
        count = 0
        for letter in word:
            count += 1
        if smallest > count:
            smallest = count
    return smallest

def find_short(s):
    return min(len(word) for word in s.split())

def find_short(s):
    return len(min(s.split(), key = len))

print(find_short("Let's travel abroad shall we"))