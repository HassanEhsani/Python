# defination function
from tokenize import Double


def free_delivery(total_cost):
    if total_cost > 40:
        print("you have a free delivery")
    else:
        print("you have not free delivery")


# call function
cost = int(input("please enter the cost: "))
free_delivery(cost)
