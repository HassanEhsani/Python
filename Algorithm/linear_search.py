from random import randint as rnd

lenght = 20
_list = [rnd(0-lenght,lenght)for i in range(lenght)]
print(_list)

def linear_search(_list,v):
    for i in _list:
        if i == v:
            return "found"
    else:
        return "not found"
print(linear_search(_list,90))