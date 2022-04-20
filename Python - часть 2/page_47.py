# numbers are entered from the keyboard, the input ends with the number 0. Determine the arithmetic mean of those entered two-digit numbers that are divisible by 5. Output "none" if there are no such numbers.
x = int(input("enter the number: "))
k = s = 0
while x != 0:
    if x % 5 == 0 and 100 > x > 9:
        k += 1
        s += x
    x = int(input("find the number: "))
if k == 0:
    print("this number is not!")
else:
    print("the average of =", s/k)
