print("please enter the number for count")
n = int(input())
count1 = 0
sumdig = 0
while n > 0:
    sumdig += n % 10
    if n % 10 == 1:
        count1 += 1
    n = n//10
print("sum",sumdig)
