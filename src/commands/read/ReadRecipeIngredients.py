from commands.Command import Command

class ReadRecipeIngredientsCommand(Command):
    def __init__(self, recipes, dc):
        self.recipes = recipes
        self.dc = dc

    def execute(self):
        print(self.dc.procedure('get_ingredients_for_recipes', (self.recipes, )))
