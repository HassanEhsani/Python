x = 7**103+6*7**104-3*7**57+98
s = 0
while x:
    s = s + x % 7
    x = x//7
print(s)
