from commands.Command import Command
from datetime import datetime

class CreateRecipeIngredientCommand(Command):
    def __init__(self, recipe_title, ingredient_title, quantity, dc):
        self.recipe_title = recipe_title
        self.ingredient_title = ingredient_title
        self.quantity = quantity
        self.date = datetime.now().strftime('%Y-%m-%d')
        self.dc = dc

    def execute(self):
        print(self.dc.procedure('add_ingredient_to_recipe', (self.recipe_title, self.ingredient_title, self.quantity, self.date)))
