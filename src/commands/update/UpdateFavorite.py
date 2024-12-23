from commands.Command import Command
from datetime import datetime

class UpdateFavoriteCommand(Command):
    def __init__(self, recipe_title, description, dc):
        self.recipe_title = recipe_title
        self.description = description
        self.date = datetime.now().strftime('%Y-%m-%d')
        self.dc = dc

    def execute(self):
        print(self.dc.procedure('update_favorite', (self.recipe_title, self.description, self.date)))
