# numbers are entered from the keyboard, the input ends with the number 0. Determine the minimum and maximum of those entered two-digit natural numbers that end in 6. Print "none" if there are no such numbers.
x = int(input())
count = 0
while x != 0:
    if x % 6 == 0 and 9 < x < 100:
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

    print("Maximum=> ", Max)
    print("Minimum=> ", Min)
