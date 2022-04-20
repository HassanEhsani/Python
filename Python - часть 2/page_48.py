# numbers are entered from the keyboard, the input ends with the number 0. Determine the arithmetic mean of those entered numbers that are powers of 2. Print "none" if there are no such numbers.
from re import X


x = int(input("enter the number: "))
z = X
k=s=0
while x!=0:
    while x%2==0:
        x=x//2
        if x==1:
            k +=1
            s +=z
    x = int(input("find the number: "))
    z = x
if k !=0:
    print("avergae of number, divided by 2= ",s/k)
else:
    print("the number is not!")