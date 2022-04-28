list1 = [2, 3, 5, 6, 8, 9]
list2 = [1, 3, 5, 6]


def combine(list1, list2):
    _list = []
    len1 = len(list1)
    len2 = len(list2)
    i = j = 0
    while i < len1 and j < len2:
        if list1[i] < list2[j]:
            _list.append(list1[i])
            i += 1
        else:
            _list.append(list2[j])
            j += 1
    _list += list1[i:]
    _list += list2[j:]
    return _list


print(combine(list1, list2))

