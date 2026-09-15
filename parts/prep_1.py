import matplotlib.pyplot as plt
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


def prep_2_1(test_x: list[int], test_y: list[int]):
    f = lambda x: (1 + x) / (2 + x)
    f_inv = lambda x: (2 * x - 1) / (1 - x)

    for x in test_x:
        assert x != 2
        np.testing.assert_approx_equal(f_inv(f(x)), x)

    for y in test_y:
        assert y != 1
        np.testing.assert_approx_equal(f(f_inv(y)), y)


def prep_2_2():
    f = lambda x: x**2 - 1
    g = lambda x: x + 1
    h = lambda x: f(g(x))

    return h(3)


def prep_2_3():
    def plot_impl(lambdas):
        x = np.linspace(0.1, np.pi, 1000)
        for i, f in enumerate(lambdas):
            plt.plot(x, f(x), linewidth=i + 1)

        plt.show()

    a = lambda x: np.sin(np.exp(x))
    # x > 0
    b = lambda x: np.sin(np.log(x))
    c = lambda x: np.exp(np.sin(x))
    # sin(x) > 0 --> x < pi
    d = lambda x: np.log(np.sin(x))

    plot_impl([a, b, c, d])


if __name__ == "__main__":
    print(prep_1_1())
    print(prep_1_2())
    print(prep_1_3())
    print(prep_1_4())
    print(prep_1_5())
    print(prep_1_6())
    print(prep_1_7())
    print(prep_1_8())

    prep_2_1([1, 4, 5, -20], [2, 4, 10, -20])
    print(prep_2_2())
    prep_2_3()
