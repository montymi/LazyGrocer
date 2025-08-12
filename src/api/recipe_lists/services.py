"""Recipe Lists service layer."""
from typing import Dict, Optional
from sqlalchemy.orm import Session
from sqlalchemy import or_
from src.models.db.models import RecipeList, Recipe
from src.middleware.errors import NotFoundError, ConflictError


class RecipeListService:
    """Service class for recipe list operations."""

    def __init__(self, session: Session):
        """Initialize service with database session."""
        self.session = session

    def get_paginated(self, page: int, per_page: int, search: str = None) -> Dict:
        """Get paginated recipe lists."""
        query = RecipeList.query_active(self.session)

        # Apply search filter
        if search:
            query = query.filter(
                or_(
                    RecipeList.name.ilike(f'%{search}%'),
                    RecipeList.description.ilike(f'%{search}%')
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
        """Get recipe list by ID with recipes."""
        recipe_list = RecipeList.query_active(self.session).filter_by(id=list_id).first()

        if not recipe_list:
            return None

        return self._serialize_list_detail(recipe_list)

    def create(self, data: Dict) -> Dict:
        """Create a new recipe list."""
        recipe_list = RecipeList(
            name=data['name'],
            description=data.get('description')
        )
        self.session.add(recipe_list)
        self.session.commit()

        return self._serialize_list_detail(recipe_list)

    def update(self, list_id: int, data: Dict) -> Optional[Dict]:
        """Update a recipe list."""
        recipe_list = RecipeList.query_active(self.session).filter_by(id=list_id).first()

        if not recipe_list:
            return None

        recipe_list.update(
            name=data.get('name', recipe_list.name),
            description=data.get('description', recipe_list.description)
        )
        self.session.commit()

        return self._serialize_list_detail(recipe_list)

    def delete(self, list_id: int) -> bool:
        """Soft delete a recipe list."""
        recipe_list = RecipeList.query_active(self.session).filter_by(id=list_id).first()

        if not recipe_list:
            return False

        recipe_list.soft_delete()
        self.session.commit()
        return True

    def add_recipe(self, list_id: int, recipe_id: int) -> Optional[Dict]:
        """Add a recipe to a recipe list."""
        recipe_list = RecipeList.query_active(self.session).filter_by(id=list_id).first()
        recipe = Recipe.query_active(self.session).filter_by(id=recipe_id).first()

        if not recipe_list or not recipe:
            return None

        # Check if recipe already in list
        if recipe in recipe_list.recipes:
            raise ConflictError(f"Recipe {recipe_id} already in list {list_id}")

        recipe_list.recipes.append(recipe)
        self.session.commit()

        return self._serialize_list_detail(recipe_list)

    def remove_recipe(self, list_id: int, recipe_id: int) -> bool:
        """Remove a recipe from a recipe list."""
        recipe_list = RecipeList.query_active(self.session).filter_by(id=list_id).first()
        recipe = Recipe.query_active(self.session).filter_by(id=recipe_id).first()

        if not recipe_list or not recipe:
            return False

        if recipe in recipe_list.recipes:
            recipe_list.recipes.remove(recipe)
            self.session.commit()
            return True

        return False

    def _serialize_list(self, recipe_list: RecipeList) -> Dict:
        """Serialize recipe list for list view."""
        return recipe_list.to_dict(exclude=['recipes'])

    def _serialize_list_detail(self, recipe_list: RecipeList) -> Dict:
        """Serialize recipe list with recipes."""
        result = recipe_list.to_dict(exclude=['recipes'])
        result['recipes'] = [
            recipe.to_dict(exclude=['recipe_ingredients', 'steps', 'ratings', 'favorites'])
            for recipe in recipe_list.recipes
            if not recipe.is_deleted
        ]
        return result