#Primo
def es_primo(x):
    if x <= 1:
        return False
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return False
    return True

#Fibonacci
def es_fibonacci(x):
    if x < 0:
        return False
    a, b = 0, 1
    while a < x:
        a, b = b, a+b
    return a == x

#Factorial
def calcular_factorial(x):
    factorial = 1
    for i in range(1, x+1):
        factorial *= i
    return factorial

def factorial_recursivo(x):
    if x == 0:
        return 1
    else:
        return x * factorial_recursivo(x-1)

#Potencia
def calcular_potencia(a, b):
    return a**b

def potencia_recursiva(a, b):
    if b == 0:
        return 1
    else:
        return a * potencia_recursiva(a, b-1)