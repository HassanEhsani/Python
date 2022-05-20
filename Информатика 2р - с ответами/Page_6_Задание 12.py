from re import M


k = 0
min = 21988
max = 9918
for x in range(9919, 21987):
    x1 = x
    if(x % 2 == 0 or x % 3 == 0) and x % 16 != 0:
        mdig = 9
        while x > 0:
            if x % 10 < mdig:
                mdig = x % 10
            x = x//10
        if mdig == 3:
            k += 1
            if x1 > max:
                max = x1
            if x1 < min:
                min = x1
print(k, max-min)
