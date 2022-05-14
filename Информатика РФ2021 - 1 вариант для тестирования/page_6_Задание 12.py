min = 555556
q = 0
for x in range(100, 555555):
    if(x % 12 == 0 or x % 15 != 0) and (x % 8 == 7 or (x % 8 == 6 and (x//8) % 8 == 6)):
        q += 1
        if min > x:
            min = x
print(q, min**2)
