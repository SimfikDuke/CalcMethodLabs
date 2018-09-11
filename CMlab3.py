import pylab
import random
from matplotlib import mlab


def hermit(x, a, b, fa, fb, dfa, dfb):
    h = b-a
    k = (x-a)/h
    res = (1-3*k**2+2*k**3)*fa+(3*k**2-2*k**3)*fb+h*(k-2*k**2+k**3)*dfa+h*(-k**2+k**3)*dfb
    return res


def task():
    a = -1
    b = 1
    fa = random.uniform(-1, 1)
    fb = random.uniform(-1, 1)
    dfb = random.uniform(-1, 1)
    x = mlab.frange(-1, 1, 0.01)
    for i in range(2):
        for j in range(3):
            dfa = random.uniform(-1.0, 1.0)
            y = [hermit(i, a, b, fa, fb, dfa, dfb) for i in x]
            pylab.subplot(2, 3, i*3+j+1)
            pylab.title('f\'(a)=%.2f  f\'(b) = %.2f' % (dfa, dfb))
            pylab.grid(True)
            pylab.plot(x, y)


def df(x):
    return (-24*x)/((12*x**2+1)**2)


def f(x):
    return 1/(1+12*x**2)


def task2():
    x = mlab.frange(-1, 1, 0.1)
    pylab.grid(True)
    for i in range(len(x)-1):
        a = x[i]
        b = x[i+1]
        x_local = mlab.frange(a, b, 0.01)
        y_local = [hermit(j, a, b, f(a), f(b), df(a), df(b)) for j in x_local]
        pylab.plot(x_local, y_local)


task()
pylab.show()
pylab.plot(mlab.frange(-1, 1, 0.01), [f(i) for i in mlab.frange(-1, 1, 0.01)])
task2()
pylab.show()