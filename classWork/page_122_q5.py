from random import randint

N = 10
A = [0]*N
for i in range(N):
    A[i] = randint(0, 5)
print("Array: ", A)
i = c = 1
while (i < N):
    if A[i] == A[i-1]:
        print('A[', i-1, ']=', 'A[', i, ']=', A[i])
    c += 1
    i += 1
if c == 0:
    print("not found!")
