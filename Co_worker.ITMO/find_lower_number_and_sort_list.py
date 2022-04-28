_list = [2, 3, 1, 5, 3, 0, 9, -1]
j = 0
while j < len(_list):
    x = j
    i = j+1
    while i < len(_list):
        if _list[i] < _list[x]:
            x = i
        i += 1
    _list[j], _list[x] = _list[x], _list[j]
    print(_list)
    j += 1
