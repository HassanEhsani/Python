from random import randint
A = [0]*10
B = [0]*10
for i in range(10):
    A[i] = randint(0, 99)
    B[i] = A[i] % 10+A[i]//10
print(A)
print(B)
for k in range(10-1):
    nM = k
    for i in range(k, 10):
        if B[i] < B[nM]:
            nM = i
    B[k], B[nM] = B[nM], B[k]
    A[k], A[nM] = A[nM], A[k]
print(A)
