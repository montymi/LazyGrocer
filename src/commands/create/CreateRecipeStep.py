from commands import Command

class CreateRecipeStepCommand(Command):
    def __init__(self, recipe_title, description, dc):
        self.recipe_title = recipe_title
        self.description = description
        self.dc = dc

    def execute(self):
        print(self.dc.createRecipeStep(self.recipe_title, self.description))