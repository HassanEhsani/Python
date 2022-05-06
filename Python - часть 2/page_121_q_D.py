def printNum(x, n):
    if x == 0:
        return
    printNum(x//n, n)
    if x % n < 10:
        print(x % n, end="")
    else:
        print(mas[x % n], end="")


mas = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
x = int(input("enter the Decimal number: "))
n = int(input("Введте основание системы счисления (2-36):"))
printNum(x, n)
