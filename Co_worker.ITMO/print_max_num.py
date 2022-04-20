# definition function
def print_maximum(n1, n2, n3):
    if n1 > n2 and n1 > n3:
        Max = n1
    elif n2 > n1 and n2 > n3:
        Max = n2
    # elif n3 > n1 and n3 > n2:
    #     Max = n3
    else:
        Max = n3
    print((n1,n2,n3),"The Maximum number of: ", Max)


# call function
num1 = int(input("please enter the number: "))
num2 = int(input("please enter the number: "))
num3 = int(input("please enter the number: "))
print("====================>")
print_maximum(num1, num2, num3)
