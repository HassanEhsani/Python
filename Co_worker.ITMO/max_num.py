print("please enter 3 number")
n1 = input()
n2 = input()
n3 = input()
if n1 > n2 and n1 > n3:
    print(n1)
elif n2 > n1 and n1 > n3:
    print(n2)
elif n3 > n1 and n3 > n2:
    print(n3)
