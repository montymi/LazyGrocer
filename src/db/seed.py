from src import create_app
from src.models.base import db
from src.models.recipe import Recipe, Instruction, Step, Rating
from src.models.ingredient import Ingredient
from src.models.grocery_list import GroceryList
from datetime import date, datetime


def seed_database():
    """Seed the database with sample data"""
    app = create_app()

    with app.app_context():
        # Clear existing data
        db.drop_all()
        db.create_all()

        # Create ingredients
        ingredients = [
            Ingredient(name="Chicken", last_added=date(2024, 4, 17)),
            Ingredient(name="Parmesan Cheese", last_added=date(2024, 4, 17)),
            Ingredient(name="Dough", last_added=date(2024, 4, 17)),
            Ingredient(name="Pizza Sauce", last_added=date(2024, 4, 17)),
            Ingredient(name="Mozzarella Cheese", last_added=date(2024, 4, 17)),
            Ingredient(name="Spaghetti", last_added=date(2024, 4, 17)),
            Ingredient(name="Black Pepper", last_added=date(2024, 4, 17)),
        ]

        for ingredient in ingredients:
            db.session.add(ingredient)

        # Create recipes
        recipes = [
            Recipe(
                title="Chicken Parm",
                description="So good!",
                date_published=date(2024, 4, 16),
            ),
            Recipe(
                title="Pizza",
                description="Cheat Meal",
                date_published=date(2024, 4, 17),
            ),
            Recipe(
                title="Mac",
                description="Cheesier and delicious!",
                date_published=date(2024, 4, 17),
            ),
        ]

        for recipe in recipes:
            db.session.add(recipe)

        db.session.commit()

        # Add instructions
        instructions = [
            Instruction(
                recipe_id=1,
                cook_time="20 mins",
                prep_time="15 mins",
                servings=3,
                calories=1000,
            ),
            Instruction(
                recipe_id=2,
                cook_time="25 mins",
                prep_time="10 mins",
                servings=3,
                calories=1000,
            ),
            Instruction(
                recipe_id=3,
                cook_time="12 mins",
                prep_time="5 mins",
                servings=5,
                calories=1500,
            ),
        ]

        for instruction in instructions:
            db.session.add(instruction)

        # Add steps
        steps = [
            Step(recipe_id=1, step_number=1, description="Cook chicken"),
            Step(recipe_id=1, step_number=2, description="Cook sauce"),
            Step(recipe_id=1, step_number=3, description="Melt cheese on top"),
            Step(recipe_id=2, step_number=1, description="Spread dough"),
            Step(recipe_id=2, step_number=2, description="Add toppings"),
            Step(recipe_id=2, step_number=3, description="Put in oven"),
            Step(recipe_id=3, step_number=1, description="Bring water to boil"),
            Step(recipe_id=3, step_number=2, description="Add pasta"),
        ]

        for step in steps:
            db.session.add(step)

        # Add ratings
        ratings = [
            Rating(
                recipe_id=1,
                score=5,
                description="Best meal",
                date_added=date(2024, 4, 16),
            ),
            Rating(
                recipe_id=2,
                score=3,
                description="Bad for me",
                date_added=date(2024, 4, 17),
            ),
            Rating(
                recipe_id=3,
                score=5,
                description="Great recipe!",
                date_added=date(2024, 4, 17),
            ),
        ]

        for rating in ratings:
            db.session.add(rating)

        # Create grocery lists
        grocery_lists = [
            GroceryList(name="Busy Week", description="For when time is running low"),
            GroceryList(name="Pizza Night", description="For pizza making"),
        ]

        for grocery_list in grocery_lists:
            db.session.add(grocery_list)

        db.session.commit()

        print("Database seeded successfully!")


if __name__ == "__main__":
    seed_database()
