from ast import Continue


i = 0
while i < 10:
    print(i)
    if i % 2 == 0:
        i += 2
        Continue
    else:
        i += 1
