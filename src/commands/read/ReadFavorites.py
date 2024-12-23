from commands.Command import Command

class ReadFavoritesCommand(Command):
    def __init__(self, dc):
        self.dc = dc

    def execute(self):
        print(self.dc.procedure('get_all_favorites'))
