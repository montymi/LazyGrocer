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


-- Allows the user to add a recipe to the recipe table
DELIMITER //

CREATE PROCEDURE add_recipe(
    IN recipe_title VARCHAR(50),
    IN recipe_description TEXT,
    IN date_published DATE
)
BEGIN
    INSERT INTO Recipe (title, description, date_published)
    VALUES (recipe_title, recipe_description, date_published);
END //

DELIMITER ;


-- Allows the user to add a rating to the rating table
DELIMITER //

CREATE PROCEDURE add_rating(
    IN recipe_title VARCHAR(50),
    IN score INTEGER,
    IN rating_description TEXT,
    IN date_added DATE
)
BEGIN
    INSERT INTO Rating (recipe_title, score, description, date_added)
    VALUES (recipe_title, score, rating_description, date_added);
END //

DELIMITER ;


-- Allows the user to add steps to the steps table
DELIMITER //

CREATE PROCEDURE add_step(
    IN recipe_title VARCHAR(50),
    IN step_description TEXT
)
BEGIN
    INSERT INTO Steps (recipe_title, description)
    VALUES (recipe_title, step_description);
END //

DELIMITER ;


-- Allows the user to add instructons to the instructions table
DELIMITER //

CREATE PROCEDURE add_instruction(
    IN recipe_title VARCHAR(50),
    IN cook_time VARCHAR(50),
    IN prep_time VARCHAR(50),
    IN servings INTEGER,
    IN calories INTEGER
)
BEGIN
    INSERT INTO Instruction (recipe_title, cook_time, prep_time, servings, calories)
    VALUES (recipe_title, cook_time, prep_time, servings, calories);
END //

DELIMITER ;


-- Allows the user to add a recipe list to the recipe list table
DELIMITER //

CREATE PROCEDURE add_recipe_list(
    IN list_name VARCHAR(50),
    IN list_description TEXT
)
BEGIN
    INSERT INTO RecipeList (name, description)
    VALUES (list_name, list_description);
END //

DELIMITER ;


-- Allows the user to add a grocery list to the grocery list table
DELIMITER //

CREATE PROCEDURE add_grocery_list(
    IN list_name VARCHAR(50),
    IN list_description TEXT
)
BEGIN
    INSERT INTO GroceryList (name, description)
    VALUES (list_name, list_description);
END //

DELIMITER ;


-- Allows the user to add an ingredient to the ingredient table 
DELIMITER //

CREATE PROCEDURE add_ingredient(
    IN ingredient_name VARCHAR(50),
    IN inventory VARCHAR(50),
    IN last_added DATE
)
BEGIN
    INSERT INTO Ingredient (name, inventory, last_added)
    VALUES (ingredient_name, inventory, last_added);
END //

DELIMITER ;


-- Allows the user to update the values in the recipe table
DELIMITER //

CREATE PROCEDURE update_recipe(
    IN old_recipe_title VARCHAR(50),
    IN new_recipe_title VARCHAR(50),
    IN new_recipe_description TEXT,
    IN new_date_published DATE
)
BEGIN
    UPDATE Recipe
    SET title = new_recipe_title,
        description = new_recipe_description,
        date_published = new_date_published
    WHERE title = old_recipe_title;
END //

DELIMITER ;


-- Allows the user to update the values in the rating table 
DELIMITER //

CREATE PROCEDURE update_rating(
    IN recipe_title VARCHAR(50),
    IN new_score INTEGER,
    IN new_rating_description TEXT,
    IN new_date_added DATE
)
BEGIN
    UPDATE Rating
    SET score = new_score,
        description = new_rating_description,
        date_added = new_date_added
    WHERE recipe_title = recipe_title;
END //

DELIMITER ;


-- Allows the user to update the values in the instructions table 
DELIMITER //

