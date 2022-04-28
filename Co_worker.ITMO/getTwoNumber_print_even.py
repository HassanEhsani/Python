x = int(input("enter the number: "))
y = int(input("enter the number: "))
if x > y:
    x, y = y, x
if x % 2:
    x += 1
    print(list(range(x, y, 2)))
