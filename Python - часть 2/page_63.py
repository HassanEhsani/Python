n = int(input("enter the number(N): "))
k = 0
for i in range(n):
    x = int(input())
    if x > 0:
        k += 1
print("The number of Positive=> ",k)
