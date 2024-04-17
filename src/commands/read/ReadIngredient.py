from commands import Command

class ReadIngredientCommand(Command):
    def __init__(self, ingredient_title, dc):
        self.ingredient_title = ingredient_title
        self.dc = dc

    def execute(self):
        print(self.dc.getIngredient(self.ingredient_title))