"""Ingredients API routes."""
from flask import Blueprint, request, jsonify
from src.api.ingredients.services import IngredientService
from src.middleware.handler import error_handler, validate_request, paginate, get_db_session
from src.middleware.errors import NotFoundError

ingredients_bp = Blueprint('ingredients', __name__)


@ingredients_bp.route('', methods=['GET'])
@error_handler
@paginate()
def get_ingredients(page, per_page):
    """
    Get paginated list of ingredients.
    ---
    tags:
      - Ingredients
    parameters:
      - $ref: '#/components/parameters/PageParam'
      - $ref: '#/components/parameters/PerPageParam'
      - $ref: '#/components/parameters/SearchParam'
    responses:
      200:
        description: List of ingredients
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/PaginatedResponse'
    """
    session = get_db_session()
    service = IngredientService(session)

    search = request.args.get('search')

    result = service.get_paginated(
        page=page,
        per_page=per_page,
        search=search
    )

    return jsonify(result), 200


@ingredients_bp.route('/<int:ingredient_id>', methods=['GET'])
@error_handler
def get_ingredient(ingredient_id):
    """
    Get ingredient by ID.
    ---
    tags:
      - Ingredients
    parameters:
      - name: ingredient_id
        in: path
        required: true
        schema:
          type: integer
    responses:
      200:
        description: Ingredient details
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/Ingredient'
      404:
        description: Ingredient not found
    """
    session = get_db_session()
    service = IngredientService(session)

    ingredient = service.get_by_id(ingredient_id)
    if not ingredient:
        raise NotFoundError(f"Ingredient with id {ingredient_id} not found")

    return jsonify(ingredient), 200


@ingredients_bp.route('', methods=['POST'])
@error_handler
@validate_request('name')
def create_ingredient():
    """
    Create a new ingredient.
    ---
    tags:
      - Ingredients
    requestBody:
      required: true
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/IngredientInput'
    responses:
      201:
        description: Ingredient created
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/Ingredient'
      400:
        description: Validation error
    """
    session = get_db_session()
    service = IngredientService(session)

    data = request.get_json()
    ingredient = service.create(data)

    return jsonify(ingredient), 201


@ingredients_bp.route('/<int:ingredient_id>', methods=['PUT'])
@error_handler
def update_ingredient(ingredient_id):
    """
    Update an ingredient.
    ---
    tags:
      - Ingredients
    parameters:
      - name: ingredient_id
        in: path
        required: true
        schema:
          type: integer
    requestBody:
      required: true
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/IngredientInput'
    responses:
      200:
        description: Ingredient updated
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/Ingredient'
      404:
        description: Ingredient not found
    """
    session = get_db_session()
    service = IngredientService(session)

    data = request.get_json()
    ingredient = service.update(ingredient_id, data)

    if not ingredient:
        raise NotFoundError(f"Ingredient with id {ingredient_id} not found")

    return jsonify(ingredient), 200


@ingredients_bp.route('/<int:ingredient_id>', methods=['DELETE'])
@error_handler
def delete_ingredient(ingredient_id):
    """
    Delete an ingredient (soft delete).
    ---
    tags:
      - Ingredients
    parameters:
      - name: ingredient_id
        in: path
        required: true
        schema:
          type: integer
    responses:
      204:
        description: Ingredient deleted
      404:
        description: Ingredient not found
    """
    session = get_db_session()
    service = IngredientService(session)

    if not service.delete(ingredient_id):
        raise NotFoundError(f"Ingredient with id {ingredient_id} not found")

    return '', 204


@ingredients_bp.route('/<int:ingredient_id>/recipes', methods=['GET'])
@error_handler
def get_ingredient_recipes(ingredient_id):
    """
    Get all recipes using this ingredient.
    ---
    tags:
      - Ingredients
    parameters:
      - name: ingredient_id
        in: path
        required: true
        schema:
          type: integer
    responses:
      200:
        description: List of recipes using this ingredient
        content:
          application/json:
            schema:
              type: array
              items:
                $ref: '#/components/schemas/Recipe'
      404:
        description: Ingredient not found
    """
    session = get_db_session()
    service = IngredientService(session)

    recipes = service.get_recipes_with_ingredient(ingredient_id)

    if recipes is None:
        raise NotFoundError(f"Ingredient with id {ingredient_id} not found")

    return jsonify(recipes), 200