"""Database models for the Recipe Management system."""
from sqlalchemy import Column, String, Integer, Text, Date, ForeignKey, Table, Float
from sqlalchemy.orm import relationship
from src.models.db.base_model import BaseModel, Base

# Association tables
recipe_recipe_list = Table(
    'recipe_recipe_list',
    Base.metadata,
    Column('recipe_id', Integer, ForeignKey('recipes.id', ondelete='CASCADE')),
    Column('recipe_list_id', Integer, ForeignKey('recipe_lists.id', ondelete='CASCADE'))
)

grocery_list_ingredient = Table(
    'grocery_list_ingredient',
    Base.metadata,
    Column('grocery_list_id', Integer, ForeignKey('grocery_lists.id', ondelete='CASCADE')),
    Column('ingredient_id', Integer, ForeignKey('ingredients.id', ondelete='CASCADE'))
)


class Recipe(BaseModel):
    """Recipe model."""

    __tablename__ = 'recipes'

    title = Column(String(50), nullable=False, unique=True)
    description = Column(Text)
    date_published = Column(Date)

    # Relationships
    instructions = relationship('Instruction', back_populates='recipe', uselist=False, cascade='all, delete-orphan')
    steps = relationship('Step', back_populates='recipe', order_by='Step.step_number', cascade='all, delete-orphan')
    recipe_ingredients = relationship('RecipeIngredient', back_populates='recipe', cascade='all, delete-orphan')
    ratings = relationship('Rating', back_populates='recipe', cascade='all, delete-orphan')
    favorites = relationship('Favorite', back_populates='recipe', cascade='all, delete-orphan')
    recipe_lists = relationship('RecipeList', secondary=recipe_recipe_list, back_populates='recipes')

    def get_average_rating(self):
        """Calculate average rating."""
        if not self.ratings:
            return None
        return sum(r.score for r in self.ratings) / len(self.ratings)


class Ingredient(BaseModel):
    """Ingredient model."""

    __tablename__ = 'ingredients'

    name = Column(String(50), nullable=False, unique=True)
    last_added = Column(Date)

    # Relationships
    recipe_ingredients = relationship('RecipeIngredient', back_populates='ingredient', cascade='all, delete-orphan')
    grocery_lists = relationship('GroceryList', secondary=grocery_list_ingredient, back_populates='ingredients')


class RecipeIngredient(Base):
    """Recipe-Ingredient association with quantity."""

    __tablename__ = 'recipe_ingredients'

    id = Column(Integer, primary_key=True, autoincrement=True)
    recipe_id = Column(Integer, ForeignKey('recipes.id', ondelete='CASCADE'), nullable=False)
    ingredient_id = Column(Integer, ForeignKey('ingredients.id', ondelete='CASCADE'), nullable=False)
    quantity = Column(String(50))

    # Relationships
    recipe = relationship('Recipe', back_populates='recipe_ingredients')
    ingredient = relationship('Ingredient', back_populates='recipe_ingredients')

    def to_dict(self):
        """Convert to dictionary."""
        return {
            'id': self.id,
            'recipe_id': self.recipe_id,
            'ingredient_id': self.ingredient_id,
            'ingredient': self.ingredient.to_dict() if self.ingredient else None,
            'quantity': self.quantity
        }


class Instruction(Base):
    """Recipe instruction model."""

    __tablename__ = 'instructions'

    id = Column(Integer, primary_key=True, autoincrement=True)
    recipe_id = Column(Integer, ForeignKey('recipes.id', ondelete='CASCADE'), nullable=False, unique=True)
    cook_time = Column(String(50))
    prep_time = Column(String(50))
    servings = Column(Integer)
    calories = Column(Integer)

    # Relationships
    recipe = relationship('Recipe', back_populates='instructions')

    def to_dict(self):
        """Convert to dictionary."""
        return {
            'id': self.id,
            'recipe_id': self.recipe_id,
            'cook_time': self.cook_time,
            'prep_time': self.prep_time,
            'servings': self.servings,
            'calories': self.calories
        }


class Step(Base):
    """Recipe step model."""

    __tablename__ = 'steps'

    id = Column(Integer, primary_key=True, autoincrement=True)
    recipe_id = Column(Integer, ForeignKey('recipes.id', ondelete='CASCADE'), nullable=False)
    step_number = Column(Integer, nullable=False)
    description = Column(Text, nullable=False)

    # Relationships
    recipe = relationship('Recipe', back_populates='steps')

    def to_dict(self):
        """Convert to dictionary."""
        return {
            'id': self.id,
            'recipe_id': self.recipe_id,
            'step_number': self.step_number,
            'description': self.description
        }


class Rating(Base):
    """Recipe rating model."""

    __tablename__ = 'ratings'

    id = Column(Integer, primary_key=True, autoincrement=True)
    recipe_id = Column(Integer, ForeignKey('recipes.id', ondelete='CASCADE'), nullable=False)
    score = Column(Integer, nullable=False)
    description = Column(Text)
    date_added = Column(Date)

    # Relationships
    recipe = relationship('Recipe', back_populates='ratings')

    def to_dict(self):
        """Convert to dictionary."""
        return {
            'id': self.id,
            'recipe_id': self.recipe_id,
            'score': self.score,
            'description': self.description,
            'date_added': self.date_added.isoformat() if self.date_added else None
        }


class Favorite(Base):
    """Favorite recipe model."""

    __tablename__ = 'favorites'

    id = Column(Integer, primary_key=True, autoincrement=True)
    recipe_id = Column(Integer, ForeignKey('recipes.id', ondelete='CASCADE'), nullable=False)
    date_added = Column(Date)
    description = Column(Text)

    # Relationships
    recipe = relationship('Recipe', back_populates='favorites')

    def to_dict(self):
        """Convert to dictionary."""
        return {
            'id': self.id,
            'recipe_id': self.recipe_id,
            'date_added': self.date_added.isoformat() if self.date_added else None,
            'description': self.description
        }


class RecipeList(BaseModel):
    """Recipe list model."""

    __tablename__ = 'recipe_lists'

    name = Column(String(50), nullable=False, unique=True)
    description = Column(Text)

    # Relationships
    recipes = relationship('Recipe', secondary=recipe_recipe_list, back_populates='recipe_lists')


class GroceryList(BaseModel):
    """Grocery list model."""

    __tablename__ = 'grocery_lists'

    name = Column(String(50), nullable=False, unique=True)
    description = Column(Text)

    # Relationships
    ingredients = relationship('Ingredient', secondary=grocery_list_ingredient, back_populates='grocery_lists')