CREATE PROCEDURE update_instruction(
    IN recipe_title VARCHAR(50),
    IN new_cook_time VARCHAR(50),
    IN new_prep_time VARCHAR(50),
    IN new_servings INTEGER,
    IN new_calories INTEGER
)
BEGIN
    UPDATE Instruction
    SET cook_time = new_cook_time,
        prep_time = new_prep_time,
        servings = new_servings,
        calories = new_calories
    WHERE recipe_title = recipe_title;
END //

DELIMITER ;


-- Allows the user to update the values in the steps table 
DELIMITER //

CREATE PROCEDURE update_step(
    IN recipe_title VARCHAR(50),
    IN step_id INTEGER,
    IN new_step_description TEXT
)
BEGIN
    UPDATE Steps
    SET description = new_step_description
    WHERE recipe_title = recipe_title AND id = step_id;
END //

DELIMITER ;


-- Allows the user to update the values in the recipe list table 
DELIMITER //

CREATE PROCEDURE update_recipe_list(
    IN old_list_name VARCHAR(50),
    IN new_list_name VARCHAR(50),
    IN new_list_description TEXT
)
BEGIN
    UPDATE RecipeList
    SET name = new_list_name,
        description = new_list_description
    WHERE name = old_list_name;
END //

DELIMITER ;


-- Allows the user to update the values in the grocery list table
DELIMITER //

CREATE PROCEDURE update_grocery_list(
    IN old_list_name VARCHAR(50),
    IN new_list_name VARCHAR(50),
    IN new_list_description TEXT
)
BEGIN
    UPDATE GroceryList
    SET name = new_list_name,
        description = new_list_description
    WHERE name = old_list_name;
END //

DELIMITER ;


-- Allows the user to update the values in the ingredient table
DELIMITER //

CREATE PROCEDURE update_ingredient(
    IN old_ingredient_name VARCHAR(50),
    IN new_ingredient_name VARCHAR(50),
    IN new_inventory VARCHAR(50),
    IN new_last_added DATE
)
BEGIN
    UPDATE Ingredient
    SET name = new_ingredient_name,
        inventory = new_inventory,
        last_added = new_last_added
    WHERE name = old_ingredient_name;
END //

DELIMITER ;


-- Allows the user to update the values in the favorites table
DELIMITER //

CREATE PROCEDURE update_favorite(
    IN recipe_title VARCHAR(50),
    IN new_date_added DATE,
    IN new_description TEXT
)
BEGIN
    UPDATE Favorite
    SET date_added = new_date_added,
        description = new_description
    WHERE recipe_title = recipe_title;
END //

DELIMITER ;



-- Allows the user to delete a recipe from the recipe table 
DELIMITER //

CREATE PROCEDURE delete_recipe(
    IN recipe_title VARCHAR(50)
)
BEGIN
    DELETE FROM Rating
    WHERE recipe_title = recipe_title;

    DELETE FROM Favorite
    WHERE recipe_title = recipe_title;

    DELETE FROM Instruction
    WHERE recipe_title = recipe_title;

    DELETE FROM Steps
    WHERE recipe_title = recipe_title;

    DELETE FROM Recipe
    WHERE title = recipe_title;
END //

DELIMITER ;


-- Allows the user to delete a recipe list from the recipe list table 
DELIMITER //

CREATE PROCEDURE delete_recipe_list(
    IN list_name VARCHAR(50)
)
BEGIN
    DELETE FROM RecipeList
    WHERE name = list_name;
END //

DELIMITER ;


-- Allows the user to delete an ingredient from the ingredient table 
DELIMITER //

CREATE PROCEDURE delete_ingredient(
    IN ingredient_name VARCHAR(50)
)
BEGIN
    DELETE FROM Ingredient
    WHERE name = ingredient_name;
END //

DELIMITER ;


-- Allows the user to delete a grocery list from the grocery list table 
DELIMITER //

CREATE PROCEDURE delete_grocery_list(
    IN list_name VARCHAR(50)
)
BEGIN
    DELETE FROM GroceryList
    WHERE name = list_name;
END //

DELIMITER ;
