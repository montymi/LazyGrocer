"""Recipe service layer."""
from datetime import date
from typing import Dict, List, Optional
from sqlalchemy.orm import Session
from sqlalchemy import or_, desc, asc
from src.models.db.models import Recipe, Ingredient, RecipeIngredient, Instruction, Step, Rating, Favorite
from src.middleware.errors import NotFoundError, ValidationError


class RecipeService:
    """Service class for recipe operations."""

    def __init__(self, session: Session):
        """Initialize service with database session."""
        self.session = session

    def get_paginated(self, page: int, per_page: int, search: str = None,
                      sort: str = 'created_at', order: str = 'desc') -> Dict:
        """Get paginated recipes."""
        query = Recipe.query_active(self.session)

        # Apply search filter
        if search:
            query = query.filter(
                or_(
                    Recipe.title.ilike(f'%{search}%'),
                    Recipe.description.ilike(f'%{search}%')
                )
            )

        # Apply sorting
        sort_column = getattr(Recipe, sort, Recipe.created_at)
        if order == 'desc':
            query = query.order_by(desc(sort_column))
        else:
            query = query.order_by(asc(sort_column))

        # Get total count
        total = query.count()

        # Apply pagination
        offset = (page - 1) * per_page
        recipes = query.offset(offset).limit(per_page).all()

        # Calculate pages
        pages = (total + per_page - 1) // per_page

        return {
            'items': [self._serialize_recipe(r) for r in recipes],
            'total': total,
            'page': page,
            'per_page': per_page,
            'pages': pages
        }

    def get_by_id(self, recipe_id: int) -> Optional[Dict]:
        """Get recipe by ID with full details."""
        recipe = Recipe.query_active(self.session).filter_by(id=recipe_id).first()

        if not recipe:
            return None

        return self._serialize_recipe_detail(recipe)

    def create(self, data: Dict) -> Dict:
        """Create a new recipe."""
        # Create recipe
        recipe = Recipe(
            title=data['title'],
            description=data.get('description'),
            date_published=data.get('date_published')
        )
        self.session.add(recipe)
        self.session.flush()  # Get recipe ID

        # Add instructions if provided
        if data.get('instructions'):
            inst_data = data['instructions']
            instruction = Instruction(
                recipe_id=recipe.id,
                cook_time=inst_data.get('cook_time'),
                prep_time=inst_data.get('prep_time'),
                servings=inst_data.get('servings'),
                calories=inst_data.get('calories')
            )
            self.session.add(instruction)

        # Add steps if provided
        for step_data in data.get('steps', []):
            step = Step(
                recipe_id=recipe.id,
                step_number=step_data['step_number'],
                description=step_data['description']
            )
            self.session.add(step)

        # Add ingredients if provided
        for ing_data in data.get('ingredients', []):
            # Find or create ingredient
            ingredient = self.session.query(Ingredient).filter_by(
                name=ing_data['ingredient_name']
            ).first()

            if not ingredient:
                ingredient = Ingredient(
                    name=ing_data['ingredient_name'],
                    last_added=date.today()
                )
                self.session.add(ingredient)
                self.session.flush()

            # Create recipe-ingredient relationship
            recipe_ingredient = RecipeIngredient(
                recipe_id=recipe.id,
                ingredient_id=ingredient.id,
                quantity=ing_data.get('quantity')
            )
            self.session.add(recipe_ingredient)

        self.session.commit()
        return self._serialize_recipe_detail(recipe)

    def update(self, recipe_id: int, data: Dict) -> Optional[Dict]:
        """Update a recipe."""
        recipe = Recipe.query_active(self.session).filter_by(id=recipe_id).first()

        if not recipe:
            return None

        # Update basic fields
        recipe.update(
            title=data.get('title', recipe.title),
            description=data.get('description', recipe.description),
            date_published=data.get('date_published', recipe.date_published)
        )

        # Update instructions
        if 'instructions' in data:
            inst_data = data['instructions']
            if recipe.instructions:
                recipe.instructions.cook_time = inst_data.get('cook_time')
                recipe.instructions.prep_time = inst_data.get('prep_time')
                recipe.instructions.servings = inst_data.get('servings')
                recipe.instructions.calories = inst_data.get('calories')
            else:
                instruction = Instruction(
                    recipe_id=recipe.id,
                    cook_time=inst_data.get('cook_time'),
                    prep_time=inst_data.get('prep_time'),
                    servings=inst_data.get('servings'),
                    calories=inst_data.get('calories')
                )
                self.session.add(instruction)

        # Update steps (replace all)
        if 'steps' in data:
            # Delete existing steps
            for step in recipe.steps:
                self.session.delete(step)

            # Add new steps
            for step_data in data['steps']:
                step = Step(
                    recipe_id=recipe.id,
                    step_number=step_data['step_number'],
                    description=step_data['description']
                )
                self.session.add(step)

        # Update ingredients (replace all)
        if 'ingredients' in data:
            # Delete existing recipe ingredients
            for ri in recipe.recipe_ingredients:
                self.session.delete(ri)

            # Add new ingredients
            for ing_data in data['ingredients']:
                ingredient = self.session.query(Ingredient).filter_by(
                    name=ing_data['ingredient_name']
                ).first()

                if not ingredient:
                    ingredient = Ingredient(
                        name=ing_data['ingredient_name'],
                        last_added=date.today()
                    )
                    self.session.add(ingredient)
                    self.session.flush()

                recipe_ingredient = RecipeIngredient(
                    recipe_id=recipe.id,
                    ingredient_id=ingredient.id,
                    quantity=ing_data.get('quantity')
                )
                self.session.add(recipe_ingredient)

        self.session.commit()
        return self._serialize_recipe_detail(recipe)

    def delete(self, recipe_id: int) -> bool:
        """Soft delete a recipe."""
        recipe = Recipe.query_active(self.session).filter_by(id=recipe_id).first()

        if not recipe:
            return False

        recipe.soft_delete()
        self.session.commit()
        return True

    def add_rating(self, recipe_id: int, data: Dict) -> Optional[Dict]:
        """Add a rating to a recipe."""
        recipe = Recipe.query_active(self.session).filter_by(id=recipe_id).first()

        if not recipe:
            return None

        rating = Rating(
            recipe_id=recipe_id,
            score=data['score'],
            description=data.get('description'),
            date_added=date.today()
        )
        self.session.add(rating)
        self.session.commit()

        return rating.to_dict()

    def add_favorite(self, recipe_id: int, data: Dict) -> Optional[Dict]:
        """Mark recipe as favorite."""
        recipe = Recipe.query_active(self.session).filter_by(id=recipe_id).first()

        if not recipe:
            return None

        # Check if already favorite
        existing = self.session.query(Favorite).filter_by(recipe_id=recipe_id).first()
        if existing:
            return existing.to_dict()

        favorite = Favorite(
            recipe_id=recipe_id,
            description=data.get('description'),
            date_added=date.today()
        )
        self.session.add(favorite)
        self.session.commit()

        return favorite.to_dict()

    def remove_favorite(self, recipe_id: int) -> bool:
        """Remove recipe from favorites."""
        favorite = self.session.query(Favorite).filter_by(recipe_id=recipe_id).first()

        if not favorite:
            return False

        self.session.delete(favorite)
        self.session.commit()
        return True

    def _serialize_recipe(self, recipe: Recipe) -> Dict:
        """Serialize recipe for list view."""
        return recipe.to_dict(exclude=['recipe_ingredients', 'steps', 'ratings', 'favorites'])

    def _serialize_recipe_detail(self, recipe: Recipe) -> Dict:
        """Serialize recipe with full details."""
        result = recipe.to_dict(exclude=['recipe_ingredients'])

        # Add instructions
        if recipe.instructions:
            result['instructions'] = recipe.instructions.to_dict()

        # Add steps
        result['steps'] = [step.to_dict() for step in recipe.steps]

        # Add ingredients with details
        result['ingredients'] = [ri.to_dict() for ri in recipe.recipe_ingredients]

        # Add ratings
        result['ratings'] = [rating.to_dict() for rating in recipe.ratings]

        # Add average rating
        result['average_rating'] = recipe.get_average_rating()

        return result