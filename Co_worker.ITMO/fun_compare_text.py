# defination function
def are_string_equal(str1, str2, is_case_sencetive=False):
    if is_case_sencetive == True:
        return str1 == str2
    else:
        return str1.lower() == str2.lower()


# call function
print(are_string_equal("Tehran", "tehran",True))



