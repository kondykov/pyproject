import numpy as np
import matplotlib.pyplot as plt
import selenium as sel
import requests


def f(x):
    return np.sin(x) - 0.5


def chord_method(f, a, b, tolerance=1e-6, max_iter=100):
    x0 = a
    x1 = b
    iter_count = 0

    while abs(f(x1)) > tolerance and iter_count < max_iter:
        x2 = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
        x0 = x1
        x1 = x2
        iter_count += 1

    return x1, iter_count


def visualize_chord_method():
    # Ввод начальных приближений от пользователя
    a = float(input("Введите начальное приближение a: "))
    b = float(input("Введите начальное приближение b: "))

    # Находим корень уравнения методом хорд
    root, iterations = chord_method(f, a, b)

    # График функции и отрезка хорды на интервале [0, 𝜋]
    x = np.linspace(0, np.pi, 100)
    y = f(x)

    plt.plot(x, y, label='f(x) = sin(x) - 0.5')
    plt.axhline(y=0, color='k', linestyle='--')
    plt.scatter([a, b], [f(a), f(b)], color='red', label='Начальные приближения')
    plt.plot([a, b], [f(a), f(b)], color='red', linestyle='--', label='Интервал хорды')
    plt.scatter(root, f(root), color='green', label='Корень')
    plt.title('График функции и метод хорд')
    plt.legend()
    plt.grid(True)
    plt.show()

    # Вывод найденного корня и количества итераций
    print(f"Найденный корень: {root}")
    print(f"Количество итераций: {iterations}")


if __name__ == "__main__":
    visualize_chord_method()
