from commands import Command

class ReadFavoritesCommand(Command):
    def __init__(self, dc):
        self.dc = dc

    def execute(self):
        print(self.dc.getFavorites())