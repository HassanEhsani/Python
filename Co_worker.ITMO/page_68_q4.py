print("please enter your password: ")
n = input()
m = "qwerty"
if len(n) < 6:
    print("your password is too short!")
elif n == m:
    print("Error!")
else:
    print("OK!")
