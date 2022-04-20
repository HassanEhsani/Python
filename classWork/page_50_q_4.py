print("please enter 4 numbers: ")
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))
d = int(input("d: "))
if a > b and a > c and a > d:
    print("bigger: ", a)
elif b > a and b > c and b > d:
    print("bigger: ", b)
if c > a and c > b and c > d:
    print("bigger: ", c)
if d > a and d > b and d > c:
    print("bigger: ", d)
