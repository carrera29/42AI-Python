# from book import Book

class Recipe:

    def __init__(self, name: str, cooking_lvl: int, cooking_time: int, ingredients: str, description: str, recipe_type: str):
        self.name = name
        self.cooking_lvl = cooking_lvl
        self.cooking_time = cooking_time
        self.ingredients = ingredients
        self.description = description
        self.recipe_type = recipe_type

    def __str__(self):
        return (f"\n\
        Recipe name:    {self.name}\n\
        Cooking level:  {self.cooking_lvl}\n\
        Cooking time:   {self.cooking_time}\n\
        Ingredients:    {self.ingredients}\n\
        Description:    {self.description}\n\
        Recipe type:    {self.recipe_type}\n")

# receta1 = Recipe("tarta", 3, 60, "harina, huevos, azucar", "tarta rica", "lunch")
# print (recipes_list["lunch"])
# print (receta1)