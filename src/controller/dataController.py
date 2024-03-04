import importlib.resources as resources
import logging
import sqlite3

logging.basicConfig(level=logging.DEBUG)

from model.enums.scripts import InsertScripts, SelectScripts

class DataController:
    def __init__(self, db=r"../artifacts/recipe.db"):
        self.db = db
        self.connection = None 
        self.cursor = None
        self._init_database_()

    def _init_database_(self):
        self.connect() 
        self.read()
        self.disconnect()

    def connect(self):
        try:
            self.connection = sqlite3.connect(self.db)
            self.cursor = self.connection.cursor()
        except sqlite3.Error as e:
            logging.error("Failed to connect to the database: %s", e)

    def disconnect(self):
        if not self.connection: logging.info("No active connection")
        else:
            try:
                self.connection.close() 
                logging.info("Disconnected from database")
            except sqlite3.Error as e:
                logging.error("Failed to disconnect from the database: %s", e)

    def execute(self, query: InsertScripts, params=[]):
        if not self.connection: 
            logging.info("No active connection")
        elif query.params != len(params):
            logging.debug("Incorrect number of parameters given")
        else:
            try:
                if not params: self.cursor.execute(query) 
                else: self.cursor.execute(query.script, params)
                self.connection.commit()
                logging.debug("Query executed successfully: %s", query.script)
                return 1
            except sqlite3.Error as e:
                logging.error("Error executing query: %s", e)
        return -1

    def fetch(self, query: SelectScripts, params=None):
        if not self.connection: 
            logging.info("No active connection")
        else: 
            try:
                if params: self.cursor.execute(query.script, params)
                else: self.cursor.execute(query.script)
                return self.cursor.fetchall()
            except sqlite3.Error as e:
                logging.error("Error fetching data: %s", e)
        return []
        
    def read(self, script="init"):
        if not self.connection: logging.info("No active connection")
        else:
            if not script.endswith('.sql'): script += '.sql'
            try:
                with resources.open_text('scripts', script) as f:
                    self.cursor.executescript(f.read())
                logging.debug("SQL script '%s' executed successfully", script)
            except sqlite3.Error as e:
                logging.error("Error executing SQL script '%s': %s", script, e)