-- tables
CREATE TABLE IF NOT EXISTS Recipe (
    title VARCHAR(50) PRIMARY KEY,
    description TEXT,
    rating INTEGER,
    meal_timing VARCHAR(50) CHECK(meal_timing IN ('BREAKFAST', 'LUNCH', 'DINNER')),
    favorite BOOLEAN,
    date_published DATE
);

CREATE TABLE IF NOT EXISTS RecipeList (
    name VARCHAR(50) PRIMARY KEY,
    description TEXT
);

CREATE TABLE IF NOT EXISTS Instruction (
    recipe_title VARCHAR(50),
    cook_time INTEGER,
    servings INTEGER,
    calories INTEGER,
    steps TEXT,
    url VARCHAR(255),
    FOREIGN KEY (recipe_title) 
        REFERENCES Recipe(title) 
        ON UPDATE CASCADE 
        ON DELETE NO ACTION
);

CREATE TABLE IF NOT EXISTS Ingredient (
    name VARCHAR(50) PRIMARY KEY,
    inventory VARCHAR(50),
    last_added DATE
);

CREATE TABLE IF NOT EXISTS IngredientList (
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
        ON UPDATE CASCADE
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
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    FOREIGN KEY (recipe_list_name) 
        REFERENCES RecipeList(title)
        ON UPDATE CASCADE 
        ON DELETE NO ACTION
);

CREATE TABLE IF NOT EXISTS ILforI (
    ingredient_list_name VARCHAR(50),
    ingredient_name VARCHAR(50),
    FOREIGN KEY (ingredient_list_name) 
        REFERENCES IngredientList(name)
        ON UPDATE CASCADE
        ON DELETE NO ACTION,
    FOREIGN KEY (ingredient_name) 
        REFERENCES Ingredient(name)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);
