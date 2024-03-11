from enum import Enum 

class Scripts(Enum):
    def __init__(self, script: str, params: int):
        self.script = script
        self.params = params

class InsertScripts(Scripts):

    # entities
    RECIPE = ( "INSERT INTO Recipe (title, description, rating, meal_timing, favorite, date_published) VALUES (%s, %s, %s, %s, %s, %s);", 6 )
    INSTRUCTION = ( "INSERT INTO Instruction (recipe_title, cook_time, servings, calories, steps, url) VALUES (%s, %s, %s, %s, %s, %s);", 6 )
    INGREDIENT = ( "INSERT INTO Ingredient (name, inventory, last_added) VALUES (%s, %s, %s);", 3 )
    RECIPELIST = ( "INSERT INTO RecipeList (name, description) VALUES (%s, %s);", 2 )
    INGREDIENTLIST = ( "INSERT INTO IngredientList (name, description) VALUES (%s, %s);", 2 )

    # relationships
    RINCLUDESI = ( "INSERT INTO RincludesI (recipe_title, ingredient_name, quantity) VALUES (%s, %s, %s);", 3 )
    RINRL = ( "INSERT INTO RinRL (recipe_title, recipe_list_name) VALUES (%s, %s);", 2 )
    ILFORI = ( "INSERT INTO ILforI (ingredient_list_name, ingredient_name) VALUES (%s, %s);", 2 )

class SelectScripts(Scripts):

    # entities
    RECIPE = ( "SELECT * FROM Recipe;", 0 )
    INGREDIENT = ( "SELECT * FROM Ingredient;", 0 )
    INSTRUCTION = ( "SELECT * FROM Instruction;", 0 )
    RECIPELIST = ( "SELECT * FROM RecipeList;", 0 )
    INGREDIENTLIST = ( "SELECT * FROM IngredientList;", 0 )

    # relationships
    RINCLUDESI = ( "SELECT * FROM RincludesI;", 0 )
    RINRL = ( "SELECT * FROM RinRL;", 0 )
    ILFORI = ( "SELECT * FROM ILforI;", 0 )

class ChefScripts(Scripts):
    GET_RECIPE_LISTS = ("SELECT name, COUNT(recipe_title) AS recipe_count FROM RinRL WHERE recipe_title IN (SELECT title FROM Recipe) GROUP BY recipe_list_name", 0)
    GET_INGREDIENT_LISTS = ("SELECT name, COUNT(ingredient_name) AS ingredient_count FROM ILforI GROUP BY ingredient_list_name", 0)
    LOAD_FAVORITES = ("SELECT * FROM Recipe WHERE favorite = 1", 0)
