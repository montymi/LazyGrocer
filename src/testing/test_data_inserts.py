import unittest
import logging

from controller.dataControllerv2 import DataController2 as DataController
from model.enums.scripts import InsertScripts

class TestDataInserts(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.dc = DataController("testgrocer")
        self.dc.connect()
        self.ingredients = [
            ('Spaghetti', "Half a package", '2024-03-03'),
            ('Bacon', "3 strips", '2024-03-03'),
            ('Eggs', "3 whole", '2024-03-03'),
            ('Parmesan Cheese', "1 cup", '2024-03-03'),
            ('Black Pepper', "1 teaspoon", '2024-03-03')
        ]

    def test_Ainsert_recipe(self):
        print("recipe")
        recipe_data = ('Pasta Carbonara', 'Classic Italian pasta dish with bacon, eggs, and cheese sauce', 4, 'DINNER', True, '2024-03-03')
        result = self.dc.execute(InsertScripts.RECIPE, recipe_data)
        assert result != -1

    def test_Binsert_ingredient(self):
        print("ingredient")
        for data in self.ingredients:
            print(data)
            logging.debug("Ingredient added: %s", str(data[0]))
            result = self.dc.execute(InsertScripts.INGREDIENT, data)
            assert result != -1

    def test_Cinsert_instruction(self):
        print("instruction")
        instruction_data = ('Pasta Carbonara', 20, 4, 500, '1. Cook pasta. 2. Fry bacon. 3. Mix eggs and cheese sauce.', 'https://www.allrecipes.com/recipe/11973/spaghetti-carbonara-ii/')
        result = self.dc.execute(InsertScripts.INSTRUCTION, instruction_data)
        assert result != -1

    def test_Dinsert_recipe_list(self):
        print("recipe list")
        recipe_list_data = ('Italian', 'List of italian recipes')
        result = self.dc.execute(InsertScripts.RECIPELIST, recipe_list_data)
        assert result != -1

    def test_Einsert_ingredient_list(self):
        print("ingredient list")
        ingredient_list_data = ('Essentials', 'List of essential ingredients')
        result = self.dc.execute(InsertScripts.INGREDIENTLIST, ingredient_list_data)
        assert result != -1

    def test_Finsert_r_includes_i(self):
        print("insert")
        for data in self.ingredients:
            result = self.dc.execute(InsertScripts.RINCLUDESI, ('Pasta Carbonara', data[0], data[1]))
            assert result != -1

    def test_Ginsert_r_in_rl(self):
        print("in")
        rl_contains_r_data = ('Pasta Carbonara', 'Italian')
        result = self.dc.execute(InsertScripts.RINRL, rl_contains_r_data)
        assert result != -1

    def test_Hinsert_il_for_i(self):
        print("for")
        il_for_i_data = ('Essentials', 'Spaghetti')
        result = self.dc.execute(InsertScripts.ILFORI, il_for_i_data)
        assert result != -1
    
    @classmethod
    def tearDownClass(self):
        self.dc.disconnect()

if __name__ == '__main__':
    unittest.main()
