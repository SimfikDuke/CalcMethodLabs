import math
import pylab
import random
from matplotlib import mlab
var = 7

def lagr1(x, lx, ly):
    y = 0
    for i in range(len(lx)):
        addi = 1
        for j in range(len(lx)):
            if i != j:
                addi *= (x - lx[j])/(lx[i] - lx[j])
        y += ly[i] * addi
    return y


def task1():
    rndx = [-1, -0.5, 0, 0.5, 1]
    rndy = [random.uniform(0,1) for i in range(5)]
    rndlagrx = mlab.frange(-1, 1, 0.01)
    rndlagry = [lagr1(x, rndx, rndy) for x in rndlagrx]
    pylab.subplot(2, 3, 1)
    pylab.title('1.1')
    pylab.grid(True)
    pylab.plot(rndlagrx, rndlagry, color='green')
    pylab.plot(rndx, rndy, 'go', color='red', marker='x')

def task2a(n=4):
    h = 2/n
    lagrx = [-1 + i*h for i in range(n)]
    lagry = [1/(1 + (10 + var) * x**2) for x in lagrx]
    xlist = mlab.frange(-1, 1, 0.01)
    ylist = [lagr1(x,lagrx,lagry) for x in xlist]
    pylab.subplot(2, 3, 2)
    pylab.plot(xlist, ylist, color='cyan')
    pylab.plot(xlist, [1/(1 + (10 + var) * x**2) for x in xlist], ':', color='blue')
    pylab.title(r'1.2(a)')
    pylab.grid(True)
    pylab.plot(lagrx, lagry, 'go', color='yellow', marker='h',markeredgecolor='red')

def task2b(n=10):
    N = 2 * (n + 1)
    lagrx = [(((2*i)+1)*math.pi/N) for i in range(n)]
    lagry = [1/(1 + (10 + var) * x**2) for x in lagrx]
    xlist = mlab.frange(-1, max(lagrx), 0.01)
    ylist = [lagr1(x, lagrx, lagry) for x in xlist]
    pylab.subplot(2, 3, 3)
    pylab.plot(xlist, ylist, color='purple')
    pylab.title(r'1.2(b)')
    pylab.grid(True)
    pylab.plot(xlist, [1/(1 + (10 + var) * x**2) for x in xlist], ':', color='blue')
    pylab.plot(lagrx, lagry, 'go', color='orange', marker='d', markeredgecolor='red')




task1()
task2a(n=4)
#xi=cos ((2i+1)?/N),     N=2(n+1),     i= 0,1,..,n;
task2b(n=4)
pylab.show()