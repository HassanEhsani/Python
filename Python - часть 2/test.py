    x = 1
    x = 0
n = int(input("enter the number: "))
while n!=0:
    c = c+(n%2)*x
    n = n//2
    x = x/0
print(c)

# def printBin(n):
#     c = 0
#     x = 1
#     while n != 0:
#         c = c+(n % 2)*x
#         n = n//2
#         x = x*10
#     print(c)
# printBin(253)
