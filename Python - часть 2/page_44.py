print("please enter the number: ")
k = 0
s = 0
x = int(input())
while x != 0:
    if x % 10 == 5:
        k += 1
        s += x
    x = int(input())
if k == 0:
    print("Ответ: нет")
else:
    print("Ответ:", s)
