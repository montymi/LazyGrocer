from mysql.connector import connect, Error
import logging
import os
import time

from model.enums.scripts import InsertScripts, SelectScripts
from model.enums.tables import Tables

db_config = {
    'host': os.getenv('MYSQL_HOST', 'db'),
    'port': int(os.getenv('MYSQL_PORT', 3306)),
    'user': os.getenv('MYSQL_USER', 'root'),
    'password': os.getenv('MYSQL_PASSWORD', 'lg-db-pd'),
    'database': os.getenv('MYSQL_DATABASE', 'lazygrocer'),
}

class DataController2:
    def __init__(self, database=db_config.get("database"), host=db_config.get("host"), user=db_config.get("user"), password=db_config.get("password")):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None 
        self.cursor  = None
    
    def clean(self):
        if not self._is_connected_():
            try:
                self.connect()
            except Error as e:
                logging.error(f"Error connecting to {self.database}:", e)       
        try: 
            self.cursor.execute(f"DROP DATABASE IF EXISTS {self.database};")
            self.connection.commit()
            logging.debug(f"Succesfully cleaned {self.database}")
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
                self.connection.commit()
                return self.cursor.fetchall()
            except Error as e:
                logging.error("Error fetching data: %s", e)
        return []
        
    def read(self, script="init"):
        if not self._is_connected_():
            logging.debug("No active connection")
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

    def procedure(self, procedure_name, args=None):
        if not self._is_connected_():
            logging.debug("No active connection")
            return None
        else:
            try:
                if args is None:
                    self.cursor.callproc(procedure_name)
                else:
                    self.cursor.callproc(procedure_name, args)
                # Fetch output parameters
                results = []
                for result in self.cursor.stored_results():
                    results.append(result.fetchall())

                self.connection.commit()  # Commit changes (if any)
                logging.debug("Procedure %s called successfully", procedure_name)
                return results
            except Error as e:
                logging.error("Error executing procedure %s: %s", procedure_name, e)
                return None

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
                    logging.debug(f'Successfully initialized {self.database}')
            else: logging.error(f'Not all tables successfully created in {self.database}')
        except Error as e:
            logging.error(f'Error creating {self.database}:', e)

    def _is_connected_(self):
        return self.connection is not None and self.connection.is_connected()
