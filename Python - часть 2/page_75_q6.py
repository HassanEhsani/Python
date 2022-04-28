from random import randint
n = int(input())
A = [0]*n
for i in range(n):
    A[i] = randint(1, 100)
print(A, "")
iA = -1
Maxk1 = 0
for i in range(n):
    x = A[i]
    k1 = 0
    while x > 0:
        if x % 2 == 1:
            k1 += 1
        x = x//2
    if k1 > Maxk1:
        Maxk1 = k1
        iA = i
print("A[", iA, "]=", A[iA])
