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
        assert result != []

    def test_select_ingredient(self):
        result = self.dc.fetch(SelectScripts.INGREDIENT)
        logging.debug(result)
        assert result != []

    def test_select_instruction(self):
        result = self.dc.fetch(SelectScripts.INSTRUCTION)
        logging.debug(result)
        assert result != []

    def test_select_recipe_list(self):
        result = self.dc.fetch(SelectScripts.RECIPELIST)
        logging.debug(result)
        assert result != []

    def test_select_ingredient_list(self):
        result = self.dc.fetch(SelectScripts.INGREDIENTLIST)
        logging.debug(result)
        assert result != []

    def test_select_r_includes_i(self):
        result = self.dc.fetch(SelectScripts.RINCLUDESI)
        logging.debug(result)
        assert result != []

    def test_select_r_in_rl(self):
        result = self.dc.fetch(SelectScripts.RINRL)
        logging.debug(result)
        assert result != []

    def test_select_il_for_i(self):
        result = self.dc.fetch(SelectScripts.ILFORI)
        logging.debug(result)
        assert result != []
    
    @classmethod
    def tearDownClass(self):
        self.dc.disconnect()