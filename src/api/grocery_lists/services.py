"""Grocery Lists service layer."""
from typing import Dict, Optional
from sqlalchemy.orm import Session
from sqlalchemy import or_
from src.models.db.models import GroceryList, Ingredient, Recipe
from src.middleware.errors import NotFoundError, ConflictError


class GroceryListService:
    """Service class for grocery list operations."""

    def __init__(self, session: Session):
        """Initialize service with database session."""
        self.session = session

    def get_paginated(self, page: int, per_page: int, search: str = None) -> Dict:
        """Get paginated grocery lists."""
        query = GroceryList.query_active(self.session)

        # Apply search filter
        if search:
            query = query.filter(
                or_(
                    GroceryList.name.ilike(f'%{search}%'),
                    GroceryList.description.ilike(f'%{search}%')
                )
            )

        # Get total count
        total = query.count()

        # Apply pagination
        offset = (page - 1) * per_page
        lists = query.offset(offset).limit(per_page).all()

        # Calculate pages
        pages = (total + per_page - 1) // per_page

        return {
            'items': [self._serialize_list(lst) for lst in lists],
            'total': total,
            'page': page,
            'per_page': per_page,
            'pages': pages
        }

    def get_by_id(self, list_id: int) -> Optional[Dict]:
        """Get grocery list by ID with ingredients."""
        grocery_list = GroceryList.query_active(self.session).filter_by(id=list_id).first()

        if not grocery_list:
            return None

        return self._serialize_list_detail(grocery_list)

    def create(self, data: Dict) -> Dict:
        """Create a new grocery list."""
        grocery_list = GroceryList(
            name=data['name'],
            description=data.get('description')
        )
        self.session.add(grocery_list)
        self.session.commit()

        return self._serialize_list_detail(grocery_list)

    def update(self, list_id: int, data: Dict) -> Optional[Dict]:
        """Update a grocery list."""
        grocery_list = GroceryList.query_active(self.session).filter_by(id=list_id).first()

        if not grocery_list:
            return None

        grocery_list.update(
            name=data.get('name', grocery_list.name),
            description=data.get('description', grocery_list.description)
        )
        self.session.commit()

        return self._serialize_list_detail(grocery_list)

    def delete(self, list_id: int) -> bool:
        """Soft delete a grocery list."""
        grocery_list = GroceryList.query_active(self.session).filter_by(id=list_id).first()

        if not grocery_list:
            return False

        grocery_list.soft_delete()
        self.session.commit()
        return True

    def add_ingredient(self, list_id: int, ingredient_id: int) -> Optional[Dict]:
        """Add an ingredient to a grocery list."""
        grocery_list = GroceryList.query_active(self.session).filter_by(id=list_id).first()
        ingredient = Ingredient.query_active(self.session).filter_by(id=ingredient_id).first()

        if not grocery_list or not ingredient:
            return None

        # Check if ingredient already in list
        if ingredient in grocery_list.ingredients:
            raise ConflictError(f"Ingredient {ingredient_id} already in list {list_id}")

        grocery_list.ingredients.append(ingredient)
        self.session.commit()

        return self._serialize_list_detail(grocery_list)

    def remove_ingredient(self, list_id: int, ingredient_id: int) -> bool:
        """Remove an ingredient from a grocery list."""
        grocery_list = GroceryList.query_active(self.session).filter_by(id=list_id).first()
        ingredient = Ingredient.query_active(self.session).filter_by(id=ingredient_id).first()

        if not grocery_list or not ingredient:
            return False

        if ingredient in grocery_list.ingredients:
            grocery_list.ingredients.remove(ingredient)
            self.session.commit()
            return True

        return False

    def add_recipe_ingredients(self, list_id: int, recipe_id: int) -> Optional[Dict]:
        """Add all ingredients from a recipe to a grocery list."""
        grocery_list = GroceryList.query_active(self.session).filter_by(id=list_id).first()
        recipe = Recipe.query_active(self.session).filter_by(id=recipe_id).first()

        if not grocery_list or not recipe:
            return None

        # Get all ingredients from the recipe
        added_count = 0
        for recipe_ingredient in recipe.recipe_ingredients:
            ingredient = recipe_ingredient.ingredient
            if ingredient and not ingredient.is_deleted:
                # Only add if not already in list
                if ingredient not in grocery_list.ingredients:
                    grocery_list.ingredients.append(ingredient)
                    added_count += 1

        if added_count > 0:
            self.session.commit()

        return self._serialize_list_detail(grocery_list)

    def _serialize_list(self, grocery_list: GroceryList) -> Dict:
        """Serialize grocery list for list view."""
        return grocery_list.to_dict(exclude=['ingredients'])

    def _serialize_list_detail(self, grocery_list: GroceryList) -> Dict:
        """Serialize grocery list with ingredients."""
        result = grocery_list.to_dict(exclude=['ingredients'])
        result['ingredients'] = [
            ingredient.to_dict()
            for ingredient in grocery_list.ingredients
            if not ingredient.is_deleted
        ]
        return result