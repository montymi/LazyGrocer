from commands.Command import Command

class ReadStepsCommand(Command):
    def __init__(self, recipe_title, dc):
        self.recipe_title = recipe_title
        self.dc = dc

    def execute(self):
        print(self.dc.procedure('get_recipe_steps', (self.recipe_title, )))
