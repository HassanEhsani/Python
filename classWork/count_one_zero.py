print("please enter the number")
s = input()
n = len(s)
count = 0
for c in s:
    if c in ["1"]:
        count += 1
print("one= ", count)
print("zer= ", n-count)
