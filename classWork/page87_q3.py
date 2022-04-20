print("enter the number binary")
s = input()
n = len(s)
count = 0
for c in s:
    if c in ["1"]:
        count += 1

print("One = ", count)
    

