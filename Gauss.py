import numpy as np


class Gauss(object):

    def __init__(self, array):
        self.n = len(array)
        self.answers = [1 for i in range(self.n)]
        self.a = array

    def first_calc(self):
        n = self.n
        print("Primary array:\n")
        print(self.a)
        print("\n")
        for i in range(0, n-1):
            max_a = abs(self.a[i][i])
            max_k = i
            for k in range(i+1, n):
                if abs(self.a[k][i]) > max_a:
                    max_a = abs(self.a[k][i])
                    max_k = k
            if max_k != i:
                print("Swap " + str(self.a[i]) + " and " + str(self.a[max_k]))
                for l in range(n+1):
                    self.a[i][l], self.a[max_k][l] = self.a[max_k][l], self.a[i][l]
                print(self.a)
                print("\n")

            for l in range(i+1, n):
                if self.a[l][i] == 0:
                    return
                m = self.a[i][i]/self.a[l][i]
                print("Row"+str(l)+" = "+str(m)+"*Row"+str(l)+" - Row"+str(i)+"\n")
                self.a[l] = self.a[l]*m - self.a[i]

                print("And now we have:")
                print(self.a)
                print("\n")

    def get_answers(self):
        n = self.n
        self.answers = [1 for i in range(n)]
        if self.a[n-1][n]==0 and self.a[n-1][n-1]==0:
            print("Infinity number of results!")
            return
        elif self.a[n-1][n-1]==0:
            print("Results is absent!")
            return

            self.answers[-1] = self.a[n-1][n] / self.a[n-1][n-1]
        for i in range(2, n+1):
            for j in range(n-i+1):
                self.a[j][n] -= self.answers[-i+1] * self.a[j][-i]
                self.answers[-i] = self.a[-i][n] / self.a[-i][-i-1]
        print("Answers:\n")
        for i in range(n):
            print("x"+str(i+1)+" = "+str(self.answers[i])+"\n")
        return

    @staticmethod
    def input_matrix():
        n = int(input("Enter n: "))
        arr = [[] for i in range(n)]
        for i in range(n):
            arr[i] = list(map(float, input().split()))
        return np.array(arr)


myGauss = Gauss(Gauss.input_matrix())
myGauss.first_calc()
myGauss.get_answers()
