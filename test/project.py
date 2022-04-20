number = input("phone: ")
number_convertor={
    "1":"one",
    "2":"two",
    "3":"three",
    "4":"four",
    "5":"five"
}
result = ""
for ch in number:
    result += number_convertor.get(ch, "!")+" "

print(result)
