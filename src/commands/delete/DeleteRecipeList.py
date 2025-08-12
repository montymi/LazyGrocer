from commands.Command import Command

class DeleteRecipeListCommand(Command):
    def __init__(self, recipe_list_title, dc):
        self.recipe_list_title = recipe_list_title
        self.dc = dc

    def execute(self):
        print(self.dc.procedure('delete_recipe_list', (self.recipe_list_title, )))
