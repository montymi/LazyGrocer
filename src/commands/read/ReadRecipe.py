from commands.Command import Command

class ReadRecipeCommand(Command):
    def __init__(self, recipe_title, dc):
        self.recipe_title = recipe_title
        self.dc = dc

    def execute(self):
        print(self.dc.procedure('read_recipe', (self.recipe_title, )))
