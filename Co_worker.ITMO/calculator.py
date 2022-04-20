# defination function
def calculator(num1, operator, num2):
    if operator == '+':
        result = num1 + num2
    elif operator == '*':
        result = num1*num2
    elif operator == '/':
        result = num1/num2
    elif operator == '-':
        result = num1-num2
    else:
        result("the operator is not valid")
    print(result)


# cll function
try:
    n1 = int(input("please enter the number: "))
    op = input("please enter the operator(+*/-): ")
    n2 = int(input("please enter the number"))
except:
    print("some thin is wrog! ")
else:
    calculator(n1, op, n2)
