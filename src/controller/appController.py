import logging

from commands.create.CreateRecipe import CreateRecipeCommand
from commands.create.CreateRecipeIngredient import CreateRecipeIngredientCommand
from commands.create.CreateRecipeRating import CreateRecipeRatingCommand
from commands.create.CreateRecipeStep import CreateRecipeStepCommand
from commands.create.CreateRecipeInstruction import CreateRecipeInstructionCommand
from commands.create.CreateRecipeList import CreateRecipeListCommand
from commands.create.CreateGroceryList import CreateGroceryListCommand
from commands.read.ReadAllIngredients import ReadAllIngredientsCommand
from commands.read.ReadAllRecipes import ReadAllRecipesCommand
from commands.read.ReadAllGroceryLists import ReadAllGroceryListsCommand
from commands.read.ReadFavorites import ReadFavoritesCommand
from commands.read.ReadIngredient import ReadIngredientCommand
from commands.read.ReadRecipe import ReadRecipeCommand
from commands.read.ReadRecipeIngredients import ReadRecipeIngredientsCommand
from commands.read.ReadRecipeList import ReadRecipeListCommand
from commands.read.ReadSteps import ReadStepsCommand
from commands.read.ReadGroceryList import ReadGroceryListCommand
from commands.update.UpdateRecipe import UpdateRecipeCommand
from commands.update.UpdateFavorite import UpdateFavoriteCommand
from commands.update.UpdateRecipeInstruction import UpdateRecipeInstructionCommand
from commands.update.UpdateRecipeRating import UpdateRecipeRatingCommand
from commands.update.UpdateRecipeStep import UpdateRecipeStepCommand
from commands.delete.DeleteRecipe import DeleteRecipeCommand
from commands.delete.DeleteFavorite import DeleteFavoriteCommand
from commands.delete.DeleteRecipeList import DeleteRecipeListCommand
from commands.delete.DeleteGroceryList import DeleteGroceryListCommand

logging.basicConfig()


