from commands.Command import Command

class ReadRecipeListCommand(Command):
    def __init__(self, recipe_list_title, dc):
        self.recipe_list_title = recipe_list_title
        self.dc = dc

    def execute(self):
        print(self.dc.procedure('get_recipes_by_list_name', (self.recipe_list_title, )))
