# Get's source of recipe name and checks it is not blank

# To Do
# Allow users to specify a custom error massage
# Allow users to specify whether number are allowed

# Not Blank Function goes here
def not_blank (question, error_msg, num_ok):
    error = error_msg

    valid = False
    while not valid:
        response = input(question)
        has_errors = ""

        if num_ok !="yes":
            # look at each character in string and if it's a number, complain
            for letter in response:
                if letter.isdigit() == True:
                    has_errors = "yes"
                    break

        if response == "":
             print(error)
             continue
        elif has_errors != "":
            print(error)
            continue
        else:
            return response


# Main Routine...

# set up empty ingredient list
ingreddients = []

# Loop to ask users to enter an ingredient
stop = ""
while stop !="xxx":
     # Ask user for ingredient (via not blank function)
    get_ingredient = not_blank ("please type in an ingredient name: "
                                "This can't be bland ",
                                "yes")
    # Stop loopin if exit code is typed and there anr more
    # than 2ingredients...
    if get_ingredient.lower() == "xxx" and len(ingreddients) > 1:
        break

    elif get_ingredient.lower() == "xxx" and len(ingreddients) <2:
        print("You need at least teo ingredients in the list.  "
        "Please add more ingredients.")

     # If exit code is not entered, add ingredient to list
    else:
        ingreddients.append(get_ingredient)

# Output list
print(ingreddients)