import matplotlib.pyplot as plt
import numpy as np
import tabulate as tab


def konvergence_order(f, x_bar, h):
    return np.log2(
        np.abs(
            (f(x_bar + h) - f(x_bar + h / 2)) / (f(x_bar + h / 2) - f(x_bar + h / 4))
        )
    )


def richardson_hat(f, x_bar, h):
    return (f(x_bar + h) * f(x_bar + h / 4) - f(x_bar + h / 2) ** 2) / (
        f(x_bar + h) - 2 * f(x_bar + h / 2) + f(x_bar + h / 4)
    )


def limited_approx(approximator, f, x_bar, h, tolerance, max_iter, expected):
    i = 0
    current_approx = approximator(f, x_bar, h)

    result_buffer = []

    while i < max_iter:
        result_buffer.append([i, h, current_approx, np.abs(expected - current_approx)])

        h /= 2
        i += 1

        next_r = approximator(f, x_bar, h)

        if np.abs(next_r - current_approx) < tolerance:
            result_buffer.append([i, h, next_r, np.abs(expected - next_r)])
            return result_buffer

        current_approx = next_r


def ordinary_derivative(f, x_bar, h):
    return (f(x_bar + h) - f(x_bar)) / h


def symmetric_derivative(f, x_bar, h):
    return (f(x_bar + h) - f(x_bar - h)) / (2 * h)


def richardson_derivative(f, x_bar, h):
    return (
        4 * symmetric_derivative(f, x_bar, h / 2) - symmetric_derivative(f, x_bar, h)
    ) / 3


def part_2_1():
    def present_richardson(f, x_bar, h, expected):
        values = richardson_hat(f, x_bar, h)
        err = np.abs(values - expected)
        r = konvergence_order(f, x_bar, h)
        print(tab.tabulate(zip(h, r, values, err), headers=["h", "r", "r_hat", "err"]))

    h_range = lambda n: 0.1 / 2 ** np.arange(0, n)

    f = lambda x: (1 + x) ** (1 / x)
    present_richardson(f, 0, h_range(4), np.e)

    g = lambda x: (np.e ** np.sqrt(x) - 1) / np.sqrt(x)
    present_richardson(g, 0, h_range(10), 1)


def part_2_2():
    f = lambda x: (2**x - 1) / x
    results = limited_approx(richardson_hat, f, 0, 1, 10e-5, 20, np.log(2))
    print(tab.tabulate(results, headers=["i", "h", "r_hat", "err"]))


def part_2_3():
    def append_err_plot(derivator, f, x_bar, h, expected, ax, label):
        values = derivator(f, x_bar, h)
        errors = np.abs(values - expected)
        ax.loglog(h, errors, label=label)

    f = lambda x: np.e**x
    h = 10.0 ** (-np.arange(1, 15))

    _fig, ax = plt.subplots()
    ax.set_xlabel("h")
    ax.set_ylabel("err")
    ax.grid(True)

    append_err_plot(ordinary_derivative, f, 0, h, 1, ax, "Ordinary Derivative")
    append_err_plot(symmetric_derivative, f, 0, h, 1, ax, "Symmetric Derivative")
    # Extra:
    # append_err_plot(richardson_derivative, f, 0, h, 1, ax, "Richardson Derivative")

    ax.legend()

    plt.show()


def part_2_4():
    f = lambda x: np.e**-x * np.sin(x)

    results = limited_approx(
        richardson_derivative, f, 1, 0.1, 10e-10, 10, -0.11079376530669924
    )

    print(tab.tabulate(results, headers=["i", "h", "r_dev", "err"]))


if __name__ == "__main__":
    part_2_1()
    part_2_2()
    part_2_3()
    part_2_4()
