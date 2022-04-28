from random import randint
n = int(input())
A = [0]*n
for i in range(n):
    A[i] = randint(-100, 100)
print(A, "")
Min = -101
Max = 101
count = 0
for i in range(n):
    if A[i] % 2 == 0:
        count += 1
        if count == 1:
            Min = A[i]
            Max = A[i]
        else:
            if A[i] > Max:
                Max = A[i]
            if A[i] < Min:
                Min = A[i]
if count == 0:
    print("not found")
else:
    print("Max", Max, "Min", Min)
