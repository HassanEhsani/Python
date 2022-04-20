# numbers are entered from the keyboard, the input ends with the number 0. Determine how many prime natural numbers were entered (which are divisible only by themselves and by 1), and how many are composite
kp = ko = 0
x = int(input("enter the number(if = 0, then end:"))
while x != 0:
    isPrime = True
    for i in range(2, round(x**0.5)+1):
        if x % i == 0:
            isPrime = False
            break
    if isPrime: kp += 1
    else: ko += 1
    x = int(input("enter the number: "))
print("isPrime count = ", kp)
print("other count = ", ko)
