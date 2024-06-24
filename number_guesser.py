import random

# UPPER LIMIT NUMBER
upper_number = input("Please provide upper limit number: ")

# Make sure input is a digit and convert to an integer.
if upper_number.isdigit():
    upper_number  = int(upper_number)
    # 0 Inputs are not allowed for a upper range
    if upper_number  <= 0:
        print("Please enter a number greater then 0")

    # user upper number to generate random number
    else:
        random_number = random.randint(0, upper_number)
        print(random_number)

else:
    print("Not a valid number, please enter a numeric value.")


# GUESS NUMBER
guess_number = input("Please guess a number: ")

# # Make sure input is a digit and convert to an integer.
# if guess_number.isdigit():
#     guess_number  = int(guess_number)
#     # 0 Inputs are not allowed for a upper range
#     if guess_number  <= 0:
#         print("Please enter a number greater then 0")
#
#     else:
#         quit()


if upper_number == guess_number:
        print ()

