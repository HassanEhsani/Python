# defination function
from unittest import result

# defination function
def is_Palindrome(text):
    if text.lower() == text[::-1].lower():
        return True
    else:
        return False

# call function
print(is_Palindrome("MOM"))

