s = input("Enter 3 numbers and 3 letters: ")
a = [0]*3
index = 0    
print("Letters:")
for i in range(0, 6):
    if((s[i] >= 'a' and s[i] <= 'z') or (s[i] >= 'A' and s[i] <= 'Z')):
        print(s[i], end="")
        continue
    if(s[i] >= '0' and s[i] <= '9'):
        a[index] = s[i]
        index += 1
tg = ''
for i in range(0, 2):
    for j in range(i+1, 3):
        if(a[i] < a[j]):
            tg = a[i]
            a[i] = a[j]
            a[j] = tg
print("\nNumber:")
for i in range(0, 3):
    print(a[i], end="")
