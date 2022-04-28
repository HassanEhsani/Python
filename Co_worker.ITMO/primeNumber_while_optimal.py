import time
n = int(input("enter the number: "))
# start = time.time()
if n >= 2:
    counter = 0
    flag = True
    i = 2
    lenght = n//2
    while i < lenght:
        if n % i == 0:
            flag = False
        i += 1
        counter += 1
    if flag:
        print("Prime")
        # pass
    else:
        print("Not a prime")
        # pass
else:
    print("The First Prime is 2")
    # pass
# end = time.time()
print(counter)
# print(end-start)
