# Iterates through atring...

# ask user for atring
recipe_name = input("what is the recipe name? ")

error ="Your recupe name number in it."
has_errors =""

# look at each character in string and if it's a number, complain
for letter in recipe_name:
    if letter.isdigit() == True:
        print(error)
        has_errors = "yes"
        break

# give user feedback...
if has_errors !="yes":
    print("you are OK")