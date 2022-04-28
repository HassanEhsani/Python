_list = [2.2, 3.2, True, 2]
_float = 0
i = 0
while i < len(_list):
    if type(_list[i]) == float:
        _float += 1
    i += 1
print(_float)
