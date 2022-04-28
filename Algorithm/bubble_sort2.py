from random import randint as rnd
import matplotlib.pyplot as plt
from sys import flags
amount = 100
_list = [rnd(1, amount)for i in range(amount)]

for i in range(amount-1):
    flag = False
    for j in range(amount-1):
        if _list[j] > _list[j+1]:
            _list[j], _list[j+1] = _list[j+1], _list[j]
            flag = True
        plt.bar(list(range(amount)),_list)
        plt.pause(00.05)
        plt.clf()
    if not flag:
        break
plt.show()            
print(_list)
