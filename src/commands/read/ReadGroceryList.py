from commands.Command import Command

class ReadGroceryListCommand(Command):
    def __init__(self, grocery_list_title, dc):
        self.grocery_list_title = grocery_list_title
        self.dc = dc

    def execute(self):
        print(self.dc.procedure('read_all_grocery_lists', (self.grocery_list_title, )))
