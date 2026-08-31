"""Main application entry point."""

import os
from flask import Flask
from flask_cors import CORS
from flask_swagger_ui import get_swaggerui_blueprint
from flasgger import Swagger
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

from src.middleware.handler import error_handler
from src.middleware.exceptions import register_error_handlers
from src.api.recipes.routes import recipes_bp
from src.api.recipe_lists.routes import recipe_lists_bp
from src.api.ingredients.routes import ingredients_bp
from src.api.grocery_lists.routes import grocery_lists_bp
from src.models.db.base_model import Base


def create_app(config_name="development"):
    """Application factory pattern."""
    app = Flask(__name__)

    # Configuration
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv(
        "DATABASE_URL", "postgresql://user:password@localhost:5432/recipe_db"
    )
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["JSON_SORT_KEYS"] = False

    # Enable CORS
    CORS(app)

    # Database setup
    engine = create_engine(app.config["SQLALCHEMY_DATABASE_URI"])
    Base.metadata.create_all(engine)

    # Create session factory
    session_factory = sessionmaker(bind=engine)
    Session = scoped_session(session_factory)
    app.Session = Session

    # Swagger setup
    swagger_config = {
        "headers": [],
        "specs": [
            {
                "endpoint": "apispec",
                "route": "/apispec.json",
                "rule_filter": lambda rule: True,
                "model_filter": lambda tag: True,
            }
        ],
        "static_url_path": "/flasgger_static",
        "swagger_ui": True,
        "specs_route": "/apidocs/",
    }

    swagger_template = {
        "swagger": "2.0",
        "info": {
            "title": "Recipe Management API",
            "description": "API for managing recipes, ingredients, and grocery lists",
            "version": "1.0.0",
        },
        "basePath": "/api/v1",
        "schemes": ["http", "https"],
    }

    Swagger(app, config=swagger_config, template=swagger_template)

    # Register error handlers
    register_error_handlers(app)

    # Register blueprints
    app.register_blueprint(recipes_bp, url_prefix="/api/v1/recipes")
    app.register_blueprint(recipe_lists_bp, url_prefix="/api/v1/recipe-lists")
    app.register_blueprint(ingredients_bp, url_prefix="/api/v1/ingredients")
    app.register_blueprint(grocery_lists_bp, url_prefix="/api/v1/grocery-lists")

    # Swagger UI
    SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
        "/swagger", "/apispec.json", config={"app_name": "Recipe Management API"}
    )
    app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix="/swagger")

    @app.teardown_appcontext
    def cleanup(resp_or_exc):
        """Clean up database session."""
        Session.remove()

    @app.route("/health")
    def health_check():
        """Health check endpoint."""
        return {"status": "healthy"}, 200

    return app
