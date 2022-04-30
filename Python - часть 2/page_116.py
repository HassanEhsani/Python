def printBin(n):
    c = 0
    x = 1
    while n != 0:
        c = c+(n % 2)*x
        n = n//2
        x = x*10
    print(c)
printBin(66)