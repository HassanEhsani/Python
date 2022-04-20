from traceback import print_tb


print("please enter the pass: ")
p1 = input()
p2 = input()
if len(p1) == 4 and len(p2) == 4:
    print(True)
elif len(p1) == 6 and len(p2) == 6:
    print(True)
else:
    print(False)
