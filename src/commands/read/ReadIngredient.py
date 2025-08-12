from commands.Command import Command

class ReadIngredientCommand(Command):
    def __init__(self, ingredient_title, dc):
        self.ingredient_title = ingredient_title
        self.dc = dc

    def execute(self):
        print(self.dc.procedure('read_ingredient', (self.ingredient_title, )))
