from datetime import datetime
import unittest
import logging

from controller.dataControllerv2 import DataController2 as DataController
from model.enums.scripts import InsertScripts

TESTDB = 'testgrocer'

class TestDataInserts(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.dc = DataController(TESTDB)
        self.dc.clean()
        self.dc.connect()
        self.ingredients = [
            ('Spaghetti', "Half a package", '2024-03-05'),
            ('Bacon', "3 strips", '2024-03-05'),
            ('Eggs', "3 whole", '2024-03-05'),
            ('Parmesan Cheese', "1 cup", '2024-03-05'),
            ('Black Pepper', "1 teaspoon", '2024-03-05')
        ]

    def date(date_string):
        try:
            date_obj = datetime.strptime(date_string, '%Y-%m-%d').date()
            return (date_obj,)
        except ValueError:
            logging.error("Invalid date format. Please provide a date in the format YYYY-MM-DD.")
            return None
    

    def test_Ainsert_recipe(self):
        recipe_data = ('Pasta Carbonara', 'Classic Italian pasta dish with bacon, eggs, and cheese sauce', 4, 'DINNER', True, '2024-03-05')
        result = self.dc.execute(InsertScripts.RECIPE, recipe_data)
        assert result != -1

    def test_Binsert_ingredient(self):
        for ingredient in self.ingredients:
            result = self.dc.execute(InsertScripts.INGREDIENT, ingredient)
            assert result != -1
            logging.debug("Ingredient added: %s", str(ingredient[0]))

    def test_Cinsert_instruction(self):
        instruction_data = ('Pasta Carbonara', 20, 4, 500, '1. Cook pasta. 2. Fry bacon. 3. Mix eggs and cheese sauce.', 'https://www.allrecipes.com/recipe/11973/spaghetti-carbonara-ii/')
        result = self.dc.execute(InsertScripts.INSTRUCTION, instruction_data)
        assert result != -1

    def test_Dinsert_recipe_list(self):
        recipe_list_data = ('Italian', 'List of italian recipes')
        result = self.dc.execute(InsertScripts.RECIPELIST, recipe_list_data)
        assert result != -1

    def test_Einsert_ingredient_list(self):
        ingredient_list_data = ('Essentials', 'List of essential ingredients')
        result = self.dc.execute(InsertScripts.INGREDIENTLIST, ingredient_list_data)
        assert result != -1

    def test_Finsert_r_includes_i(self):
        for data in self.ingredients:
            result = self.dc.execute(InsertScripts.RINCLUDESI, ('Pasta Carbonara', data[0], data[1]))
            assert result != -1

    def test_Ginsert_r_in_rl(self):
        rl_contains_r_data = ('Pasta Carbonara', 'Italian')
        result = self.dc.execute(InsertScripts.RINRL, rl_contains_r_data)
        assert result != -1

    def test_Hinsert_il_for_i(self):
        il_for_i_data = ('Essentials', 'Spaghetti')
        result = self.dc.execute(InsertScripts.ILFORI, il_for_i_data)
        assert result != -1

    @classmethod
    def tearDownClass(self):
        self.dc.disconnect()

