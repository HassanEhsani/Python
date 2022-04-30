def printBin(x, y):
    if x == 0:
        return 0
    printBin(x // y, y)
    print(x % y, end="")

# def printBin(x):
#     if x == 0:
#         return 0
#     arr = []
#     while(x > 0):
#         arr.append(x % 8)
#         x //= 8
#     arr.reverse()
#     res = ""
#     for i in range(len(arr)):
#         res += str(arr[i])
#     return res    

x = int(input("enter the number: "))
y = int(input("enter the number: "))
printBin(x, y)
