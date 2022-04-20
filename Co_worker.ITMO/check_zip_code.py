# defination function
def validation_zip_code(zip_code):
    if len(zip_code) == 5 and zip_code.isdigit():
        print("%s It's Your Zip Code" % (zip_code))
    else:
        print("%s It's not Your Zip Code" % (zip_code))


# call function
code = input("please enter the code: ")
validation_zip_code(code)
