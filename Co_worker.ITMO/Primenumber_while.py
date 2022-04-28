n = int(input("enter the number: "))
if n >= 2:
    counter = 0
    flag = True
    i = 2
    while i < n:
        if n % i == 0:
            flag = False
        i += 1
        counter +=1
    if flag:
        print("Prime")
    else:
        print("Not a prime")
        
else:
    print("The First Prime is 2")
print(counter)
