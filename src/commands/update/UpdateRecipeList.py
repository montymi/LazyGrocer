from commands import Command

class UpdateRecipeListCommand(Command):
    def __init__(self, recipe_title, recipe_list_title, dc):
        self.recipe_title = recipe_title
        self.recipe_list_title = recipe_list_title
        self.dc = dc

    def execute(self):
        print(self.dc.updateRecipeList(self.recipe_title, self.recipe_list_title))