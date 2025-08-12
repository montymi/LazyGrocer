from commands.Command import Command

class CreateRecipeListCommand(Command):
    def __init__(self, recipe_list_title, description, dc):
        self.recipe_list_title = recipe_list_title
        self.description = description
        self.dc = dc

    def execute(self):
        print(self.dc.procedure('add_recipe_list', (self.recipe_list_title, self.description)))
