# numbers are entered from the keyboard, the input ends with the number 0. Determine the minimum and maximum of the entered numbers
x = int(input())
count = 0
while x != 0:
    if x % 3 == 0:
        count += 1
        if count == 1:
            Max = x
            Min = x
        else:
            if x > Max:
                Max = x
            if x < Min:
                Min = x

    x = int(input())
if count == 0:
    print("Not found it: ")
else:

    print("Maximum=> ",Max)
    print("Minimum=> ",Min)
