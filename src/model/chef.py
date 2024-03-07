from controller.dataControllerv2 import DataController2 as DataController

USER='default'
DB='lazygrocer'

class Chef:
    def __init__(self, dc: DataController, username: str=USER, database: str=DB):
        self.dc = dc
        self.username = username
        self.database = database 

    # favorites 
    def read_favorites(self):
        pass
    
    # recipe list 
    def create_recipe_list(self, name: str, desc: str='', recipes: tuple=()):
        pass 

    def read_recipe_list(self, name: str):
        pass 

    def update_recipe_list(self, name: str, desc: str='', recipes: tuple=()):
        pass 

    def delete_recipe_list(self, name: str): 
        pass 

    # ingredient list 
    def create_ingredient_list():
        pass

    def read_ingredient_list():
        pass 

    def update_ingredient_list():
        pass 

    def delete_ingredient_list(): 
        pass 