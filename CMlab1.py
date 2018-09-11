from math import *


def task1_1():
    x = 1
    while x:
        print('x = ' + str(x) + '  x/2 = ' + str(x/2))
        x /= 2


def task1_2():
    x = 1
    while 1 + x/2 > 1:
        print('1 + x = ' + str(1 + x / 2))
        x = x/2
    print(x)


def task2():
    x = 2
    while x > 1:
        x = sqrt(x)
        print("sqrt(x) = " + str(x))

def ExpSum(x):
    #if(x < 0): return 1 / ExpSum(-x)
    s = 0
    k = 0
    while (s + (x ** k) / factorial(k)) != s:
        s += (x ** k) / factorial(k)
        k += 1
    return s


def task2_1():
    inp = [i for i in range(51) if i % 10 == 0]
    for i in inp:
        print('Test for ' + str(i) + ': ' + str(ExpSum(i)) + ' and '
              + str(exp(i)) + '\nErr: ' + str(abs(ExpSum(i) - exp(i))))


def task2_2():
    inp = [-i for i in reversed(range(51)) if i % 10 == 0]
    for i in inp:
        print('Test for ' + str(i) + ': ' + str(ExpSum(i))
              + ' and ' + str(exp(i)) + '\nErr: ' + str(abs(ExpSum(i) - exp(i))))


def CosSum(x):
    if(x < 0): return 1 / CosSum(-x)
    s = 0
    k = 0
    while s + (-1 ** k * x ** (2*k)) / factorial(2 * k) != s:
        s += (-1 ** k * x ** (2*k)) / factorial(2 * k)
        k += 1
    return s


def CosSumFixed(x):
    if x < 0: return CosSumFixed(-x)
    t = int(x/2/pi)
    x -= float(t)*pi*2
    s = 0
    a = 1
    k = 1
    while s + a != s:
        s += a
        a = -a*x*x/((2*k-1)*(2*k))
        k += 1
    return s


def task2_3():
    inp = [i for i in range(51) if i % 5 == 0]
    for i in inp:
        print('Test for ' + str(i) + ': \n' + 'CosSum = ' + str(CosSum(i)) + '\nFixed CosSum = '
              + str(CosSumFixed(i)) + '\nMath.cos = ' + str(cos(i)) + '\nErr: ' + str(abs(CosSum(i) - cos(i)))+ '\n')


def Ek(x, eps=10 ** -7):
    if x == 1: return exp(-1) + eps
    return 1 - x * Ek(x-1, eps)


def task3_1():
    inp = list(range(1, 21))
    eps = [0, 10 ** -7, 10 ** -6, 10 ** -5]
    for i in eps:
        print('\nEk for eps = ' + str(i))
        for j in inp:
            print('E(' + str(j) + ') = ' + str(Ek(j, i)))


def Ekm(k, ekm, m=30):
    if k == m: return ekm
    return (1 - Ekm(k+1, ekm))/(k + 1)


def task3_2():
    inp = list(range(1,31))
    ekm = [0, 10 ** -2, 10 ** -1, 1]
    for i in ekm:
        print('\nEk for ekm = ' + str(i))
        for j in inp:
            print('E(' + str(j) + ') = ' + str(Ekm(j, i)))


def L(i):
    s = 1
    for j in range(1,21):
        if i != j:
            s *= (i-j)
    return i**19/s


def Dx(i, Da=10**-7):
    return L(i) * Da


def P(x):
    for i in range(1,21):
        pass
task3_2()
