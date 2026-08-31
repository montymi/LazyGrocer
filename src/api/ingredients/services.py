"""Ingredients service layer."""
from datetime import date
from typing import Dict, List, Optional
from sqlalchemy.orm import Session
from sqlalchemy import or_
from src.models.db.models import Ingredient, Recipe, RecipeIngredient
from src.middleware.errors import ConflictError


class IngredientService:
    """Service class for ingredient operations."""

    def __init__(self, session: Session):
        """Initialize service with database session."""
        self.session = session

    def get_paginated(self, page: int, per_page: int, search: str = None) -> Dict:
        """Get paginated ingredients."""
        query = Ingredient.query_active(self.session)

        # Apply search filter
        if search:
            query = query.filter(
                Ingredient.name.ilike(f'%{search}%')
            )

        # Get total count
        total = query.count()

        # Apply pagination
        offset = (page - 1) * per_page
        ingredients = query.offset(offset).limit(per_page).all()

        # Calculate pages
        pages = (total + per_page - 1) // per_page

        return {
            'items': [ing.to_dict() for ing in ingredients],
            'total': total,
            'page': page,
            'per_page': per_page,
            'pages': pages
        }

    def get_by_id(self, ingredient_id: int) -> Optional[Dict]:
        """Get ingredient by ID."""
        ingredient = Ingredient.query_active(self.session).filter_by(id=ingredient_id).first()

        if not ingredient:
            return None

        return ingredient.to_dict()

    def get_by_name(self, name: str) -> Optional[Ingredient]:
        """Get ingredient by name."""
        return Ingredient.query_active(self.session).filter_by(name=name).first()

    def create(self, data: Dict) -> Dict:
        """Create a new ingredient."""
        # Check if ingredient with same name exists
        existing = self.get_by_name(data['name'])
        if existing:
            raise ConflictError(f"Ingredient with name '{data['name']}' already exists")

        ingredient = Ingredient(
            name=data['name'],
            last_added=date.today()
        )
        self.session.add(ingredient)
        self.session.commit()

        return ingredient.to_dict()

    def update(self, ingredient_id: int, data: Dict) -> Optional[Dict]:
        """Update an ingredient."""
        ingredient = Ingredient.query_active(self.session).filter_by(id=ingredient_id).first()

        if not ingredient:
            return None

        # Check if new name conflicts with existing ingredient
        if 'name' in data and data['name'] != ingredient.name:
            existing = self.get_by_name(data['name'])
            if existing:
                raise ConflictError(f"Ingredient with name '{data['name']}' already exists")

        ingredient.update(
            name=data.get('name', ingredient.name)
        )
        ingredient.last_added = date.today()
        self.session.commit()

        return ingredient.to_dict()

    def delete(self, ingredient_id: int) -> bool:
        """Soft delete an ingredient."""
        ingredient = Ingredient.query_active(self.session).filter_by(id=ingredient_id).first()

        if not ingredient:
            return False

        ingredient.soft_delete()
        self.session.commit()
        return True

    def get_recipes_with_ingredient(self, ingredient_id: int) -> Optional[List[Dict]]:
        """Get all recipes that use this ingredient."""
        ingredient = Ingredient.query_active(self.session).filter_by(id=ingredient_id).first()

        if not ingredient:
            return None

        # Get recipes through the relationship
        recipes = (
            self.session.query(Recipe)
            .join(RecipeIngredient)
            .filter(
                RecipeIngredient.ingredient_id == ingredient_id,
                Recipe.is_deleted == False
            )
            .all()
        )

        return [
            recipe.to_dict(exclude=['recipe_ingredients', 'steps', 'ratings', 'favorites'])
            for recipe in recipes
        ]