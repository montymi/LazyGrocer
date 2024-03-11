from datetime import datetime as dt
import logging

from model.enums.tables import MealTimings
from model.enums.scripts import InsertScripts
from model.ingredient import Ingredient
from model.instruction import Instruction

class Recipe: 
    def __init__(self, title: str, description: str, rating: int, meal_timing: str, favorite: bool=False, date_published: str=str(dt.now().strftime("%Y-%m-%d")), url: str=''):
        self.title = title
        self.description = description
        self.rating = rating 
        self.meal_timing = self._check_timing_(meal_timing)
        self.favorite = favorite 
        self.date_published = date_published
        self.ingredients: list[Ingredient] = []
        self.instructions = Instruction(title, url)
    
    def addIngredient(self, name: str, quantity: str):
        self.ingredients.append(Ingredient(name, quantity))
    
    def save(self, dc):
        if not all(ingredient.save() != -1 for ingredient in self.ingredients): 
            return -1
        elif self.instructions.save() == -1: return -1
        else: return self._save_to_db_(dc)
    
    def _save_to_db_(self, dc) -> bool:
        return dc.execute(InsertScripts.RECIPE, self._get_params_())

    def _get_params_(self) -> tuple:
        return (self.title, self.description, self.rating, self.meal_timing, self.favorite, self.date_published)
    
    def _check_timing_(self, timing: str):
        for time in MealTimings:
            if timing == time:
                logging.debug(f"{self.title} created with valid meal timing: {timing}")
                return timing
        logging.error(f"{self.title} created with invalid meal timing: {timing}")
        return None
