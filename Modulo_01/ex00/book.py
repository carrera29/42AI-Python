from datetime import datetime as date
from recipe import Recipe 

class Book:
    def __init__(self, name: str):
        self.name = name,
        self.last_update = date.now(),
        self.creation_date = date.now(),
        self.recipes_list  = {
                                "starter" : [],
                                "lunch" : [],
                                "dessert" : []}

    def __str__(self):
        return (f"\n\
        Book name:      {self.name}\n\
        Last_update:    {self.last_update}\n\
        Creation_date:  {self.creation_date}\n\
        Recipes_list:   {self.recipes_list}")
    
    def add_recipe_type(self, recipe_type):
        try:
            recipes_list[recipe_type].append(self.name)
        except:
            print ("Wrong type recipe")

    def create_book(self, name):
        name = Book(name)

    def create_recipe(self, book_name: str, recipe: str, cooking_lvl: int, cooking_time: int, ingredients: str, description: str, recipe_type: str):
        try:
            Book[book_name]
            recipe = Recipe(recipe, cooking_lvl, cooking_time, ingredients, description, recipe_type)
            book_name.recipes_list[recipe_type].append(recipe)
        except:
            print ("book_name does not exit")
        

My_book = Book("desserts")
bizcocho = Recipe("Bizcocho", 3, 60, "harina, huevos, azucar, leche", "sencillo", "dessert")
# pizza = Recipe("pizza", 5, 5, "harina, agua, sal", "complicado", "lunch")
My_book.recipes_list[bizcocho.recipe_type].append(bizcocho)
# My_book.recipes_list[pizza.recipe_type].append(pizza)
for i in My_book.recipes_list["dessert"]:
    print(i)
# print (recipes_list["lunch"])

# print (pizza)
