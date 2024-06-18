print("Welcome to my computer quiz!")

# Take user input
playing = input("Do you want to play?: ")

# Check if the user wants to play
if playing.lower() != 'yes':
    print("No worries, we will miss you!")
    quit()

print("Okay! Lets play")

# Capture score
score = 0

# Retrieve answer from a user on 4 separate questions
answer = input("What does a CPU stand for?: ")
if answer.lower() != "central processing unit":
    print("Incorrect answer!")
else:
    score += 1
    print("Correct answer!")

answer = input("What does a GPU stand for?: ")
if answer.lower() != "graphic processing unit":
    print("Incorrect answer!")
else:
    score += 1
    print("Correct answer!")

answer = input("What does a RAM stand for?: ")
if answer.lower() != "random access memory":
    print("Incorrect answer!")
else:
    score += 1
    print("Correct answer!")

answer = input("What does a PS stand for?: ")
if answer.lower() != "power supply":
    print("Incorrect answer!")
else:
    score += 1
    print("Correct answer!")

print (f"You got {(score)}  questions correct")
print ("You got " + str((score/4)*100) + "%")