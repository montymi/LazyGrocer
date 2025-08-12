"""Recipe Lists API routes."""
from flask import Blueprint, request, jsonify
from src.api.recipe_lists.services import RecipeListService
from src.middleware.handler import error_handler, validate_request, paginate, get_db_session
from src.middleware.errors import NotFoundError

recipe_lists_bp = Blueprint('recipe_lists', __name__)


@recipe_lists_bp.route('', methods=['GET'])
@error_handler
@paginate()
def get_recipe_lists(page, per_page):
    """
    Get paginated list of recipe lists.
    ---
    tags:
      - Recipe Lists
    parameters:
      - $ref: '#/components/parameters/PageParam'
      - $ref: '#/components/parameters/PerPageParam'
      - $ref: '#/components/parameters/SearchParam'
    responses:
      200:
        description: List of recipe lists
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/PaginatedResponse'
    """
    session = get_db_session()
    service = RecipeListService(session)

    search = request.args.get('search')

    result = service.get_paginated(
        page=page,
        per_page=per_page,
        search=search
    )

    return jsonify(result), 200


@recipe_lists_bp.route('/<int:list_id>', methods=['GET'])
@error_handler
def get_recipe_list(list_id):
    """
    Get recipe list by ID.
    ---
    tags:
      - Recipe Lists
    parameters:
      - name: list_id
        in: path
        required: true
        schema:
          type: integer
    responses:
      200:
        description: Recipe list details
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/RecipeListDetail'
      404:
        description: Recipe list not found
    """
    session = get_db_session()
    service = RecipeListService(session)

    recipe_list = service.get_by_id(list_id)
    if not recipe_list:
        raise NotFoundError(f"Recipe list with id {list_id} not found")

    return jsonify(recipe_list), 200


@recipe_lists_bp.route('', methods=['POST'])
@error_handler
@validate_request('name')
def create_recipe_list():
    """
    Create a new recipe list.
    ---
    tags:
      - Recipe Lists
    requestBody:
      required: true
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/RecipeListInput'
    responses:
      201:
        description: Recipe list created
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/RecipeListDetail'
      400:
        description: Validation error
    """
    session = get_db_session()
    service = RecipeListService(session)

    data = request.get_json()
    recipe_list = service.create(data)

    return jsonify(recipe_list), 201


@recipe_lists_bp.route('/<int:list_id>', methods=['PUT'])
@error_handler
def update_recipe_list(list_id):
    """
    Update a recipe list.
    ---
    tags:
      - Recipe Lists
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
            $ref: '#/components/schemas/RecipeListInput'
    responses:
      200:
        description: Recipe list updated
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/RecipeListDetail'
      404:
        description: Recipe list not found
    """
    session = get_db_session()
    service = RecipeListService(session)

    data = request.get_json()
    recipe_list = service.update(list_id, data)

    if not recipe_list:
        raise NotFoundError(f"Recipe list with id {list_id} not found")

    return jsonify(recipe_list), 200


@recipe_lists_bp.route('/<int:list_id>', methods=['DELETE'])
@error_handler
def delete_recipe_list(list_id):
    """
    Delete a recipe list (soft delete).
    ---
    tags:
      - Recipe Lists
    parameters:
      - name: list_id
        in: path
        required: true
        schema:
          type: integer
    responses:
      204:
        description: Recipe list deleted
      404:
        description: Recipe list not found
    """
    session = get_db_session()
    service = RecipeListService(session)

    if not service.delete(list_id):
        raise NotFoundError(f"Recipe list with id {list_id} not found")

    return '', 204


@recipe_lists_bp.route('/<int:list_id>/recipes/<int:recipe_id>', methods=['POST'])
@error_handler
def add_recipe_to_list(list_id, recipe_id):
    """
    Add a recipe to a recipe list.
    ---
    tags:
      - Recipe Lists
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
        description: Recipe added to list
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/RecipeListDetail'
      404:
        description: Recipe list or recipe not found
    """
    session = get_db_session()
    service = RecipeListService(session)

    recipe_list = service.add_recipe(list_id, recipe_id)

    if not recipe_list:
        raise NotFoundError(f"Recipe list {list_id} or recipe {recipe_id} not found")

    return jsonify(recipe_list), 200


@recipe_lists_bp.route('/<int:list_id>/recipes/<int:recipe_id>', methods=['DELETE'])
@error_handler
def remove_recipe_from_list(list_id, recipe_id):
    """
    Remove a recipe from a recipe list.
    ---
    tags:
      - Recipe Lists
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
      204:
        description: Recipe removed from list
      404:
        description: Recipe list or recipe not found
    """
    session = get_db_session()
    service = RecipeListService(session)

    if not service.remove_recipe(list_id, recipe_id):
        raise NotFoundError(f"Recipe list {list_id} or recipe {recipe_id} not found")

    return '', 204