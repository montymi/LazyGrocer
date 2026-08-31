# Database migration script (migrate.py)
"""
Database migration utilities for the Recipe Management API
"""

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from src import create_app
from src.models.base import db

app = create_app()
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command("db", MigrateCommand)

if __name__ == "__main__":
    manager.run()
