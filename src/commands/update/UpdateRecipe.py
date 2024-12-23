from datetime import datetime
from commands.Command import Command

class UpdateRecipeCommand(Command):
    def __init__(self, old_recipe_title, recipe_title, description, dc):
        self.old_recipe = old_recipe_title
        self.recipe_title = recipe_title
        self.description = description
        self.date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.dc = dc

    def execute(self):
        print(self.dc.procedure('update_recipe', (self.old_recipe, self.recipe_title, self.description, self.date)))
