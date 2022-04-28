_list = [3,2,4,1,9,5]
x= int(input("enter the number: "))

i = 0
while i<len(_list):
    if _list[i]==x:
        print(i)
        break
    i +=1
if i == len(_list):
    print(-1)
