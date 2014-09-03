from math import sqrt

def euler1():
    """Find the sum of all numbers under 1,000 divisible by 3 or 5"""
    total = 0
    for i in range(1000):
        if i % 3 == 0 or i % 5 == 0:
            total += i
    return total

def euler2():
    """Find all even Fibonacci numbers under 4,000,000"""
    a, b, total = 0, 1, 0
    while b < 4000000:
        if b % 2 == 0:
            total += b
        a, b = b, a + b
    return total

def euler3():
    """Find the largest prime factor of the number 600851475143"""
    n = 600851475143
    i, fact = 3, 0
    while i <= n:
        if n % i == 0:
            n /= i
            fact = i
        i += 2
    return fact

def euler4():
    """Find the largest palindrome formed by the product
    of two three-digit numbers"""
    largest = 0
    for i in range(900, 1000):
        for j in range(900, 1000):
            n = i * j
            if str(n) == str(n)[::-1] and n > largest:
                largest = n
    return largest

def euler_main():
    print(euler1())
    print(euler2())
    print(euler3())
    print(euler4())
    return "Done"