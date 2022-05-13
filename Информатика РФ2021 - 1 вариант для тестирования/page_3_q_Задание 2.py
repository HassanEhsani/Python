def f(a,b,c):
    f = a == ((b or b)<=c)
    if f:
        return 1
    else:
        return 0

print("a","b","c","|","F")
for a in range (2):
    for b in range(2):
        for c in range(2):
            print(a,b,c,"|",f(a,b,c))