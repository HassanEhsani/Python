from itertools import count
from operator import le


print("please enter number: ")
s = input()
n = len(s)
count = 0
for c in s:
    if c in ["1"]:
        count +=1
print("one= ",count)