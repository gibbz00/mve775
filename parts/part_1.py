import matplotlib.pyplot as plt
import numpy as np


def part_1_1():
    def approximateSqrt(num: int, epsilon: float) -> float:
        assert num >= 1
        assert epsilon > 0

        lower = 1
        upper = num
        approx = float(num)

        while np.absolute(approx**2 - num) >= epsilon:
            approx = (lower + upper) / 2

            if approx**2 < num:
                lower = approx
            else:
                upper = approx

        return approx

    print(approximateSqrt(1, 1e-10))
    print(approximateSqrt(2, 1e-10))
    print(approximateSqrt(9, 1e-10))
    print(approximateSqrt(121, 1e-10))


def part_1_2(f, a: float, b: float, n: int):
    assert n > 0
    x = np.linspace(a, b, n)
    return plt.plot(x, f(x))


def part_1_3():
    f = lambda x: np.sin(x) * np.cos(x**2)
    min = -5 * np.pi
    max = -min

    (line,) = part_1_2(f, min, max, 1000)

    line.set_color("green")
    plt.title("f(x) = sin(x) * cos(x^2)")
    plt.grid()
    plt.axis("equal")
    plt.ylabel("y")
    plt.xlabel("x")

    plt.show()


if __name__ == "__main__":
    part_1_1()
    part_1_3()
