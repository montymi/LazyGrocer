from commands import Command

class CreateRecipeIngredientCommand(Command):
    def __init__(self, recipe_title, ingredient_title, quantity, dc):
        self.recipe_title = recipe_title
        self.ingredient_title = ingredient_title
        self.quantity = quantity
        self.dc = dc

    def execute(self):
        print(self.dc.createRecipeIngredient(self.recipe_title, self.ingredient_title, self.quantity))