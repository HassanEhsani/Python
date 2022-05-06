# def printNum(x, n):
#     if x == 0:
#         return
#     printNum(x//n, n)
#     if x % n < 10:
#         print(x % n, end="")
#     else:
#         print(mas[x % n], end="")


# mas = "0123456789ABCDEF"
# x = int(input("enter the Decimal number: "))
# n = int(input("Введте основание системы счисления (2-16):"))
# printNum(x, n)

def printNum(x, n):
    if x == 0:
        return
    printNum(x//16, n)
    if x % n < 10:
        print(x % n, end="")
    else:
        print(mas[x % n], end="")


mas = "0123456789ABCDEF"
x = int(input("enter the Decimal number: "))
# n = int(input("Введте основание системы счисления (2-16):"))
printNum(x, 16)
