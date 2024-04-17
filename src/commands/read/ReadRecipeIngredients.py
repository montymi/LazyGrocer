from commands import Command

class ReadRecipeIngredientsCommand(Command):
    def __init__(self, recipes, dc):
        self.recipes = recipes
        self.dc = dc

    def execute(self):
        print(self.dc.getIngredients(self.recipes))