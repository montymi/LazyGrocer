from mysql.connector import connect, Error
import getpass
import logging
import time

from model.enums.scripts import InsertScripts, SelectScripts
from model.enums.tables import Tables

class DataController2:
    def __init__(self, database='lazygrocer', host='localhost', user='root'):
        self.host = host
        self.user = user
        self.password = getpass.getpass("Enter password: ")
        self.database = database
        self.connection = None 
        self.cursor  = None
        self.TESTDB = 'testgrocer'
        self._init_database_()
    
    def clean(self):
        if not self._is_connected_():
            self.connect()           
        try: 
            self.cursor.execute(f"DROP DATABASE IF EXISTS {self.database};")
            self.connection.commit()
            logging.info(f"Succesfully cleaned {self.database}")
        except Error as e:
            logging.error(f"Error cleaning {self.database}:", e)
        self.disconnect()
        self._init_database_()

    def connect(self):
        try:
            if not self._is_connected_():
                self.connection = connect(
                    host=self.host,
                    user=self.user,
                    password=self.password,
                    database=self.database
                )
                if self._is_connected_():
                    logging.debug(f"Connected to {self.database}")
                    self.cursor = self.connection.cursor()
        except Error as e:
            logging.error(f"Failed to connect to the {self.database}:", e)

    def disconnect(self):
        try:
            if not self._is_connected_():
                logging.debug("No active connection")
            else:    
                self.cursor.close()
                self.connection.close() 
                self.cursor = None
                self.connection = None
                logging.debug(f"Disconnected from {self.database}")
        except Error as e:
            logging.error(f"Failed to disconnect from {self.database}: %s", e)

    def execute(self, query: InsertScripts, params: tuple=()):
        if not self._is_connected_(): 
            logging.debug("No active connection")
        elif query.params != len(params):
            logging.debug(f"Incorrect number of parameters: given {len(params)}, needs {query.params}")
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

    def fetch(self, query: SelectScripts, params: tuple=()):
        if not self._is_connected_(): 
            logging.debug("No active connection")
        elif query.params != len(params):
            logging.debug("Incorrect number of parameters given")
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
        if not self._is_connected_():
            logging.info("No active connection")
        else:
            if not script.endswith('.sql'):
                script += '.sql'
            try:
                with open(f'scripts/{script}', 'r') as f:
                    self.cursor.execute(f.read(), multi=True)
                time.sleep(3) # waits for tables to be created
                logging.debug("%s executed successfully", script)
            except Error as e:
                logging.error("Error executing %s: %s", script, e)

    def _get_tables_(self):
        if not self._is_connected_():
            self.connect()          
        try:
            existing_tables = []
            for table in Tables:
                self.cursor.execute(f"SHOW TABLES LIKE '{table.value}';")
                result = self.cursor.fetchone()
                if result:
                    existing_tables.append(table.value)
        except Error as e:
            logging.error("Error checking tables: %s", e)
            return []
        
        logging.debug('Existing tables: %s', ', '.join(existing_tables))
        return existing_tables

    def _init_database_(self):
        try:
            if not self._is_connected_():
                self.connection = connect(
                    host=self.host,
                    user=self.user,
                    password=self.password
                )
            self.cursor = self.connection.cursor()
            self.cursor.execute(f"CREATE DATABASE IF NOT EXISTS {self.database}")
            self.connection.commit()
            self.cursor.execute(f"USE {self.database}")
            self.read()
            if self._get_tables_() == [table.value for table in Tables]:
                    logging.info(f'Successfully initialized {self.database}')
            else: logging.error(f'Not all tables successfully created in {self.database}')
        except Error as e:
            logging.error(f'Error creating {self.database}:', e)

    def _is_connected_(self):
        return self.connection is not None and self.connection.is_connected()