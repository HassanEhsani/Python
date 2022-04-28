_list = [2, 3, 1, 4, 8, 9]

temp = _list[0]
_list[0] = _list[len(_list)-1]
_list[len(_list)-1] = temp

print(_list)
