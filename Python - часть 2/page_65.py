# the number N is entered from the keyboard, and then - N integers. Determine the sum of two-digit numbers (both positive and negative). If there were no two-digit numbers, output "none".
n = int(input("enter the number(N): "))
sum = count = 0
for i in range(n):

    x = int(input("Number: "))
    if (-100 < x < -9) or (9 < x < 100):
        sum += x
        count += 1
    if count == 0:
        print("Not Found")
    else:
        print("sum of digits= ", sum)
