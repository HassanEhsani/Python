def printBin(x):
    if x == 0:
        return 0
    arr = []
    while x > 0:
        arr.append(x % 16)
        x //= 16
    arr.reverse()
    res = ""
    for i in range(len(arr)):
        if(arr[i] >= 10):
            if(arr[i] == 10):
                res += "A"
            if(arr[i] == 11):
                res += "B"
            if(arr[i] == 12):
                res += "C"
            if(arr[i] == 13):
                res += "D"
            if(arr[i] == 14):
                res += "E"
            if(arr[i] == 15):
                res += "F"

        else:
            res += str(arr[i])
    return res


print("enter the number: ")
x = int(input())

print(printBin(x))
