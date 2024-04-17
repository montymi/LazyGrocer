from commands import Command

class DeleteRecipeCommand(Command):
    def __init__(self, recipe_title, dc):
        self.recipe_title = recipe_title
        self.dc = dc

    def execute(self):
        print(self.dc.deleteRecipe(self.recipe_title))