from datetime import datetime
import unittest
import logging

from controller.dataControllerv2 import DataController2 as DataController
from model.enums.scripts import InsertScripts

TESTDB = 'lazygrocer'

class TestDataInserts(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.dc = DataController(TESTDB)
        self.dc.connect()
        self.date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.ingredients = [
            ('Spaghetti', 'Mac', "Half a package", self.date),
            ('Parmesan Cheese', 'Mac', "1 cup", self.date),
            ('Black Pepper', 'Mac', "1 teaspoon", self.date)
        ]

    def test_Ainsert_recipe(self):
        recipe_data = ('Mac', 'Cheesy and delicious!', self.date)
        result = self.dc.procedure('add_recipe', recipe_data)
        assert result != -1
    
    def test_Binsert_rating(self):
        rating_data = ('Mac', 4, 'Great recipe!', self.date) 
        result = self.dc.procedure('add_rating', rating_data)
        assert result != -1

    def test_Cinsert_step(self):
        step_data = [('Mac', 1, 'Bring water to boil.'), ('Mac', 2, 'Add pasta.')] 
        result = []
        for step in step_data:
            result.append(self.dc.procedure('add_step', step))
        assert result != -1
    
    def test_Dinsert_instruction(self):
        inst_data = ('Mac', '10 min', '5 min', 4, 1200)
        result = self.dc.procedure('add_instruction', inst_data)
        assert result != -1

    def test_Einsert_recipe_list(self):
        rl_data = ('Pastas', 'For the italians')
        result = self.dc.procedure('add_recipe_list', rl_data)
        assert result != -1

    def test_Finsert_recipe_to_list(self):
        rl_data = ('Mac', 'Pastas')
        result = self.dc.procedure('add_recipe_to_list', rl_data)
        assert result != -1

    def test_Ginsert_grocery_list(self):
        gl_data = ('Busy Week', 'For when time is running low')
        result = self.dc.procedure('add_grocery_list', gl_data)
        assert result != -1
    
    def test_Hinsert_ingredient(self):
        for ingredient in self.ingredients:
            result = self.dc.procedure('add_ingredient_to_recipe', ingredient)
            assert result != -1
            logging.debug("Ingredient added: %s", str(ingredient[0]))

    def test_Iinsert_ingredient_to_list(self):
        gl_data = ('Parmesan Cheese', 'Busy Week')
        result = self.dc.procedure('add_ingredient_to_grocery_list', gl_data)
        assert result != -1

    
    def test_Jupdate_recipe(self):
        recipe_data = ('Mac', 'Mac', 'Cheesier and delicious!', self.date)
        result = self.dc.procedure('update_recipe', recipe_data)
        assert result != -1

    def test_Kupdate_rating(self):
        rating_data = ('Mac', 5, 'Greater recipe!', self.date) 
        result = self.dc.procedure('update_rating', rating_data)
        assert result != -1

    def test_Lupdate_instruction(self):
        inst_data = ('Mac', '12 min', '5 min', 5, 1500)
        result = self.dc.procedure('update_instruction', inst_data)
        assert result != -1
    
    def test_Mupdate_step(self):
        step_data = ('Mac', 1, 'Bring water to boil.') 
        result = self.dc.procedure('update_step', step_data)
        assert result != -1

    def test_Nupdate_favorite(self):
        fav = ('Mac', self.date, 'Incredible dish, would recommend')
        result = self.dc.procedure('update_favorite', fav)
        assert result != -1

    @classmethod
    def tearDownClass(self):
        self.dc.disconnect()
