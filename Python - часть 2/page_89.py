from random import randint
A = [0]*10
for i in range(10):
    A[i] = randint(0, 100)
print(A)
for k in range(4):
    nM = k
    for i in range(k, 5):
        if A[i] < A[nM]:
            nM = i
    A[k], A[nM] = A[nM], A[k]
for k in range(5, 9):
    nM = k
    for i in range(k, 10):
        if A[i] > A[nM]:
            nM = i
    A[k], A[nM] = A[nM], A[k]
print(A)
