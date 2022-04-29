from cmath import sqrt


print("enter a,b,c: ")
a = float(input())
b = float(input())
c = float(input())
D = b*b - 4*a*c
x1 = (-b+sqrt(D))/(2*a)
x2 = (-b-sqrt(D))/(2*a)

print("x1=", x1, "x2=", x2, sep="")
