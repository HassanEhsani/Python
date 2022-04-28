_list = [3, 2, 5, 1]
x = 0
i = 1
while i < len(_list):
    if _list[x] > _list[i]:
        x = i
    i += 1
print(x)
