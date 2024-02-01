import numpy as np
import matplotlib.pyplot as plt
import sympy as sp


# Define the potential energy function
def U(r):
    return ((r - 1) * (r + 2) * (r - 3))**2 - 8.0 + r


def plot_U(r_values, u_values):
    plt.plot(r_values, u_values, label='Potential Energy Function')
    plt.title('Potential Energy Function U(r)')
    plt.xlabel('r')
    plt.ylabel('U(r)')
    plt.legend()
    plt.grid(True)
    plt.show()


def calculate_derivative(r, h=1e-6):
    return (U(r + h) - U(r - h)) / (2 * h)


def calculate_second_derivate(r, h=1e-5):
    return (U(r + h) - 2 * U(r) + U(r - h)) / (h**2)


def steepest_descent_method(r_initial, alpha, iterations):
    r = r_initial

    # Steepest Descent method
    for i in range(iterations):
        derivative_U = calculate_derivative(r)
        r -= alpha * derivative_U

    return r


def newton_raphson_method(r_initial, iterations):
    r = r_initial

    # Newton-Raphson method
    for i in range(iterations):
        derivative_U = calculate_derivative(r)
        second_derivative_U = calculate_second_derivate(r)
        r -= derivative_U / second_derivative_U

    return r


# Generate values for 'r' in the given range
r_values = np.linspace(-2.5, 3.5, 1000)
u_values = U(r_values)
plot_U(r_values, u_values)


r_initial = np.linspace(-2.5, 3.5, 1000)
alpha = 0.001
iterations = 100
unique_minima = set()
for r_ in r_initial:
    minima = steepest_descent_method(r_, alpha, iterations)
    # print("Minimum found using Steepest Descent method:", minima)
    unique_minima.add(round(minima, 4))

for minima in unique_minima:
    print("Unique minima:", minima)


# Newton-Raphson method
iterations = 100
unique_minima = set()
for r_ in r_initial:
    minima = newton_raphson_method(r_, iterations)
    # print("Minimum found using Newton-Raphson method:", minima)
    unique_minima.add(round(minima, 4))
print("------------------------")
print("Newton-Raphson method")
print("------------------------")
for minima in unique_minima:
    print("Unique minima:", minima)

