from random import *
a = [0]*20
count = 0
for i in range(20):
    a[i] = randint(-100, 100)
    if i % 2 != 0 and a[i] % 7 == 0:
        count += 1
print(a)
print("number of multiples 7 with an odd index =", count)
