print("please enter your password: ")
m = input()

if m[-3:] == "php" or m[-3:] == "htm" or m[-4:] == "html":
    print("This is your webpage!")
else:
    print("Error!")
