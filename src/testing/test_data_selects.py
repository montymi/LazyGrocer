import unittest
import logging

from controller.dataController import DataController
from model.enums.scripts import SelectScripts

class TestDataSelects(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.dc = DataController(r"../artifacts/test.db")
        self.dc.connect()

    def test_select_recipe(self):
        result = self.dc.fetch(SelectScripts.RECIPE)
        logging.debug(result)
        assert result == [('Pasta Carbonara', 'Classic Italian pasta dish with bacon, eggs, and cheese sauce', 4, 'DINNER', True, '2024-03-03')]

    def test_select_ingredient(self):
        result = self.dc.fetch(SelectScripts.INGREDIENT)
        logging.debug(result)
        assert result == [
            ('Spaghetti', "Half a package", '2024-03-03'),
            ('Bacon', "3 strips", '2024-03-03'),
            ('Eggs', "3 whole", '2024-03-03'),
            ('Parmesan Cheese', "1 cup", '2024-03-03'),
            ('Black Pepper', "1 teaspoon", '2024-03-03')]

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
    
    @classmethod
    def tearDownClass(self):
        self.dc.disconnect()