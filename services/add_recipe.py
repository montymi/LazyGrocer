import sqlite3
from sqlite3 import Error

def _create_connection(db):
    """
    Create a database connection to the SQLite database
    specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    connection = None
    try:
        connection = sqlite3.connect(db)
        cur = connection.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS recipes
                    (recipe_id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, rating INTEGER, notes TEXT, url TEXT)''')
        cur.execute('''CREATE TABLE IF NOT EXISTS ingredients
                    (recipe_id INTEGER, ingredient TEXT)''')
    except Error as e:
        print("ERROR: ", e)

    return connection

def _add_recipe(conn, r):
    """
    Create a new project into the projects table
    :param conn:
    :param project:
    :return: project id
    """
    sql = '''INSERT INTO recipes(name,rating,notes,url)
              VALUES(?,?,?,?)'''
    cur = conn.cursor()
    cur.execute(sql, r)
    conn.commit()
    lastrowid = cur.lastrowid
    cur.close()
    return lastrowid

def _add_ingredients(conn, items):
    """
    Create a new task
    :param conn:
    :param task:
    :return:
    """

    sql = '''INSERT INTO ingredients(recipe_id,ingredient)
             VALUES(?,?)''' 
    cur = conn.cursor()
    cur.executemany(sql, items)
    conn.commit()
    lastrowid = cur.lastrowid
    cur.close()
    return lastrowid

def add(recipe):
    database = r"recipe.db"

    # create a database connection
    conn = _create_connection(database)
    with conn:
        # create a new project
        rData = (recipe.get("name"), recipe.get("rating"), recipe.get("notes"), recipe.get("url"))
        r_id = _add_recipe(conn, rData)
            
        ingredients=recipe.get("ingredients")

        # tasks
        iData=[]
        for ingredient in ingredients:
            item=(r_id, ingredient)
            iData.append(item)

        # create tasks
        _add_ingredients(conn, iData)

    conn.close()

if __name__ == "__main__":
    add()
