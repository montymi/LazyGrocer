"""API models generated from Swagger/OpenAPI specification."""
from dataclasses import dataclass, field
from typing import Optional, List
from datetime import date, datetime


@dataclass
class RecipeInput:
    """Input model for creating/updating recipes."""
    title: str
    description: Optional[str] = None
    date_published: Optional[date] = None
    instructions: Optional['InstructionInput'] = None
    steps: List['StepInput'] = field(default_factory=list)
    ingredients: List['RecipeIngredientInput'] = field(default_factory=list)


@dataclass
class RecipeResponse:
    """Response model for recipe."""
    id: int
    title: str
    description: Optional[str] = None
    date_published: Optional[date] = None
    is_deleted: bool = False
    is_shared: bool = False
    created_at: datetime = None
    updated_at: datetime = None


@dataclass
class RecipeDetailResponse(RecipeResponse):
    """Detailed response model for recipe."""
    instructions: Optional['InstructionResponse'] = None
    steps: List['StepResponse'] = field(default_factory=list)
    ingredients: List['RecipeIngredientResponse'] = field(default_factory=list)
    ratings: List['RatingResponse'] = field(default_factory=list)
    average_rating: Optional[float] = None


@dataclass
class InstructionInput:
    """Input model for recipe instructions."""
    cook_time: Optional[str] = None
    prep_time: Optional[str] = None
    servings: Optional[int] = None
    calories: Optional[int] = None


@dataclass
class InstructionResponse:
    """Response model for recipe instructions."""
    id: int
    recipe_id: int
    cook_time: Optional[str] = None
    prep_time: Optional[str] = None
    servings: Optional[int] = None
    calories: Optional[int] = None


@dataclass
class StepInput:
    """Input model for recipe steps."""
    step_number: int
    description: str


@dataclass
class StepResponse:
    """Response model for recipe steps."""
    id: int
    recipe_id: int
    step_number: int
    description: str


@dataclass
class IngredientInput:
    """Input model for ingredients."""
    name: str


@dataclass
class IngredientResponse:
    """Response model for ingredients."""
    id: int
    name: str
    last_added: Optional[date] = None
    is_deleted: bool = False
    created_at: datetime = None
    updated_at: datetime = None


@dataclass
class RecipeIngredientInput:
    """Input model for recipe ingredients."""
    ingredient_name: str
    quantity: Optional[str] = None


@dataclass
class RecipeIngredientResponse:
    """Response model for recipe ingredients."""
    id: int
    recipe_id: int
    ingredient_id: int
    ingredient: Optional[IngredientResponse] = None
    quantity: Optional[str] = None


@dataclass
class RatingInput:
    """Input model for ratings."""
    score: int
    description: Optional[str] = None


@dataclass
class RatingResponse:
    """Response model for ratings."""
    id: int
    recipe_id: int
    score: int
    description: Optional[str] = None
    date_added: Optional[date] = None


@dataclass
class FavoriteInput:
    """Input model for favorites."""
    description: Optional[str] = None


@dataclass
class FavoriteResponse:
    """Response model for favorites."""
    id: int
    recipe_id: int
    date_added: Optional[date] = None
    description: Optional[str] = None


@dataclass
class RecipeListInput:
    """Input model for recipe lists."""
    name: str
    description: Optional[str] = None


@dataclass
class RecipeListResponse:
    """Response model for recipe lists."""
    id: int
    name: str
    description: Optional[str] = None
    is_deleted: bool = False
    is_shared: bool = False
    created_at: datetime = None
    updated_at: datetime = None


@dataclass
class RecipeListDetailResponse(RecipeListResponse):
    """Detailed response model for recipe lists."""
    recipes: List[RecipeResponse] = field(default_factory=list)


@dataclass
class GroceryListInput:
    """Input model for grocery lists."""
    name: str
    description: Optional[str] = None


@dataclass
class GroceryListResponse:
    """Response model for grocery lists."""
    id: int
    name: str
    description: Optional[str] = None
    is_deleted: bool = False
    is_shared: bool = False
    created_at: datetime = None
    updated_at: datetime = None


@dataclass
class GroceryListDetailResponse(GroceryListResponse):
    """Detailed response model for grocery lists."""
    ingredients: List[IngredientResponse] = field(default_factory=list)


@dataclass
class PaginatedResponse:
    """Generic paginated response."""
    items: List[any]
    total: int
    page: int
    per_page: int
    pages: int


@dataclass
class ErrorResponse:
    """Error response model."""
    error: dict