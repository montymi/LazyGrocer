from datetime import datetime
from commands import Command

class CreateRecipeRatingCommand(Command):
    def __init__(self, recipe_title, score, description, date, dc):
        self.recipe_title = recipe_title
        self.score = score
        self.description = description
        self.date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.dc = dc

    def execute(self):
        print(self.dc.createRecipeRating(self.recipe_title, self.score, self.description, self.date))