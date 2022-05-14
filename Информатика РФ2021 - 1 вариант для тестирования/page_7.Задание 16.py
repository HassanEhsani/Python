n = 0
for x in range(33333, 55555):
    if (x//100) % 2 == 0 and x % 2 == 0 and x % 6 != 0 and x % 7 != 0 and x % 8 != 0:
        n += 1
print(n)
 