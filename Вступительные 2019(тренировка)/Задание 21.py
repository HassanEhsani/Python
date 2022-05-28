from re import X


x = int(input("enter the number: "))
a = x
sum = 0
count = 0
while a > 0:
    if a % 2 != 0:
        sum += a % 10
        count += 1
    a = a//10
if count == 0:
    print("Not Found!")
else:
    print("avrega of number", x, "=", sum/count)
