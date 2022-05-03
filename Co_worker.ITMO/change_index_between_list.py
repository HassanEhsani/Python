import random
_list=[1,2,3,4,5,6,7,8,9,10]
for i in range(9):
    new = random.randint(i,9)
    _list[i],_list[new]=_list[new],_list[i]
print(_list)