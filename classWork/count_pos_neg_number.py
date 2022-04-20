# numbers are entered from the keyboard, the input ends with the number 0. Determine how many positive and how many negative numbers were entered.
kp = kn = 0
x = int(input("enter the number (if = 0, then end): "))
while x != 0:
    if x > 0:
        kp += 1
    else:
        kn += 1
    x = int(input("please enter the number: "))
print("Positive count = ", kp)
print("Negative count = ", kn)
