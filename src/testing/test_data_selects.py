import unittest
import logging
import datetime

from controller.dataControllerv2 import DataController2 as DataController
from model.enums.scripts import SelectScripts

TESTDB = 'lazygrocer'

class TestDataSelects(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.ingredients = [
            ('Spaghetti', 'Mac', "Half a package"),
            ('Parmesan Cheese', 'Mac', "1 cup"),
            ('Black Pepper', 'Mac', "1 teaspoon")
        ]
        self.dc = DataController(TESTDB)
        self.dc.connect()

    def test_select_recipe(self):
        result = self.dc.procedure('read_recipe', ('Mac', ))
        logging.debug(result)
        assert result == [[('Mac', 'Cheesier and delicious!', datetime.date(2024, 4, 17), 5, 'Greater recipe!', '12 min', '5 min', 5, 1500)]]
 
    @classmethod
    def tearDownClass(self):
        self.dc.disconnect()
'''
    def test_select_ingredient(self):
        result = self.dc.fetch(SelectScripts.INGREDIENT)
        assert sorted(result) == sorted(self.ingredients)

    def test_select_instruction(self):
        result = self.dc.fetch(SelectScripts.INSTRUCTION)
        logging.debug(result)
        assert result == [('Pasta Carbonara', 20, 4, 500, '1. Cook pasta. 2. Fry bacon. 3. Mix eggs and cheese sauce.', 'https://www.allrecipes.com/recipe/11973/spaghetti-carbonara-ii/')]

    def test_select_recipe_list(self):
        result = self.dc.fetch(SelectScripts.RECIPELIST)
        logging.debug(result)
        assert result == [('Italian', 'List of italian recipes')]

    def test_select_ingredient_list(self):
        result = self.dc.fetch(SelectScripts.INGREDIENTLIST)
        logging.debug(result)
        assert result == [('Essentials', 'List of essential ingredients')]

    def test_select_r_includes_i(self):
        result = self.dc.fetch(SelectScripts.RINCLUDESI)
        logging.debug(result)
        assert result != []

    def test_select_r_in_rl(self):
        result = self.dc.fetch(SelectScripts.RINRL)
        logging.debug(result)
        assert result == [('Pasta Carbonara', 'Italian')]

    def test_select_il_for_i(self):
        result = self.dc.fetch(SelectScripts.ILFORI)
        logging.debug(result)
        assert result == [('Essentials', 'Spaghetti')]
''' 
