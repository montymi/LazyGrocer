from os import environ

PASS = environ.get("PASS", "default_password")
USER = environ.get("USER", "default_user")
DB = environ.get("DB", "default_db")
HOST = environ.get("HOST", "localhost")
