import matplotlib.pyplot as plt
from math import cos, pi
import numpy as np
import random

x = [-2, -1, 1, 1.5, 2, 3]
y = [-1.5, 1.2, -1.3, 2, -1, -2]


def calculate_s(x, y, h, s1=None, s2=None):

    n = len(x)

    # a, b, c - коэффициеты перед x_i-1, x_i, x_i+1
    a = [0.0]
    b, c, f = [], [], []
    if s1 is None or s2 is None:
        b.append(1.0)
        c.append(-1.0)
        f.append(0.0)
    elif s1==0 and s2==0:
        b.append(1.0)
        c.append(0.0)
        a.append(0.0)
        f.append(0.0)
    else:
        b.append(2.0)
        c.append(1.0)
        f.append(6.0 * ((y[1] - y[0]) / h[1] ** 2 - s1 / h[1] ** 2))
    for i in (range(1, n - 1)):
        a.append(h[i])
        b.append(2.0 * (h[i] + h[i + 1]))
        c.append(h[i + 1])
        f.append((6.0 * ((y[i + 1] - y[i]) / h[i + 1] - (y[i] - y[i - 1]) / h[i])))

    if s1 is None or s2 is None:
        b.append(-1.0)
        f.append(0.0)
        a.append(1.0)
        c.append(0.0)
    elif s1 == 0 and s2 == 0:
        a.append(0.0)
        b.append(1.0)
        c.append(0.0)
        f.append(0.0)
    else:
        b.append(2.0)
        f.append(-6.0 * ((y[n - 1] - y[n - 2]) / h[n - 1] ** 2 - s2 / h[n - 1] ** 2))
        a.append(1.0)
        c.append(0.0)
    print('A,B,C,F')
    print(a)
    print(b)
    print(c)
    print(f)
    return resolve_tridiagonal_matrix(a, b, c, f)


def resolve_tridiagonal_matrix(a, b, c, f):
    n = len(f)
    s = n * [None]
    p = [0, -c[0] / b[0]]
    q = [0, f[0] / b[0]]
    for i in range(1, n - 1):
        k = b[i] + a[i] * p[i]
        p.append(-c[i] / k)
        q.append((f[i] - a[i] * q[i]) / k)

    s[n-1] = ((-a[n - 1] * q[n - 1] + f[n - 1]) / (b[n - 1] + a[n - 1] * p[n - 1]))

    for i in range(n-1, 0, -1):
        s[i - 1] = p[i] * s[i] + q[i]

    return s


def calculate_value_at_point_x(point_x, x, y, s, h):
    i = 1
    while i < len(x) and point_x > x[i]:
        i += 1

    return (s[i - 1] * (x[i] - point_x)**3 + s[i] * (point_x - x[i - 1])**3) / (6.0 * h[i]) \
        + (point_x - x[i - 1]) * (y[i]/h[i] - h[i]*s[i]/6.0) \
        + (x[i] - point_x) * (y[i-1]/h[i] - h[i]*s[i-1]/6.0)

def task1():
    print("Resolve system:")
    print(resolve_tridiagonal_matrix(a, b, c, f))
    s = calculate_s(x, y, h, -2, 1)

    xp = np.linspace(np.min(x), np.max(x), 1000)
    calculator = lambda t: calculate_value_at_point_x(t, x, y, s, h)
    yp = np.vectorize(calculator)(xp)

    plt.plot(xp, yp, c='r')
    plt.plot(x, y, 'go', color='yellow', marker='h', markeredgecolor='red')
    plt.grid(True)
    plt.show()


def task2():
    h = np.repeat([2.0 / (l - 1)], l)
    s = calculate_s(x_lin, y_lin, h, 0, 0)
    print(s)
    vector_natural_calculator = np.vectorize(lambda t: calculate_value_at_point_x(t, x_lin, y_lin, s, h))

    xp = np.linspace(-1, 1, 100000)
    yp = vector_natural_calculator(xp)

    plt.plot(xp, yp, c='black')
    plt.scatter(x_lin, y_lin, c='y')
    plt.grid(True)
    plt.show()


def task3():
    h = np.repeat([2.0 / (l - 1)], l)
    s = calculate_s(x_lin, y_lin, h)
    print("sol:")
    print(s)
    quadratic_calculator = np.vectorize(lambda t: calculate_value_at_point_x(t, x_lin, y_lin, s, h))
    xp = np.linspace(-1, 1, 100000)
    yp = quadratic_calculator(xp)

    plt.plot(xp, yp, color='green')
    plt.plot(x_lin, y_lin, 'go', color='red', marker='x')
    plt.grid(True)

    plt.show()



h = [0]
a = [0, 3, 1, 1]
b = [5, 6, 4, -3]
c = [3, 1, -2, 0]
f = [8, 10, 3, -2]

for i in range(1, len(x)):
    h.append(x[i] - x[i - 1])

l = 6
x_lin = np.linspace(-1, 1, l)
y_lin = np.random.random_sample((l,))
y_lin = y

#task1() #s1 = -2 s2 = 1
#task2() #s1 = 0 s2 = 0
task3() #s1,s2 is unknown


