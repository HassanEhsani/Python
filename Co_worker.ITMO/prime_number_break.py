x = int(input("enter the number: "))
counter = 0
if x >= 2:
    if x % 2 == 0 and x != 2:
        print("The only even prime number is two~")
    else:
        flag = True
        i = 2
        lenght = (x//2)+1
        while i < lenght:
            if x % i == 0:
                flag = False
                print("Not a Prime!")
                break
            i += 1
            counter += 1
        if flag:
            print("Prime")
else:
    print("The first prime is a 2")
print(counter)
