from commands import Command

class CreateGroceryListCommand(Command):
    def __init__(self, grocery_list_title, description, dc):
        self.grocery_list_title = grocery_list_title
        self.description = description
        self.dc = dc

    def execute(self):
        print(self.dc.createGrocerylist(self.grocery_list_title, self.description))