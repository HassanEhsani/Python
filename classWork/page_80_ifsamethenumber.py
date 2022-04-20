n = int(input())
n1 = n % 10
p = "not"
while n > 0:
    n = n//10
    n2 = n % 10
    if n1 == n2:
        p = "yes"
    n1 = n2
print(p)
