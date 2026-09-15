import matplotlib.pyplot as plt
import numpy as np


def test_2(months: list[tuple[str, list[float]]]):
    _fig, ax = plt.subplots()
    ax.set_xlabel("Day")
    ax.set_ylabel("Temp")

    for name, temps in months:
        ax.plot(range(len(temps)), temps, label=name)

    ax.legend()

    plt.show()


# Reciprokfunktionen: y = 1/x
def test():
    x = np.arange(1, 10, 0.1, dtype=np.float64)
    y = np.reciprocal(x)
    _fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set_title("Reciprocal")
    plt.show()


if __name__ == "__main__":
    test()
    test_2([])
