for x in range(1, 1000):
    x1 = x
    k = x1 % 6
    a = 0
    b = 0
    while x1 > 0:
        d = x1 % 6
        if d == k:
            a = a+1
        b = b+d
        x1 = x1//6
    if a == 2 and b == 15:
        print(x)
        break
