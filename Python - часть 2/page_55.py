x = int(input())
count = 0
while x != 0:
    if x % 2 == 0:
        count += 1
        if count == 1:
             m = x
        else:
            if x > m:
                m = x
    x = int(input())
if count == 0:
    print("Not found it: ")
else:
    
    print(m)
