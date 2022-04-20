print("enter the number")
s = input()
n = len(s)
count = 0
for c in s:
    if c in ["1", "0"]:
        count += 1
if count == n:
    print("yes")
else:
    print("no")
