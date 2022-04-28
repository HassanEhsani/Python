from random import randint
n = int(input())
a = [0]*n
k = 0
for i in range(n):
    a[i] = randint(1, 100)
    if a[i] % 5 == 0:
        k += 1
print(a)
print("the number divide by 5", k)
