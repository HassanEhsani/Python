print("Welome to my quiz game!")

playing = input("Do you want to play? ")
if playing.lower() != "yes":
    quit()
print("OK Let's Play:) ")
score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorect!")

answer = input("what does GPU stand for? ")
if answer.lower() == "Graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorect!")

answer = input("what does RAM stand for? ")
if answer.lower() == "Random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorect!")

answer = input("what does PSU stand for? ")
if answer.lower() == "Power supply":
    print("Correct!")
    score += 1
else:
    print("Incorect!")

# print("you got " + str(score) + "question Correct!")
print("you got " + str((score/4)*100) + "%.")
