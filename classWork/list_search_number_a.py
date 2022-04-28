_list = [3,2,4,1,9,5]
x= int(input("enter the number: "))
flage = False
i = 0
while i<len(_list):
    if _list[i]==x:
        flage = True
        print(i)
    i +=1
if not flage:
    print(-1)
