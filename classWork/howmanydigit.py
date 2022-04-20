# numbers are entered from the keyboard, the input ends with the number 0. Determine how many two-digit natural numbers were entered, and how many others
k2 = ko =0
x = int(input("enter number(if = 0, then end):"))
while x!=0:
    if 9<x<100 or -10<x<0:
        k2 +=1
    else:
        ko +=1
    x=int(input("enter the number: "))
print("2 digit in number count = ",k2)
print("other count = ",ko)

