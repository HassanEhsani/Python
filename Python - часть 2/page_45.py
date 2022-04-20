# numbers are entered from the keyboard, the input ends with the number 0. Determine the sum of those entered numbers that are divisible by 5
x = int(input("enter the number: "))
k = s = 0
while x != 0:
    if x % 5 == 0:
        k += 1
        s += x
    x = int(input("find the number: "))
print("sum of number, divided by 5 = ", s)
