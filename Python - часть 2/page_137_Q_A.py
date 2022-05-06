def Even(n):
    return(n % 10 == 0 or n % 10 == 1)


i = int(input("enter the number: "))
print("statment", i, "0 or 1", Even(i))
