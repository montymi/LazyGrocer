from commands.Command import Command

class CreateRecipeStepCommand(Command):
    def __init__(self, recipe_title, description, dc):
        self.recipe_title = recipe_title
        self.description = description
        self.dc = dc

    def execute(self):
        print(self.dc.procedure('add_recipe_step', (self.recipe_title, self.description)))
