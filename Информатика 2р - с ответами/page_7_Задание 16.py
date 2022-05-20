n = 0
for x in range(57888, 74555):
    if (x//10000) % 2 != 0 and (x//1000) % 2 != 0 and (x//100) % 2 == 0 and \
            (x//10) % 2 == 0 and x % 2 == 0 and x % 7 != 0 and x % 9 != 0 and x % 13 != 0:
        n += 1
print(n)
