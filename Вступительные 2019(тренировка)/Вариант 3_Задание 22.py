from random import *
a = [0]*20
sum = 0
for i in range(20):
    a[i] = randint(-100, 100)
    k = a[i]
    while k > 0:
        if k % 10 != 3:
            sum += a[i]
            break
        k = k//10
print(a)
print(sum)
