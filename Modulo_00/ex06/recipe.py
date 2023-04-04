cookbook = {
    "bocadillo": {
        "ingredients" : ["jamón" , "pan", "queso" , "tomate"], 
        "meal" : "almuerzo", 
        "prep_time" : "10"},
    "tarta": {
        "ingredients" : ["harina" , "azúcar", "huevos"], 
        "meal" : "postre", 
        "prep_time" : "60"},
    "ensalada": {
        "ingredients" : ["aguacate", "rúcula", "tomates" , "espinacas"], 
        "meal" : "almuerzo", 
        "prep_time" : "15"},
}

def print_recepies():
    for i in cookbook:
        print (i)

def print_ingredients(meal):
    try:
        print (f"\nRecipe for {meal}:")
        print ("    Ingredients list:", cookbook[meal]["ingredients"])
        print ("    To be eaten for", cookbook[meal]["meal"])
        print ("    Takes", cookbook[meal]["prep_time"], " minutes of cooking\n")
    except:
        print ("Sorry, the recipe does not exist\n")

def del_recipe(name):
    del cookbook[name]

def create_recipe():
    name = input("Enter a name:\n ")
    print ("Enter ingredients:")
    ingredients = []
    ingredients.append(input())
    while ingredients[-1] != "":
        ingredients.append(input())
    type = input("Enter a meal type:\n")
    time = input(" Enter a preparation time:\n")
    cookbook[name] = {
        "ingredients" : ingredients,
        "meal" : type,
        "prep_time" : time}

print (
"""Welcome to the Python Cookbook !
List of available option:
    1: Add a recipe
    2: Delete a recipe
    3: Print a recipe
    4: Print the cookbook
    5: Quit\n""")
while (True):
    try: 
        num = int(input("Please select an option:\n>> "))
        if num is 1:
            create_recipe()
        elif num is 2:
            del_recipe(input("Enter a recipe name:\n\n"))
        elif num is 3:
            print_ingredients(input("Enter a recipe name:\n"))
        elif num is 4:
            print_recepies()
        elif num is 5:
            break
        else:
            print ("Sorry, this option does not exist\n")
    except:
        print ("Sorry, this option does not exist\n")