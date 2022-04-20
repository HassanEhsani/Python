# numbers are entered from the keyboard, the input ends with the number 0. Determine the sum of those entered numbers that are divisible by 3 and end with 1. Print "none" if there are no such numbers.
x = int(input("enter the number: "))
k = s = 0
while x != 0:
    if x % 3 == 0 and x % 10 == 1:
        k += 1
        s += x
    x = int(input("find the number: "))
if k == 0:
    print("this is not")
else:
    print("sum of = ", s)
