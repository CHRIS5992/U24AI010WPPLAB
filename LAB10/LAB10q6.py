import numpy as np
import matplotlib.pyplot as plt
import random

def f(x):
    return x**3 - 6*x**2 + 11*x - 6

def find_initial_interval():
    while True:
        a = random.uniform(0, 5)
        b = random.uniform(0, 5)
        if a > b:
            a, b = b, a
        if f(a) * f(b) < 0:
            return a, b

def bisection_method(f, a, b, tol=1e-5, max_iter=100):
    history = []
    for _ in range(max_iter):
        c = (a + b) / 2
        history.append(c)
        if abs(f(c)) < tol or (b - a) / 2 < tol:
            break
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return np.array(history)

a, b = find_initial_interval()
history = bisection_method(f, a, b)

x_vals = np.linspace(0, 5, 400)
y_vals = f(x_vals)

plt.plot(x_vals, y_vals, label='f(x)')
plt.axhline(0, color='black', linewidth=0.5)
plt.plot(history, f(history), 'ro-', label='Bisection steps')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Bisection Method Root Finding')
plt.legend()
plt.grid(True)
plt.show()
