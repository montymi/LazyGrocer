from enum import Enum 

class Scripts(Enum):
    def __init__(self, script: str, params: int):
        self.script = script
        self.params = params

class InsertScripts(Scripts):

    # entities
    RECIPE = ( "INSERT INTO Recipe (title, description, rating, meal_timing, favorite, date_published) VALUES (?, ?, ?, ?, ?, ?);", 6 )
    INGREDIENT = ( "INSERT INTO Ingredient (name, inventory, last_added) VALUES (?, ?, ?);", 3 )
    INSTRUCTION = ( "INSERT INTO Instruction (recipe_title, cook_time, servings, calories, steps, url) VALUES (?, ?, ?, ?, ?, ?);", 6 )
    RECIPELIST = ( "INSERT INTO RecipeList (name, description) VALUES (?, ?);", 2 )
    INGREDIENTLIST = ( "INSERT INTO IngredientList (name, description) VALUES (?, ?);", 2 )

    # relationships
    RINCLUDESI = ( "INSERT INTO RincludesI (recipe_title, ingredient_name, quantity) VALUES (?, ?, ?);", 3 )
    RLCONTAINSR = ( "INSERT INTO RLcontainsR (recipe_title, recipe_list_name) VALUES (?, ?);", 2 )
    ILFORI = ( "INSERT INTO ILforI (ingredient_list_name, ingredient_name) VALUES (?, ?);", 2 )

class SelectScripts(Scripts):

    # entities
    RECIPES = ( "SELECT * FROM Recipe;", 0 )
    INGREDIENTS = ( "SELECT * FROM Ingredient;", 0 )
    INSTRUCTIONS = ( "SELECT * FROM Instruction;", 0 )
    RECIPELISTS = ( "SELECT * FROM RecipeList;", 0 )
    INGREDIENTLISTS = ( "SELECT * FROM IngredientList;", 0 )

    # relationships
    RINCLUDESI = ( "SELECT * FROM RincludesI;", 0 )
    RLCONTAINSR = ( "SELECT * FROM RLcontainsR;", 0 )
    ILFORI = ( "SELECT * FROM ILforI;", 0 )