print("please enter number:")
n = int(input())
coun = 0
sdig = 0
while n > 0:
    sdig += n % 10
    if n % 10 == 0:
        coun += 1
    n = n//10
print(sdig)
