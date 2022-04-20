from random import randint

N = 10
A = [0]*N
for i in range(N):
    A[i] = randint(0, 101)
print("array: ",A)
Sm, Cm, Sb, Cb = 0, 0, 0, 0
for i in range(N):
    if A[i] < 50:
        Sm += A[i]
        Cm += 1
    else:
        Sb += A[i]
        Cb += 1
print("the average is <50 = ", Sm/Cm)
print("the average is >50 = ", Sb/Cb)
