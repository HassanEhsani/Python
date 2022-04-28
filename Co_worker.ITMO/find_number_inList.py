_list = [2,3,1,4,9]
x = int(input("please enter the number: "))
if x in _list:
    print(_list.index(x))
else:
    print(-1)