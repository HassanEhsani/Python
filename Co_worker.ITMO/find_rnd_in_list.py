from random import random


import random
from typing import Counter
_list = []
i = 0
Counter = 0
while i < 10:
    new = random.randint(1, 10)
    if new not in _list:
        _list.append(new)
        i += 1
    Counter += 1
print(_list)
print(Counter)
