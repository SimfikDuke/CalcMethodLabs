import numpy as np


class RGauss(object):
    def __init__(self, array):
        self.n = len(array)
        self.answers = [1 for i in range(self.n)]
        self.a = array

    @staticmethod
    def input_matrix():
        n = int(input("Enter n: "))
        arr = [[] for i in range(n)]
        for i in range(n):
            arr[i] = list(map(float, input().split()))
            for j in range(n):
                if i == j:
                    arr[i].append(1)
                else:
                    arr[i].append(0)
        return np.array(arr)

    def sort_m(self, i):
        if self.a[i][i] == 0:
            k = i
            for h in range(i + 1, self.n):
                if self.a[h][i] != 0:
                    k = h
            if k != i:
                self.a[i], self.a[k] = self.a[k], self.a[i]
                return True
            else:
                print("OBRATNOY NET!!!!")
                return False
        return True

    def revers_matrix(self):
        for i in range(self.n):
            if self.sort_m(i):
                self.a[i] /= self.a[i][i]
                for j in range(self.n):
                    if i != j:
                        self.a[j] -= self.a[i]*self.a[j][i]
                print(self.a)
                print("\n")




