from random import randint
a = randint(100000, 1000000)
b = randint(100000, 1000000)
c = randint(100000, 1000000)
print(a)
print(b)
print(c)
count1 = 0
count2 = 0
a = str(a)
b = str(b)
c = str(c)
for i in range(0, 6):
    if (a[i] == '1'):
        count1 += 1
    if (a[i] == '2'):
        count2 += 1
for i in range(0, 6):
    if (b[i] == '1'):
        count1 += 1
    if (b[i] == '2'):
        count2 += 1
for i in range(0, 6):
    if (c[i] == '1'):
        count1 += 1
    if (c[i] == '2'):
        count2 += 1
print("Numbers of ones:", count1)
print("Numbers of twos:", count2)
print("Sum:", count1+count2)
