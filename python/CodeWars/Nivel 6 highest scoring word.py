"""
Given a string of words, you need to find the highest scoring word.

Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.

For example, the score of abad is 8 (1 + 2 + 1 + 4).

You need to return the highest scoring word as a string.

If two words score the same, return the word that appears earliest in the original string.

All letters will be lowercase and all inputs will be valid."""

def high(x):
    letters = "abcdefghijklmnopqrstuvwxyz"
    highest = 0
    highest_word = ""
    for word in x.split():
        score = 0
        for letter in word:
            score += letters.index(letter)+1
        if score > highest:
            highest = score
            highest_word = word

    return highest_word

print(high('man i need a taxi up to ubud'))