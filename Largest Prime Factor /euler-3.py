import math


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def largest_prime_factor(n):
    largest_prime = -1

    while n % 2 == 0:
        largest_prime = 2
        n = n // 2

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            largest_prime = i
            n = n // i

    if n > 2:
        largest_prime = n

    return largest_prime


print("###############################")
print("Largest prime factor:", largest_prime_factor(600851475143))
