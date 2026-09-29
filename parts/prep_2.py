from collections.abc import Callable

import numpy as np


def konvergence_order(f: Callable[[float], float], x_hat: float, h: float) -> float:
    return np.log2(
        np.abs(
            (f(x_hat + h) - f(x_hat + h / 2)) / (f(x_hat + h / 2) - f(x_hat + h / 4))
        )
    )


def richardson(f: Callable[[float], float], x_hat: float, r: float, h: float) -> float:
    return (2**r * f(x_hat + h / 2) - f(x_hat + h)) / (2 * r - 1)


def richardson_hat(f: Callable[[float], float], x_hat: float, h: float) -> float:
    r = konvergence_order(f, x_hat, h)
    return richardson(f, x_hat, r, h)


def prep_1() -> float:
    f = lambda x: (1 - np.cos(3 * x)) / (x * np.sin(x))
    return richardson(f, 0, 2, 1e-5)


def prep_2() -> float:
    f = lambda x: np.cos(x) + (x * 2) / 2
    return richardson_hat(f, 0, 1e-5)


if __name__ == "__main__":
    print(prep_1())
    print(prep_2())
