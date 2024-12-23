from datetime import datetime
from commands.Command import Command

class CreateRecipeRatingCommand(Command):
    def __init__(self, recipe_title, score, description, dc):
        self.recipe_title = recipe_title
        self.score = score
        self.description = description
        self.date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.dc = dc

    def execute(self):
        print(self.dc.procedure('add_recipe_rating', (self.recipe_title, self.score, self.description, self.date)))
