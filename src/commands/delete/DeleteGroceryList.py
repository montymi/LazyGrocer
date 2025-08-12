from commands.Command import Command

class DeleteGroceryListCommand(Command):
    def __init__(self, grocery_list_title, dc):
        self.grocery_list_title = grocery_list_title
        self.dc = dc

    def execute(self):
        print(self.dc.procedure('delete_grocery_list', (self.grocery_list_title, )))
