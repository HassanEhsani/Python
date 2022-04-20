from random import randint


N = 10
A = [0]*N
for i in range(N):
    A[i] = randint(100, 200)
print("Array: ", A)
i = 0
while (i < N) and (A[i] % 10 != 2):
    i += 1
if i < N:
    print("A[", i, "]=", A[i])
else:
    print("not found!")
