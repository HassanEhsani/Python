_list = [2, 3, 1, 5, 3, 0, 9,-1]
x = 0
i = 1
while i < len(_list):
    if _list[i] < _list[x]:
        x = i
    i += 1
_list[0], _list[x] = _list[x], _list[0]
print(_list)
