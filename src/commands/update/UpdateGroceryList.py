from commands import Command

class UpdateGroceryListCommand(Command):
    def __init__(self, ingredient_title, grocery_list_title, dc):
        self.ingredient_title = ingredient_title
        self.grocery_list_title = grocery_list_title
        self.dc = dc

    def execute(self):
        print(self.dc.updateGroceryList(self.ingredient_title, self.grocery_list_title))