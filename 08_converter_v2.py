# Conversion Function...

import csv

# ***** Functions go here *****
def gentral_converter(how_much,lookup,dictionary,conversion_factor):

    if lookup in dictionary:
        mult_by = dictionary.get(lookup)
        how_much = how_much * float(mult_by) / conversion_factor
        converted = "yes"

    else:
        converted = "no"

    return [how_much,converted]

def unit_checker():

    unit_tockeck = input("Unit? ")

    # Abbreviation list
    teaspoon = ["tsp", "teaspoon", "t" "teaspoons"]
    tablespoon = ["tbs", "tablespoon", "T", "tbsp" "tablespoons"]
    ounce = ["oz", "ounce", "fl oz", "ounces"]
    cup = ["c", "cup", "cups"]
    pint = ["p", "pt", "fl pt","pint","pints"]
    quart = ["q", "qt", "fl qt","quarts"]
    mls = ["ml", "milliliter", "millilitre","milliliters", "millilitres"]
    litre = ["litre", "liter", "l", "litres", "liters"]
    pound = ["pound", "lb", "#", "pounds"]

    if unit_tockeck == "":
    # print("you chose()".format(unit_tocheck))
        return unit_tockeck
    elif unit_tockeck == "T" or unit_tockeck.lower() in tablespoon:
        return "tbs"
    elif unit_tockeck.lower() in tablespoon:
        return "tsp"
    elif unit_tockeck.lower() in ounce:
        return "ounce"
    elif unit_tockeck.lower() in cup:
        return "cup"
    elif unit_tockeck.lower() in pint:
        return "pint"
    elif unit_tockeck.lower() in quart:
        return "quart"
    elif unit_tockeck.lower() in mls:
        return "ml"
    elif unit_tockeck.lower() in litre:
        return "litre"
    elif unit_tockeck.lower()in pound:
        return "pound"


# ****** Mian Rountine  Goes hrer ******

# dictionaries go here
unit_central = {
    "tsp": 5,
    "tbs": 15,
    "cup" : 237,
    "ounce": 28.35,
    "pint": 473,
    "quart": 946,
    "pound": 454,
    "litre":  1000,
    "ml": 1
}

# *** Generste food dictionary *****
# open file
groceries = open('01_ingredients_ml_to_g.csv')

# Read data into a list
csv_groceries = csv.reader(groceries)

# Create a dictionary to hold the data
food_dictionary = {}

# Add the data from the list into the dictionary
# (first item in row is key, next is definition)

for row in csv_groceries:
    food_dictionary[row[0]] = row[1]

print(food_dictionary)

# **** Get items etc *****

keep_going = ""
while keep_going == "":
    amount = eval(input("hoe much? "))
    amount = float(amount)

    # Get unit and change it to match dictionary.
    unit = unit_checker()
    ingredient = input ("Ingredient: ")

    # Convert to mis if possible
    amount = gentral_converter(amount, unit, unit_central, 1)
    print(amount)

    # If we cooverted to mls, try and convert to grams
    if amount[1] == "yes":
        amount_2 = gentral_converter(amount[0],ingredient,food_dictionary,250)

        # if the ingredient is in the list,convert it
        if amount_2[1] == "yes":
            print(amount_2)

        # if the ingrediennt is not the list,leave the unit as ml
        else: print("unchanged")

    # If the unit is not mls, leave the line unchanged
    else:
        print("unchanged")

    # keep_going = input ("<enter> or q ")















































