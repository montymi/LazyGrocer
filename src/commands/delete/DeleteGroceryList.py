from commands import Command

class DeleteGroceryListCommand(Command):
    def __init__(self, grocery_list_title, dc):
        self.grocery_list_title = grocery_list_title
        self.dc = dc

    def execute(self):
        print(self.dc.deleteGroceryList(self.grocery_list_title))