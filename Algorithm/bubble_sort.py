from random import randint as rnd
from sys import flags
amount = 10
_list = [rnd(1, amount)for i in range(amount)]
counter = 0
for i in range(amount-1):
    flag = False
    for j in range(amount-1):
        if _list[j] > _list[j+1]:
            _list[j], _list[j+1] = _list[j+1], _list[j]
            flag = True
        counter +=1
    if not flag:
        break
            
print(_list)
print(counter)