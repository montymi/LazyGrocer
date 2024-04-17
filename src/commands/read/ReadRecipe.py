from commands import Command

class ReadRecipeCommand(Command):
    def __init__(self, recipe_title, dc):
        self.recipe_title = recipe_title
        self.dc = dc

    def execute(self):
        print(self.dc.readRecipe(self.read_title))

# Similarly, create command classes for other operations like AddRecipeCommand, UpdateRecipeCommand, etc.