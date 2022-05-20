x = 7**103+20*7**204-3*7**57+97
s = 0
while x:
    if x % 7 == 6:
        s = s+1
    x = x//7
print(s)
