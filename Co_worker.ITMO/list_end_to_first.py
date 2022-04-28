
_list = []
i = 0
while i < 4:
    n = int(input("enter the number: "))
    _list.append(n)
    i += 1
_list1 = []
i = len(_list)-1
while i >= 0:
    _list1.append(_list[i])
    i -= 1
print(_list1)
