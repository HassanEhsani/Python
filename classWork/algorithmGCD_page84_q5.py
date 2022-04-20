from itertools import count

print("enter 2 number: ")
a = int(input())
b = int(input())
count = 0
x, y = a, b
while x != y:
    count += 1
    if x > y:
        x -= y
    else:
        y -= x
print("GCD(", a, ",", b, ")=", x)
print("usually algorithm GCD ", count, "Steps")

x, y = a, b
count = 0
while x != 0 and y != 0:
    count += 1
    if x > y:
        x %= y
    else:
        y %= x
if x != 0:
    print("GCD(", a, ",", b, ")=", x)
else:
    print("GCD(", a, ",", b, ")=", y)
