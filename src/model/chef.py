import logging

from controller.dataControllerv2 import DataController2 as DataController
from model.ingredient import Ingredient 
from model.recipe import Recipe
from model.recipeList import RecipeList
from model.ingredientList import IngredientList
from model.enums.scripts import ChefScripts, SelectScripts

USER = 'default'
DB = 'lazygrocer'
FAVORITES = 'Favorites'

class Chef:
    def __init__(self, dc: DataController, username: str=USER, database: str=DB, favorites_name: str=FAVORITES):
        self.dc = dc
        self.favorites = RecipeList(favorites_name)
        self.recipes = RecipeList()
        self.ingredients = IngredientList()
        self.username = username
        self.database = database
        self.recipe_lists: list[RecipeList] = [self.recipes, self.favorites]
        self.ingredient_lists: list[IngredientList] = [self.ingredients]

    def load(self):
        self.loadFavorites()
        self.loadRecipes()
        self.loadIngredients()

    def addRecipe(self, title: str, description: str, rating: int, meal_timing: str, favorite: bool=False, date_published: str=None, url: str='') -> None:
        new_recipe = Recipe(title, description, rating, meal_timing, favorite, date_published, url)
        self.recipes.add_recipe(new_recipe)
    
    def getRecipeLists(self) -> list | None:
        result = self.dc.fetch(ChefScripts.GET_RECIPE_LISTS.script)
        return [ {"name": row['name'], "recipe_count": row['recipe_count']} for row in result ] if result else None

    def getIngredientLists(self) -> list | None:
        result = self.execute_query(ChefScripts.GET_INGREDIENT_LISTS.script)
        return [ {"name": row['name'], "ingredient_count": row['ingredient_count']} for row in result ] if result else None

    def loadFavorites(self) -> None:
        result = self.dc.fetch(ChefScripts.LOAD_FAVORITES.script)
        [ self.favorites.add_recipe(self._create_recipe_from_row(row)) for row in result ]
    
    def loadRecipes(self) -> None:
        result = self.dc.fetch(SelectScripts.RECIPES.script)
        [ self.recipes.add_recipe(self._create_recipe_from_row(row)) for row in result ]

    def loadIngredients(self) -> None:
        result = self.dc.fetch(SelectScripts.INGREDIENTS.script)
        [ self.ingredients.add_ingredient(self._create_ingredient_from_row(row)) for row in result ]

    def updateProfile(self, username: str= USER, database: str= DB) -> None:
        self.username = username
        self.database = database

    def _create_recipe_from_row(self, row) -> Recipe:
        return Recipe(row['title'], row['description'], row['rating'], row['meal_timing'], row['favorite'], row['date_published'])

    def _create_ingredient_from_row(self, row) -> Ingredient:
        return Ingredient(row['name'], row['inventory'], row['last_added'])