import random

# Request an upper range of number from a user
random_number_request = input("Please provide a number for a range: ")

# Make sure input is a digit and convert to an integer.
if random_number_request.isdigit():
    random_number_request = int(random_number_request)
    # 0 Inputs are not allowed for a upper range
    if random_number_request <= 0:
        print("Please enter a number greater then 0")

    print(random_number_request)

else:
    print("Not a valid number, please enter a numeric value.")
