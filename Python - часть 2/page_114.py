def printUpDownO(c, n):
    print(c*n)


def printCenterO(n):
    k = n-2
    print("o", " "*k, "o", sep="")


n = int(input("enter the number: "))
printUpDownO("o", n)
for i in range(n-2):

    printCenterO(n)
printUpDownO("o", n)
