import numpy as np


def prep_1_1():
    return np.arange(0, 100 + 1)


def prep_1_2():
    return np.arange(1, 100, 2)


def prep_1_3():
    return np.sum(np.arange(0, 100 + 1))


def prep_1_4():
    return np.sum(np.arange(1, 100, 2))


def is_prime(prime_buffer: list[int], n: int) -> bool:
    if n != 2:
        # IMPROVEMENT: no need to check if prime > sqrt(n)
        for prime in prime_buffer:
            if n % prime == 0:
                return False

    return True


def prep_1_5(target=1000) -> list[int]:
    primes = []

    for n in range(2, target + 1):
        if is_prime(primes, n):
            primes.append(n)

    return primes


def prep_1_6(target=1000) -> list[int]:
    primes = []

    n = 2

    while len(primes) < target:
        if is_prime(primes, n):
            primes.append(n)
        n += 1

    return primes


def prep_1_7(end=100) -> float:
    current = 1.0

    for _ in range(1, end + 1):
        current = current / 2 + 1 / current

    return current


def prep_1_8(epsilon=1e-10) -> int:
    current = 1.0
    n = 1

    while True:
        next = current / 2 + 1 / current

        if np.abs(next - current) < epsilon:
            return n

        current = next
        n += 1


if __name__ == "__main__":
    print(prep_1_1())
    print(prep_1_2())
    print(prep_1_3())
    print(prep_1_4())
    print(prep_1_5())
    print(prep_1_6())
    print(prep_1_7())
    print(prep_1_8())
