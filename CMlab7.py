import numpy as np

n = int(input("Enter n: "))
arr = [[] for i in range(n)]
for i in range(n):
    arr[i] = list(map(float, input().split()))

a = np.array(arr)
print(a)
print("\n")

for i in range(0, n-1):
    max_a = abs(a[i][i])
    max_k = i
    for k in range(i+1, n):
        if abs(a[k][i]) > max_a:
            max_a = abs(a[k][i])
            max_k = k
    if max_k != i:
        print("Swap " + str(a[i]) + " and " + str(a[max_k]))
        for l in range(n+1): a[i][l], a[max_k][l] = a[max_k][l], a[i][l]
        print(a)
        print("\n")

    #for j in range(i):
    #    if i>0:
    for l in range(i+1, n):
        m = a[i][i]/a[l][i]
        print("m = "+str(m)+"\n")
        a[l] = a[l]*m - a[i]

        print("And now we have:")
        print(a)
        print("\n")
    print(str(i+1))
