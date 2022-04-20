# deifinition function
def odd_even(num):
    result = num % 2
    if result == 0:
        print("%d is even!" % (num))
    else:
        print("%d is odd!" % (num))


# call function
num = int(input("please enter the number: "))
odd_even(num)
