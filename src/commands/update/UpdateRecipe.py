from datetime import datetime

from commands import Command

class UpdateRecipeCommand(Command):
    def __init__(self, recipe_title, description, dc):
        self.recipe_title = recipe_title
        self.description = description
        self.date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.dc = dc

    def execute(self):
        print(self.dc.updateRecipe(self.recipe_title, self.description, self.date))