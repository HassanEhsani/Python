_list = [2, 4, 1, 5, 3]
x = int(input("enter the number: "))
flage = False
i = 0
while i < len(_list):
    if x == _list[i]:
        flage = True
        print(i)
    i += 1
if flage:
    pass
else:
    print(-1)