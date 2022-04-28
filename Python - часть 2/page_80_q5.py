from random import randint
n = int(input())
A = [0]*n
for i in range(n):
    A[i] = randint(-100, 100)
print(A, "")

count = 0
for i in range(n):
    if A[i] % 2 == 0:
        count += 1
        if count == 1:
            Min = i
        else:
            if A[Min] > A[i]:
                Min = i
if count == 0:
    print("not found")
else:
    print("min", Min, "Min", A[Min])
