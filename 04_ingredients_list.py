# Ingredients List


# Not blank Function goes here
def not_blank(question , error_msg, num_ok):
    error = error_msg

    valid = False
    while not valid:
        response = input(question)
        has_errors = ""

        if num_ok !="yes":
            # look at each character in string and if it's number, comolain
            for letter in response:
                if letter.isdigit() == True:
                    has_errors ="yes"
                    break

        if response == "":
            print(error)
            continue
        elif has_errors !="":
            print(error)
            continue
# Main Routine...

# set up empty ingredient list

# Loop to ask users to enter an ingredient

# Ask user for ingredient (via not blank function)

# If exit code is typed...

# Check that list contains at least two items

# If list contains at least two items break out of loop

# If exit code is not entered, add ingredient to list

# Output list