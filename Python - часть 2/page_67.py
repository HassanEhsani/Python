n = int(input())
a = [0]*n
for i in range(n):
    a[i] = int(input())
i = count = 0
for i in range(n):
    isPrime = True
    for j in range(2, round(a[i]**0.5)):
        if a[i] % j == 0:
            isPrime = False
            break
    if isPrime:
        count += 1
        if count == 1:
            Max = Min = a[i]
        else:
            if a[i] > Max:
                Max = a[i]
            if a[i] < Min:
                Min = a[i]
    if count == 0:
        print("Not found")
    else:
        print("Max of print=>", Max)
        print("Min of print=>", Min)