class AppController:
    def __init__(self, dc):
        self.dc = dc
        self._create_services_ = ['Add Recipe', 'Add Ingredient to Recipe', 'Add Rating', 'Add Step', 'Add Instruction', 'Add Recipe List', 'Add Grocery List']
        self._read_services_ = ['All Recipes', 'All Ingredients', 'Recipe', 'Ingredient', 'Recipe List', 'All Grocery Lists', 'Grocery List', 'Recipe Steps', 'Favorites', 'Recipe/s Ingredients']
        self._update_services_ = ['update_recipe', 'update_rating', 'update_instruction', 'update_step', 'update_favorite']
        self._delete_services_ = ['delete_recipe', 'delete_recipe_list', 'delete_grocery_list', 'delete_recipe_from_favorites']
        self.dc.connect()

    def start(self):
        print("Select Service:\n1. Create\n2. Read\n3. Update\n4. Delete\n5. Quit")
        service = input("Service ID: ")
        self._handle_service_(service)

    def _handle_service_(self, service):
        if int(service) == 1: # create
            self.create()
        elif int(service) == 2: # read
            self.read()
        elif int(service) == 3: # update
            self.update()
        elif int(service) == 4: # delete
            self.delete()
        elif int(service) == 5:
            quit()
        else:
            logging.error("Invalid Input")
            self.start()

    def create(self):
        print("Select CREATE Service")
        for index, service in enumerate(self._create_services_):
            print(f'{index+1}. {service}')
        c_service = input("CREATE ID: ")
        self._handle_create_service_(c_service)

    def _handle_create_service_(self, service):
        iService = int(service)
        if iService == 1: # recipe
            recipe_title = input("Recipe Title: ")
            desc = input("Description: ")
            command = CreateRecipeCommand(recipe_title, desc, self.dc)
            command.execute()
        elif iService == 2: # ingredient to recipe
            recipe_title = input("Recipe Title: ")
            num_ingredients = int(input("Number of ingredients to add: "))
            for _ in range(0, num_ingredients):
                ingredient = input("Ingredient: ")
                quantity = input("Quantity: ")
                command = CreateRecipeIngredientCommand(ingredient, recipe_title, quantity, self.dc)
                command.execute()
        elif iService == 3: # rating
            recipe_title = input("Recipe Title: ")
            score = int(input("Score (int): "))
            desc = input("Description: ")
            command = CreateRecipeRatingCommand(recipe_title, score, desc, self.dc)
        elif iService == 4: # step
            recipe_title = input("Recipe Title: ")
            num_steps = int(input("Number of steps to add: "))
            for index in range(1, num_steps+1):
                step_id = index
                desc = input("Description: ")
                command = CreateRecipeStepCommand(recipe_title, step_id, desc)
                command.execute()
        elif iService == 5: # instruction
            recipe_title = input("Recipe Title: ")
            cook_time = input("Cook Time: ")
            prep_time = input("Prep Time: ")
            servings = int(input("Servings: ")) | 0
            calories = int(input("Calories: ")) | 0
            command = CreateRecipeInstructionCommand(recipe_title, cook_time, prep_time, servings, calories, self.dc)
            command.execute()
        elif iService == 6: # recipe list
            rl_name = input("Recipe List Name: ")
            desc = input("Description: ")
            command = CreateRecipeListCommand(rl_name, desc, self.dc)
            command.execute()
        elif iService == 7: # grocery list
            gl_name = input("Grocery List Name: ")
            desc = input("Description: ")
            command = CreateGroceryListCommand(gl_name, desc, self.dc)
            command.execute()
        else:
            logging.error("Invalid Input")
            self.create()

    def read(self):
        print("Select READ Service")
        for index, service in enumerate(self._read_services_):
            print(f'{index+1}. {service}')
        serv = input("READ ID: ")
        self._handle_read_service_(serv)

    def _handle_read_service_(self, service):
        iService = int(service)
        if iService == 1: # all recipes
            command = ReadAllRecipesCommand(self.dc)
            command.execute()
        elif iService == 2: # all ingredients 
            command = ReadAllIngredientsCommand(self.dc)
            command.execute()
        elif iService == 3: # recipe
            recipe_title = input("Recipe Title: ")
            command = ReadRecipeCommand(recipe_title, self.dc)
            command.execute()
        elif iService == 4: # ingredient
            ingredient = input("Ingredient: ")
            command = ReadIngredientCommand(ingredient, self.dc)
            command.execute()
        elif iService == 5: # recipe list
            rl_name = input("Recipe List Name: ")
            command = ReadRecipeListCommand(rl_name, self.dc)
            command.execute()
        elif iService == 6: # all grocery lists
            command = ReadAllGroceryListsCommand(self.dc)
            command.execute()
        elif iService == 7: # grocery list
            gl_name = input("Grocery List: ")
            command = ReadGroceryListCommand(gl_name, self.dc)
            command.execute()
        elif iService == 8: # steps
            recipe = input("Recipe Title: ")
            command = ReadStepsCommand(recipe, self.dc)
        elif iService == 9: # favorites 
            command = ReadFavoritesCommand(self.dc)
            command.execute()
        elif iService == 10: # recipe/s to ingredient list
            recipes = input("Recipe/s (comma separated): ")
            command = ReadRecipeIngredientsCommand(recipes, self.dc)
            command.execute()
        else:
            logging.error("Invalid Input")
            self.create()

    def update(self):
        print("Select UPDATE Service")
        for index, service in enumerate(self._update_services_):
            print(f'{index+1}. {service}')
        u_service = input("UPDATE ID: ")
        self._handle_update_service_(u_service)
        
    def _handle_update_service_(self, service):
        iService = int(service)
        if iService == 1:
            old_recipe_title = input("Old Recipe Title: ")
            new_recipe_title = input("New Recipe Title: ")
            new_recipe_description = input("New Description: ")
            command = UpdateRecipeCommand(old_recipe_title, new_recipe_title, new_recipe_description, self.dc)
            command.execute()
        elif iService == 2:
            recipe_title = input("Recipe Title: ")
            new_score = input("New Score: ")
            new_rating_description = input("New Description: ")
            command = UpdateRecipeRatingCommand(recipe_title, new_score, new_rating_description, self.dc)
            command.execute()
        elif iService == 3:
            recipe_title = input("Recipe Title: ")
            new_cook_time = input("New Cook Time: ")
            new_prep_time = input("New Prep Time: ")
            new_servings = input("New Servings: ")
            new_calories = input("New Calories: ")
            command = UpdateRecipeInstructionCommand(recipe_title, new_cook_time, new_prep_time, new_servings, new_calories, self.dc)
            command.execute()
        elif iService == 4:
            recipe_title = input("Recipe Title: ")
            step_id = input("Step ID: ")
            new_step_description = input("New Description: ")
            command = UpdateRecipeStepCommand(recipe_title, step_id, new_step_description, self.dc)
            command.execute()
        elif iService == 5:
            recipe_title = input("Recipe Title: ")
            new_description = input("Description: ")
            command = UpdateFavoriteCommand(recipe_title, new_description, self.dc)
            command.execute()
        else:
            logging.error("Invalid Input")
            self.update()

    def delete(self):
        print("Select DELETE Service")
        for index, service in enumerate(self._delete_services_):
            print(f'{index+1}. {service}')
        d_service = input("DELETE ID: ")
        self._handle_delete_service_(d_service)
        
    def _handle_delete_service_(self, service):
        iService = int(service)
        if iService == 1:
            del_recipe_title = input("Recipe Title: ")
            deleteRecipeCommand = DeleteRecipeCommand(del_recipe_title, self.dc)
            deleteRecipeCommand.execute()
        elif iService == 2:
            list_name = input("Recipe List Name: ")
            deleteRecipeCommand = DeleteRecipeListCommand(list_name, self.dc)
            deleteRecipeCommand.execute()
        elif iService == 3:
            list_name = input("Recipe List Name: ")
            deleteRecipeCommand = DeleteGroceryListCommand(list_name, self.dc)
            deleteRecipeCommand.execute()
        elif iService == 4:
            del_recipe_title = input("Recipe Title: ")
            deleteRecipeCommand = DeleteFavoriteCommand(del_recipe_title, self.dc)
            deleteRecipeCommand.execute()
        else:
            logging.error("Invalid Input")
            self.delete()
