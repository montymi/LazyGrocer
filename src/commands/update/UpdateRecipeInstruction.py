from commands.Command import Command

class UpdateRecipeInstructionCommand(Command):
    def __init__(self, recipe_title, cook_time, prep_time, servings, calories, dc):
        self.recipe_title = recipe_title
        self.cook_time = cook_time
        self.prep_time = prep_time
        self.servings = servings 
        self.calories = calories
        self.dc = dc

    def execute(self):
        print(self.dc.procedure('update_instruction', (self.recipe_title, self.cook_time, self.prep_time, self.servings, self.calories)))
