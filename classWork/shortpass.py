print("please enter the pass")
s = input()
if len(s) < 6:
    print("its to short")
elif s[:6] == "no":
    print("not avilable password")
else:
    print("ok")
