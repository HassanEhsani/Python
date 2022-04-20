from random import randint
N = 10
A = [0]*N
a, b = map(int, input().split())
if a > b:
    a, b = b, a
for i in range(5):
    A[i] = randint(a, b)
    A[5+i] = A[i]*A[i]
print(A)
