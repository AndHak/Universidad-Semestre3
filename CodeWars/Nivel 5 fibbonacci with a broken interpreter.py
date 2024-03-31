"""
Oh no!!
You dropped your interpreter!?
That didn't sound so good...

Write a function that returns the Nth fibonacci number.
The use of the character "(" and the words "while", "for" and "gmpy2" has been disabled (broken).
You may only use up to 1000 letters in your solution.

The use of one "(" is permited for the line "def fibo(..."
it will only exactly work in that line and only once.
feel free not to use it :)

For your convenience the recursion limit has been raised.
No test will be over 200 away from the last one starting at 0 and ending at around 5,000.

The fibonacci sequence is defined as:
"""

fibo = lambda n, a=0, b=1: a if n == 0 else fibo(n-1, b, a+b)

print(fibo(1)) #1
print(fibo(3)) #2
print(fibo(5)) #5
print(fibo(10)) #55
print(fibo(100)) #354224848179261915075
