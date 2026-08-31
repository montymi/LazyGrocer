"""Recipe API routes."""
from flask import Blueprint, request, jsonify
from src.api.recipes.services import RecipeService
from src.middleware.handler import error_handler, validate_request, paginate, get_db_session
from src.middleware.errors import NotFoundError, ValidationError

recipes_bp = Blueprint('recipes', __name__)


@recipes_bp.route('', methods=['GET'])
@error_handler
@paginate()
def get_recipes(page, per_page):
    """
    Get paginated list of recipes.
    ---
    tags:
      - Recipes
    parameters:
      - $ref: '#/components/parameters/PageParam'
      - $ref: '#/components/parameters/PerPageParam'
      - $ref: '#/components/parameters/SearchParam'
      - $ref: '#/components/parameters/SortParam'
      - $ref: '#/components/parameters/OrderParam'
    responses:
      200:
        description: List of recipes
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/PaginatedResponse'
    """
    session = get_db_session()
    service = RecipeService(session)

    search = request.args.get('search')
    sort = request.args.get('sort', 'created_at')
    order = request.args.get('order', 'desc')

    result = service.get_paginated(
        page=page,
        per_page=per_page,
        search=search,
        sort=sort,
        order=order
    )

    return jsonify(result), 200


@recipes_bp.route('/<int:recipe_id>', methods=['GET'])
@error_handler
def get_recipe(recipe_id):
    """
    Get recipe by ID.
    ---
    tags:
      - Recipes
    parameters:
      - name: recipe_id
        in: path
        required: true
        schema:
          type: integer
    responses:
      200:
        description: Recipe details
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/RecipeDetail'
      404:
        description: Recipe not found
    """
    session = get_db_session()
    service = RecipeService(session)

    recipe = service.get_by_id(recipe_id)
    if not recipe:
        raise NotFoundError(f"Recipe with id {recipe_id} not found")

    return jsonify(recipe), 200


@recipes_bp.route('', methods=['POST'])
@error_handler
@validate_request('title')
def create_recipe():
    """
    Create a new recipe.
    ---
    tags:
      - Recipes
    requestBody:
      required: true
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/RecipeInput'
    responses:
      201:
        description: Recipe created
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/RecipeDetail'
      400:
        description: Validation error
    """
    session = get_db_session()
    service = RecipeService(session)

    data = request.get_json()
    recipe = service.create(data)

    return jsonify(recipe), 201


@recipes_bp.route('/<int:recipe_id>', methods=['PUT'])
@error_handler
def update_recipe(recipe_id):
    """
    Update a recipe.
    ---
    tags:
      - Recipes
    parameters:
      - name: recipe_id
        in: path
        required: true
        schema:
          type: integer
    requestBody:
      required: true
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/RecipeInput'
    responses:
      200:
        description: Recipe updated
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/RecipeDetail'
      404:
        description: Recipe not found
    """
    session = get_db_session()
    service = RecipeService(session)

    data = request.get_json()
    recipe = service.update(recipe_id, data)

    if not recipe:
        raise NotFoundError(f"Recipe with id {recipe_id} not found")

    return jsonify(recipe), 200


@recipes_bp.route('/<int:recipe_id>', methods=['DELETE'])
@error_handler
def delete_recipe(recipe_id):
    """
    Delete a recipe (soft delete).
    ---
    tags:
      - Recipes
    parameters:
      - name: recipe_id
        in: path
        required: true
        schema:
          type: integer
    responses:
      204:
        description: Recipe deleted
      404:
        description: Recipe not found
    """
    session = get_db_session()
    service = RecipeService(session)

    if not service.delete(recipe_id):
        raise NotFoundError(f"Recipe with id {recipe_id} not found")

    return '', 204


@recipes_bp.route('/<int:recipe_id>/ratings', methods=['POST'])
@error_handler
@validate_request('score')
def add_rating(recipe_id):
    """
    Add a rating to a recipe.
    ---
    tags:
      - Recipes
    parameters:
      - name: recipe_id
        in: path
        required: true
        schema:
          type: integer
    requestBody:
      required: true
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/RatingInput'
    responses:
      201:
        description: Rating added
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/RatingResponse'
      404:
        description: Recipe not found
    """
    session = get_db_session()
    service = RecipeService(session)

    data = request.get_json()

    # Validate score
    if not 1 <= data['score'] <= 5:
        raise ValidationError("Score must be between 1 and 5")

    rating = service.add_rating(recipe_id, data)

    if not rating:
        raise NotFoundError(f"Recipe with id {recipe_id} not found")

    return jsonify(rating), 201


@recipes_bp.route('/<int:recipe_id>/favorite', methods=['POST'])
@error_handler
def add_favorite(recipe_id):
    """
    Mark recipe as favorite.
    ---
    tags:
      - Recipes
    parameters:
      - name: recipe_id
        in: path
        required: true
        schema:
          type: integer
    requestBody:
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/FavoriteInput'
    responses:
      201:
        description: Recipe marked as favorite
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/FavoriteResponse'
      404:
        description: Recipe not found
    """
    session = get_db_session()
    service = RecipeService(session)

    data = request.get_json() or {}
    favorite = service.add_favorite(recipe_id, data)

    if not favorite:
        raise NotFoundError(f"Recipe with id {recipe_id} not found")

    return jsonify(favorite), 201


@recipes_bp.route('/<int:recipe_id>/favorite', methods=['DELETE'])
@error_handler
def remove_favorite(recipe_id):
    """
    Remove recipe from favorites.
    ---
    tags:
      - Recipes
    parameters:
      - name: recipe_id
        in: path
        required: true
        schema:
          type: integer
    responses:
      204:
        description: Recipe removed from favorites
      404:
        description: Recipe not found
    """
    session = get_db_session()
    service = RecipeService(session)

    if not service.remove_favorite(recipe_id):
        raise NotFoundError(f"Recipe with id {recipe_id} not found")

    return '', 204