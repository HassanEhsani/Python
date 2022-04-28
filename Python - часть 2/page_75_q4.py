x = int(input("enter the number: "))
k = s = 0
while x != 1:
    if x % 3 == 0:
        k += 1
        s += x
    x = int(input("find the number: "))
print("sum of number, divided by 3 = ", s)