from commands import Command

class UpdateRecipeStepCommand(Command):
    def __init__(self, recipe_title, step_id, description, dc):
        self.recipe_title = recipe_title
        self.step_id = step_id
        self.description = description
        self.dc = dc

    def execute(self):
        print(self.dc.updateRecipeStep(self.recipe_title, self.step_id, self.description))