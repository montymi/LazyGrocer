-- tables
CREATE TABLE IF NOT EXISTS Recipe (
    title VARCHAR(50) PRIMARY KEY,
    description TEXT,
    date_published DATE CHECK(date_published REGEXP '[0-9]{4}-[0-9]{2}-[0-9]{2}')
);

CREATE TABLE IF NOT EXISTS Rating (
    score INTEGER,
    description TEXT,
    date_added DATE
    FOREIGN KEY (recipe_title)
	REFERENCES Recipe(title)
	ON UPDATE CASCADE 
	ON DELETE CASCADE 
);

CREATE TABLE IF NOT EXISTS Favorite (
    date_added DATE,
    description TEXT,
    FOREIGN KEY (recipe_title)
	REFERENCES Recipe(title)
	ON UPDATE CASCADE 
	ON DELETE CASCADE 
);

CREATE TABLE IF NOT EXISTS RecipeList (
    name VARCHAR(50) PRIMARY KEY,
    description TEXT
);

CREATE TABLE IF NOT EXISTS Instruction (
    recipe_title VARCHAR(50) PRIMARY KEY,
    cook_time VARCHAR(50),
    prep_time VARCHAR(50),
    servings INTEGER,
    calories INTEGER,
    FOREIGN KEY (recipe_title) 
        REFERENCES Recipe(title) 
        ON UPDATE CASCADE 
        ON DELETE NO ACTION
);

CREATE TABLE IF NOT EXISTS Steps (
    id INTEGER PRIMARY KEY,
    description TEXT,
    FOREIGN KEY (recipe_title)
	REFERENCES Recipe(title)
	ON UPDATE CASCADE
	ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS Ingredient (
    name VARCHAR(50) PRIMARY KEY,
    inventory VARCHAR(50),
    last_added DATE CHECK(last_added REGEXP '[0-9]{4}-[0-9]{2}-[0-9]{2}')
);

CREATE TABLE IF NOT EXISTS GroceryList (
    name VARCHAR(50) PRIMARY KEY,
    description TEXT
);

-- relationship tables
CREATE TABLE IF NOT EXISTS RincludesI (
    recipe_title VARCHAR(50),
    ingredient_name VARCHAR(50),
    quantity VARCHAR(50),
    FOREIGN KEY (recipe_title) 
        REFERENCES Recipe(title)
        ON UPDATE NO ACTION
        ON DELETE CASCADE,
    FOREIGN KEY (ingredient_name) 
        REFERENCES Ingredient(name)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS RinRL (
    recipe_title VARCHAR(50),
    recipe_list_name VARCHAR(50),
    FOREIGN KEY (recipe_title) 
        REFERENCES Recipe(title)
        ON UPDATE NO ACTION
        ON DELETE CASCADE,
    FOREIGN KEY (recipe_list_name) 
        REFERENCES RecipeList(name)
        ON UPDATE CASCADE 
        ON DELETE NO ACTION
);

CREATE TABLE IF NOT EXISTS ILforI (
    grocery_list_name VARCHAR(50),
    ingredient_name VARCHAR(50),
    FOREIGN KEY (grocery_list_name) 
        REFERENCES GroceryList(name)
        ON UPDATE CASCADE
        ON DELETE NO ACTION,
    FOREIGN KEY (ingredient_name) 
        REFERENCES Ingredient(name)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);

-- Functions: 
-- create:
-- - Recipe 
-- - RecipeList
-- - GroceryList
-- read: 
-- - Recipe 
-- - RecipeList
-- - GroceryList
-- - Ingredient
-- update: 
-- - Recipe 
-- - RecipeList
-- - GroceryList
-- - Ingredient
-- delete:
-- - Recipe 
-- - RecipeList
-- - GroceryList
