from msvcrt import kbhit


for x in range(1, 1000):
    x1 = x
    k = x1 % 5
    a = 0
    b = 0
    while x1 > 0:
        d = x1 % 5
        if d == k:
            a = a+1
        b = b+d
        x1 = x1//5
    if a == 3 and b == 10:
        print(x)
        break
