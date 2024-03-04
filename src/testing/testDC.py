import unittest
import logging

from LazyGrocer.src.controller.dataController import DataController
from LazyGrocer.src.model.enums.scripts import InsertScripts

logging.basicConfig(level=logging.DEBUG)

class TestDataController(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.dc = DataController()
        self.dc.connect()
        self.dc.read()

        self.ingredients = [
            ('Spaghetti', 10, '2024-03-03'),
            ('Bacon', 5, '2024-03-03'),
            ('Eggs', 6, '2024-03-03'),
            ('Parmesan Cheese', 3, '2024-03-03'),
            ('Black Pepper', 1, '2024-03-03')
        ]

    @classmethod
    def tearDownClass(self):
        self.dc.disconnect()

    def test_insert_recipe(self):
        recipe_data = ('Pasta Carbonara', 'Classic Italian pasta dish with bacon, eggs, and cheese sauce', 4, 'DINNER', True, '2024-03-03')
        result = self.dc.execute(InsertScripts.RECIPE, recipe_data)
        assert result != -1

    def test_insert_ingredient(self):
        for ingredient, inventory, date_created in self.ingredients:
            logging.info("Ingredient added:", ingredient)
            result = self.dc.execute(InsertScripts.INGREDIENT, ingredient)
            assert result != -1

    def test_insert_instruction(self):
        instruction_data = ('Pasta Carbonara', 20, 4, 500, '1. Cook pasta. 2. Fry bacon. 3. Mix eggs and cheese sauce.', 'https://www.allrecipes.com/recipe/11973/spaghetti-carbonara-ii/')
        result = self.dc.execute(InsertScripts.INSTRUCTION, instruction_data)
        assert result != -1

    def test_insert_recipe_list(self):
        recipe_list_data = ('Italian', 'List of italian recipes')
        result = self.dc.execute(InsertScripts.RECIPELIST, recipe_list_data)
        assert result != -1

    def test_insert_ingredient_list(self):
        ingredient_list_data = ('Essentials', 'List of essential ingredients')
        result = self.dc.execute(InsertScripts.INGREDIENTLIST, ingredient_list_data)
        assert result != -1

    def test_insert_r_includes_i(self):
        for ingredient, inventory, date_created in self.ingredients:
            result = self.dc.execute(InsertScripts.RINCLUDESI, ('Pasta Carbonara', ingredient))
            assert result != -1

    def test_insert_r_in_rl(self):
        rl_contains_r_data = ('Pasta Carbonara', 'Italian')
        result = self.dc.execute(InsertScripts.RLCONTAINSR, rl_contains_r_data)
        assert result != -1

    def test_insert_il_for_i(self):
        il_for_i_data = ('Essentials', 'Spaghetti')
        result = self.dc.execute(InsertScripts.ILFORI, il_for_i_data)
        assert result != -1

if __name__ == '__main__':
    logging.info("Running tests")
    unittest.main()