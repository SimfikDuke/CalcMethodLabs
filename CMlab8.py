import numpy as np


class Iter(object):
    def __init__(self, array):
        self.n = len(array)
        self.a = array
        self.b = np.array([array[i][-1] for i in range(self.n)], dtype=float)
        self.c = self.getC()
        self.d = np.array([self.b[i]/self.a[i][i] for i in range(self.n)], dtype=float)
        self.xn = self.d
        self.xn1 = self.d

    def getC(self):
        c = np.zeros((self.n, self.n))
        for i in range(self.n):
            for k in range(self.n):
                if i != k:
                    c[i][k] = -self.a[i][k]/self.a[i][i]
                else:
                    c[i][k] = 0
        return c

    def do_simple_iter(self, n='n'):
        self.xn = self.xn1
        self.xn1 = np.dot(self.c, self.xn) + self.d
        print("X("+str(n)+") = ", end='')
        print(self.xn1)


tempArr = [
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 1, 1]
]
npArr = np.array(tempArr, dtype=float)
myIter = Iter(npArr)
print('a')
print(myIter.a)
print('b')
print(myIter.b)
print('c')
print(myIter.c)
print('d')
print(myIter.d)
print(' ')

for i in range(10):
    myIter.do_simple_iter(i+1)
