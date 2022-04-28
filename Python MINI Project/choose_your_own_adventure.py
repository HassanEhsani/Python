name = input("Type your name: ")
print("welcome", name, "to this adventure!")

answer = input(
    "your are on a dirt road, it has come to an end, and you can go left or right. which way you like to go ?").lower()

if answer == "left":
    answer = input(
        "you come to a river, you can walk around it or swim accross? type walk to walk around and swim to swim accross: ")

    if answer == "swim":
        print("you swam accross and were eaten by alligator.")
    elif answer == "walk":
        print("you walk for many miles, ran out of water and you lost the game ")
    else:
        print("not a valid options. you lose.")

elif answer == "right":
    answer = input(
        "you come to a bridge, its looks wobbly, do you wanted to cross it or head back(cross/back)? ")

    if answer == "back":
        print("you can go back and loss ")
    elif answer == "cross":
        answer = input(
            "you cross the bridge and meet a stranger. Do you talk to them (YES/NO)? ")
        if answer == "yes":
            print("you talk to the stranger and they gave you gold. You Win!")
        elif answer == "no":
            print("you ignore the stranger and you loss!")
        else:
            print("not a valid options. you lose.")

    else:
        print("not a valid options. you lose.")


else:
    print("not a valid options. you lose.")

print("Thank you for trying",name)
