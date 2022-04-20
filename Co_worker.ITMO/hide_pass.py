# defination function
def secure_card_number(card_number):
    secure = "*"*15 + card_number[-4:]
    return secure

# call function
print(secure_card_number("1234-2341-3109-0012"))
