"""Grocery Lists API routes."""
from flask import Blueprint, request, jsonify
from src.api.grocery_lists.services import GroceryListService
from src.middleware.handler import error_handler, validate_request, paginate, get_db_session
from src.middleware.errors import NotFoundError

grocery_lists_bp = Blueprint('grocery_lists', __name__)


@grocery_lists_bp.route('', methods=['GET'])
@error_handler
@paginate()
def get_grocery_lists(page, per_page):
    """
    Get paginated list of grocery lists.
    ---
    tags:
      - Grocery Lists
    parameters:
      - $ref: '#/components/parameters/PageParam'
      - $ref: '#/components/parameters/PerPageParam'
      - $ref: '#/components/parameters/SearchParam'
    responses:
      200:
        description: List of grocery lists
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/PaginatedResponse'
    """
    session = get_db_session()
    service = GroceryListService(session)

    search = request.args.get('search')

    result = service.get_paginated(
        page=page,
        per_page=per_page,
        search=search
    )

    return jsonify(result), 200


@grocery_lists_bp.route('/<int:list_id>', methods=['GET'])
@error_handler
def get_grocery_list(list_id):
    """
    Get grocery list by ID.
    ---
    tags:
      - Grocery Lists
    parameters:
      - name: list_id
        in: path
        required: true
        schema:
          type: integer
    responses:
      200:
        description: Grocery list details
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/GroceryListDetail'
      404:
        description: Grocery list not found
    """
    session = get_db_session()
    service = GroceryListService(session)

    grocery_list = service.get_by_id(list_id)
    if not grocery_list:
        raise NotFoundError(f"Grocery list with id {list_id} not found")

    return jsonify(grocery_list), 200


@grocery_lists_bp.route('', methods=['POST'])
@error_handler
@validate_request('name')
def create_grocery_list():
    """
    Create a new grocery list.
    ---
    tags:
      - Grocery Lists
    requestBody:
      required: true
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/GroceryListInput'
    responses:
      201:
        description: Grocery list created
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/GroceryListDetail'
      400:
        description: Validation error
    """
    session = get_db_session()
    service = GroceryListService(session)

    data = request.get_json()
    grocery_list = service.create(data)

    return jsonify(grocery_list), 201


@grocery_lists_bp.route('/<int:list_id>', methods=['PUT'])
@error_handler
def update_grocery_list(list_id):
    """
    Update a grocery list.
    ---
    tags:
      - Grocery Lists
    parameters:
      - name: list_id
        in: path
        required: true
        schema:
          type: integer
    requestBody:
      required: true
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/GroceryListInput'
    responses:
      200:
        description: Grocery list updated
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/GroceryListDetail'
      404:
        description: Grocery list not found
    """
    session = get_db_session()
    service = GroceryListService(session)

    data = request.get_json()
    grocery_list = service.update(list_id, data)

    if not grocery_list:
        raise NotFoundError(f"Grocery list with id {list_id} not found")

    return jsonify(grocery_list), 200


@grocery_lists_bp.route('/<int:list_id>', methods=['DELETE'])
@error_handler
def delete_grocery_list(list_id):
    """
    Delete a grocery list (soft delete).
    ---
    tags:
      - Grocery Lists
    parameters:
      - name: list_id
        in: path
        required: true
        schema:
          type: integer
    responses:
      204:
        description: Grocery list deleted
      404:
        description: Grocery list not found
    """
    session = get_db_session()
    service = GroceryListService(session)

    if not service.delete(list_id):
        raise NotFoundError(f"Grocery list with id {list_id} not found")

    return '', 204


@grocery_lists_bp.route('/<int:list_id>/ingredients/<int:ingredient_id>', methods=['POST'])
@error_handler
def add_ingredient_to_list(list_id, ingredient_id):
    """
    Add an ingredient to a grocery list.
    ---
    tags:
      - Grocery Lists
    parameters:
      - name: list_id
        in: path
        required: true
        schema:
          type: integer
      - name: ingredient_id
        in: path
        required: true
        schema:
          type: integer
    responses:
      200:
        description: Ingredient added to list
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/GroceryListDetail'
      404:
        description: Grocery list or ingredient not found
    """
    session = get_db_session()
    service = GroceryListService(session)

    grocery_list = service.add_ingredient(list_id, ingredient_id)

    if not grocery_list:
        raise NotFoundError(f"Grocery list {list_id} or ingredient {ingredient_id} not found")

    return jsonify(grocery_list), 200


@grocery_lists_bp.route('/<int:list_id>/ingredients/<int:ingredient_id>', methods=['DELETE'])
@error_handler
def remove_ingredient_from_list(list_id, ingredient_id):
    """
    Remove an ingredient from a grocery list.
    ---
    tags:
      - Grocery Lists
    parameters:
      - name: list_id
        in: path
        required: true
        schema:
          type: integer
      - name: ingredient_id
        in: path
        required: true
        schema:
          type: integer
    responses:
      204:
        description: Ingredient removed from list
      404:
        description: Grocery list or ingredient not found
    """
    session = get_db_session()
    service = GroceryListService(session)

    if not service.remove_ingredient(list_id, ingredient_id):
        raise NotFoundError(f"Grocery list {list_id} or ingredient {ingredient_id} not found")

    return '', 204


@grocery_lists_bp.route('/<int:list_id>/add-from-recipe/<int:recipe_id>', methods=['POST'])
@error_handler
def add_recipe_ingredients_to_list(list_id, recipe_id):
    """
    Add all ingredients from a recipe to a grocery list.
    ---
    tags:
      - Grocery Lists
    parameters:
      - name: list_id
        in: path
        required: true
        schema:
          type: integer
      - name: recipe_id
        in: path
        required: true
        schema:
          type: integer
    responses:
      200:
        description: Recipe ingredients added to list
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/GroceryListDetail'
      404:
        description: Grocery list or recipe not found
    """
    session = get_db_session()
    service = GroceryListService(session)

    grocery_list = service.add_recipe_ingredients(list_id, recipe_id)

    if not grocery_list:
        raise NotFoundError(f"Grocery list {list_id} or recipe {recipe_id} not found")

    return jsonify(grocery_list), 200