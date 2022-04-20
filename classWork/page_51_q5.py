print("please enter 5 numbers: ")
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))
d = int(input("d: "))
f = int(input("f: "))

if a>b and a>c and a>d and a>f:
    print("bigger: ",a)
if b>a and b>c and b>d and b>f:
    print("bigger: ",b)
if c>a and c>b and c>d and c>f:
    print("bigger: ",c)
if d>a and d>b and d>c and d>f:
    print("bigger: ",d)
if f>a and f>b and f>c and f>d:
    print("bigger: ",f)