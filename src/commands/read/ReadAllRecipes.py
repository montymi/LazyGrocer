from commands.Command import Command

class ReadAllRecipesCommand(Command):
    def __init__(self, dc):
        self.dc = dc

    def execute(self):
        print(self.dc.procedure('read_all_recipes'))
