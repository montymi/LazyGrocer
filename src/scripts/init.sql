-- tables
CREATE TABLE IF NOT EXISTS Recipe (
    title VARCHAR(50) PRIMARY KEY,
    description TEXT,
    date_published DATE 
);

CREATE TABLE IF NOT EXISTS Rating (
	recipe_title VARCHAR(50),
    score INTEGER,
    description TEXT,
    date_added DATE,
    FOREIGN KEY (recipe_title)
	REFERENCES Recipe(title)
	ON UPDATE CASCADE 
	ON DELETE CASCADE 
);

CREATE TABLE IF NOT EXISTS Favorite (
	recipe_title VARCHAR(50),
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
	recipe_title VARCHAR(50),
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
    last_added DATE 
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

-- Allows user to read ALL recipes 
DELIMITER //

CREATE PROCEDURE read_all_recipes()
BEGIN
    SELECT 
        r.title AS recipe_title,
        r.description AS description,
        r.date_published AS date_published,
        rt.score AS rating_score,
        rt.description AS rating_description,
        i.cook_time AS instruction_cook_time,
        i.prep_time AS instruction_prep_time,
        i.servings AS instruction_servings,
        i.calories AS instruction_calories,
        s.id AS step_id,
        s.description AS step_description
    FROM 
        Recipe r
    LEFT JOIN 
        Rating rt ON r.title = rt.recipe_title
    LEFT JOIN 
        Instruction i ON r.title = i.recipe_title
    LEFT JOIN 
        Steps s ON r.title = s.recipe_title
    ORDER BY 
        r.title, s.id;
END //

DELIMITER ;


-- Allows user to read ONE SPECIFIC recipe
DELIMITER //

CREATE PROCEDURE read_recipe(IN recipe_title VARCHAR(50))
BEGIN
    SELECT 
        r.title AS recipe_title,
        r.description AS description,
        r.date_published AS date_published,
        rt.score AS rating_score,
        rt.description AS rating_description,
        i.cook_time AS instruction_cook_time,
        i.prep_time AS instruction_prep_time,
        i.servings AS instruction_servings,
        i.calories AS instruction_calories,
        s.id AS step_id,
        s.description AS step_description
    FROM 
        Recipe r
    LEFT JOIN 
        Rating rt ON r.title = rt.recipe_title
    LEFT JOIN 
        Instruction i ON r.title = i.recipe_title
    LEFT JOIN 
        Steps s ON r.title = s.recipe_title
    WHERE 
        r.title = recipe_title
    ORDER BY 
        r.title, s.id;
END //

DELIMITER ;


-- Allows the user to read ALL recipe lists
DELIMITER //

CREATE PROCEDURE read_all_recipe_lists()
BEGIN
    SELECT name, description
    FROM RecipeList;
END //

DELIMITER ;


-- Allows the user to read ONE SPECIFIC recipe list
DELIMITER //

CREATE PROCEDURE read_recipe_list(IN list_name VARCHAR(50))
BEGIN
    SELECT name, description
    FROM RecipeList
    WHERE name = list_name;
END //

DELIMITER ;


-- Allows the user to read ALL grocery lists
DELIMITER //

CREATE PROCEDURE read_all_grocery_lists()
BEGIN
    SELECT name, description
    FROM GroceryList;
END //

DELIMITER ;


-- Allows the user to read ONE SPECIFIC grocery list
DELIMITER //

CREATE PROCEDURE read_grocery_list(IN list_name VARCHAR(50))
BEGIN
    SELECT name, description
    FROM GroceryList
    WHERE name = list_name;
END //

DELIMITER ;


-- Allows the user to read ALL ingredients
DELIMITER //

CREATE PROCEDURE read_all_ingredients()
BEGIN
    SELECT name, inventory, last_added
    FROM Ingredient;
END //

DELIMITER ;


-- Allows the user to read ONE SPECIFIC ingredient
DELIMITER //

CREATE PROCEDURE read_ingredient(IN ingredient_name VARCHAR(50))
BEGIN
    SELECT name, inventory, last_added
    FROM Ingredient
    WHERE name = ingredient_name;
END //

DELIMITER ;


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
