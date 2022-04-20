print("enter 2 number")
a = int(input())
b = int(input())
x, y = a, b
while x != 0 and y != 0:
    if x > y:
        x %= y
    else:
        y %= x
if x != 0:
    print("GCD(", a, ",", b, ") =", x)
else:
    print("GCD(", a, ",", b, ") =", y)
