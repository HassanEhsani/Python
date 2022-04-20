from random import randint
N = 10
A = [0]*N
a, b = map(int, input().split())
for i in range(N):
    A[i] = randint(a, b)
print(A)
