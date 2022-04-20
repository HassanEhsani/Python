# defination function
def is_valid(pin_code):
    if pin_code.isdigit() == True:
        if len(pin_code)==4 or len(pin_code)==6:
            return True
        else:
            return False
    return False

# call function
print(is_valid("1234"))