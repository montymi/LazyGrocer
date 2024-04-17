from commands import Command

class ReadAllIngredientsCommand(Command):
    def __init__(self, dc):
        self.dc = dc

    def execute(self):
        print(self.dc.getAllIngredients())
