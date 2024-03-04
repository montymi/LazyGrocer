from mysql.connector import connect
import getpass
import logging

from model.enums.scripts import InsertScripts, SelectScripts

class DataController2:
    def __init__(self, host='localhost', user='root', password='', database='recipes'):
        self.host = host
        self.user = user
        self.password = getpass.getpass("Enter password: ")
        self.database = database
        self.connection = None 
        self.cursor = None
        self._init_database_()

    def _init_database_(self):
        self.connect() 
        self.read()
        self.disconnect()

    def connect(self):
        try:
            self.connection = connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            if self.connection.is_connected():
                logging.debug("Connected to MySQL database")
                self.cursor = self.connection.cursor()
        except Error as e:
            logging.error("Failed to connect to the database: %s", e)

    def disconnect(self):
        if not self.connection:
            logging.debug("No active connection")
        else:
            try:
                self.connection.close() 
                logging.debug("Disconnected from MySQL database")
            except Error as e:
                logging.error("Failed to disconnect from the database: %s", e)

    def execute(self, query: InsertScripts, params=[]):
        if not self.connection: 
            logging.debug("No active connection")
        elif query.params != len(params):
            logging.debug("Incorrect number of parameters given")
        else:
            try:
                if not params:
                    self.cursor.execute(query.script) 
                else:
                    self.cursor.execute(query.script, params)
                self.connection.commit()
                logging.debug("Query executed successfully: %s", query.script)
                return 1
            except Error as e:
                logging.error("Error executing query: %s", e)
        return -1

    def fetch(self, query: SelectScripts, params=None):
        if not self.connection: 
            logging.debug("No active connection")
        else: 
            try:
                if params:
                    self.cursor.execute(query.script, params)
                else:
                    self.cursor.execute(query.script)
                return self.cursor.fetchall()
            except Error as e:
                logging.error("Error fetching data: %s", e)
        return []
        
    def read(self, script="init"):
        if not self.connection:
            logging.info("No active connection")
        else:
            if not script.endswith('.sql'):
                script += '.sql'
            try:
                with open(f'scripts/{script}', 'r') as f:
                    self.cursor.execute(f.read(), multi=True)
                logging.debug("SQL script '%s' executed successfully", script)
            except Error as e:
                logging.error("Error executing SQL script '%s': %s", script, e)

data = DataController2()
