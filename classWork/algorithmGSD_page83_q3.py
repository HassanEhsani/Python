from tkinter import Y


print("enter 2 numbers")
a = int(input())
b = int(input())
x, y = a, b
while x != y:
    if x > y:
        x -= y
    else:
        y -= x
print("GSD(", a, ",", b, ") =", x)
