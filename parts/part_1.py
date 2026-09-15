import numpy as np


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


def part_1_1():
    print(approximateSqrt(1, 1e-10))
    print(approximateSqrt(2, 1e-10))
    print(approximateSqrt(9, 1e-10))
    print(approximateSqrt(121, 1e-10))


if __name__ == "__main__":
    part_1_1()
