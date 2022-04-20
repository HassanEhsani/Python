print("please enter the pass")
s = input()
if s[-3:] == "php" or s[-3:] == "htm" or s[-4:] == "html":
    print("its the web page")
else:
    print("its something else")
