from multiprocessing import RLock
import random

print("Rock...".lower())
print("Paper...".lower())
print("Scissor...".lower())
print("---------------------------------")

randomNumber = (random.randint(0, 2))
computerMove = "rock"

if randomNumber == 0:
    computerMove = "rock"
elif randomNumber == 1:
    computerMove = "paper"
elif randomNumber == 2:
    computerMove = "scissor"


Player_1 = input("Player_1, make your move...")

print(f"Player_2, make your move...:{computerMove}")
Player_2 = computerMove

if Player_1 == Player_2:
    print("that's tie ...")

elif Player_1 == "rock":
    if Player_2 == "scissor":
        print("player_1 wins!...")
    elif Player_2 == "paper":
        print("player_2 wins!...")
elif Player_1 == "paper":
    if Player_2 == "rock":
        print("player_1 wins!...")
    elif Player_2 == "scissor":
        print("player_2 wins!...")
    elif Player_1 == "scissor":
        if Player_2 == "paper":
            print("player_1 wins!...")
elif Player_2 == "rock":
    print("player_2 wins!...")
else:
    print("something went wrong")

    # if Player_1 == "rock" and Player_2 == "scissor":
    #     print("Player_1 wins!...")
    # elif Player_1 == "rock" and Player_2 == "paper":
    #     print("player_2 wins!...")
    # elif Player_1 == "paper" and Player_2 == "rock":
    #     print("player_1 wins!...")
    # elif Player_1 == "paper" and Player_2 =="scissor":
    #     print("player_2 wins!...")
# elif Player_1 == "scissor" and Player_2 == "paper":
#     print("player_1 Wins!...")
# `elif Player_1 == Player_2:
#     print("that's tie ...")
# else:
#     print("something went wrong")`
