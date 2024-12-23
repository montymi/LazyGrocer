from commands.Command import Command

class UpdateGroceryListCommand(Command):
    def __init__(self, ingredient_title, grocery_list_title, dc):
        self.ingredient_title = ingredient_title
        self.grocery_list_title = grocery_list_title
        self.dc = dc

    def execute(self):
        print(self.dc.procedure('add_ingredient_to_grocery_list', (self.ingredient_title, self.grocery_list_title)))
