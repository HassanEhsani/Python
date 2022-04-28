_list = [-3, -2, 0, 2, 3, 4, 6, 9, 10, 13, 57]


def binary_search(_list, v):
    if len(_list) == 1:
        if _list[0] == v:
            return "found"
        else:
            return "Not_found"
    else:
        mid = len(_list)//2
        if v >= _list[mid]:
            return binary_search(_list[mid:], v)
        else:
            return binary_search(_list[:mid], v)


print(binary_search(_list, 1))
