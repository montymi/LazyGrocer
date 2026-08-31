-- PostgreSQL Migration Script for Recipe Management System
-- This script creates the database schema from scratch

-- Enable UUID extension if needed
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Drop tables if they exist (be careful in production!)
DROP TABLE IF EXISTS recipe_recipe_list CASCADE;
DROP TABLE IF EXISTS grocery_list_ingredient CASCADE;
DROP TABLE IF EXISTS favorites CASCADE;
DROP TABLE IF EXISTS ratings CASCADE;
DROP TABLE IF EXISTS steps CASCADE;
DROP TABLE IF EXISTS instructions CASCADE;
DROP TABLE IF EXISTS recipe_ingredients CASCADE;
DROP TABLE IF EXISTS recipe_lists CASCADE;
DROP TABLE IF EXISTS grocery_lists CASCADE;
DROP TABLE IF EXISTS recipes CASCADE;
DROP TABLE IF EXISTS ingredients CASCADE;

-- Create base tables with soft delete and sharing support

-- Ingredients table
CREATE TABLE ingredients (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL UNIQUE,
    last_added DATE,
    is_deleted BOOLEAN DEFAULT FALSE NOT NULL,
    is_shared BOOLEAN DEFAULT FALSE NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP NOT NULL,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP NOT NULL
);

-- Recipes table
CREATE TABLE recipes (
    id SERIAL PRIMARY KEY,
    title VARCHAR(50) NOT NULL UNIQUE,
    description TEXT,
    date_published DATE,
    is_deleted BOOLEAN DEFAULT FALSE NOT NULL,
    is_shared BOOLEAN DEFAULT FALSE NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP NOT NULL,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP NOT NULL
);

-- Recipe Lists table
CREATE TABLE recipe_lists (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL UNIQUE,
    description TEXT,
    is_deleted BOOLEAN DEFAULT FALSE NOT NULL,
    is_shared BOOLEAN DEFAULT FALSE NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP NOT NULL,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP NOT NULL
);

-- Grocery Lists table
CREATE TABLE grocery_lists (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL UNIQUE,
    description TEXT,
    is_deleted BOOLEAN DEFAULT FALSE NOT NULL,
    is_shared BOOLEAN DEFAULT FALSE NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP NOT NULL,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP NOT NULL
);

-- Recipe-Ingredient relationship with quantity
CREATE TABLE recipe_ingredients (
    id SERIAL PRIMARY KEY,
    recipe_id INTEGER NOT NULL REFERENCES recipes(id) ON DELETE CASCADE,
    ingredient_id INTEGER NOT NULL REFERENCES ingredients(id) ON DELETE CASCADE,
    quantity VARCHAR(50),
    UNIQUE(recipe_id, ingredient_id)
);

-- Instructions table (one-to-one with recipe)
CREATE TABLE instructions (
    id SERIAL PRIMARY KEY,
    recipe_id INTEGER NOT NULL UNIQUE REFERENCES recipes(id) ON DELETE CASCADE,
    cook_time VARCHAR(50),
    prep_time VARCHAR(50),
    servings INTEGER,
    calories INTEGER
);

-- Steps table
CREATE TABLE steps (
    id SERIAL PRIMARY KEY,
    recipe_id INTEGER NOT NULL REFERENCES recipes(id) ON DELETE CASCADE,
    step_number INTEGER NOT NULL,
    description TEXT NOT NULL,
    UNIQUE(recipe_id, step_number)
);

-- Ratings table
CREATE TABLE ratings (
    id SERIAL PRIMARY KEY,
    recipe_id INTEGER NOT NULL REFERENCES recipes(id) ON DELETE CASCADE,
    score INTEGER NOT NULL CHECK (score >= 1 AND score <= 5),
    description TEXT,
    date_added DATE DEFAULT CURRENT_DATE
);

-- Favorites table
CREATE TABLE favorites (
    id SERIAL PRIMARY KEY,
    recipe_id INTEGER NOT NULL REFERENCES recipes(id) ON DELETE CASCADE,
    date_added DATE DEFAULT CURRENT_DATE,
    description TEXT,
    UNIQUE(recipe_id)
);

-- Many-to-many association tables
CREATE TABLE recipe_recipe_list (
    recipe_id INTEGER NOT NULL REFERENCES recipes(id) ON DELETE CASCADE,
    recipe_list_id INTEGER NOT NULL REFERENCES recipe_lists(id) ON DELETE CASCADE,
    PRIMARY KEY (recipe_id, recipe_list_id)
);

CREATE TABLE grocery_list_ingredient (
    grocery_list_id INTEGER NOT NULL REFERENCES grocery_lists(id) ON DELETE CASCADE,
    ingredient_id INTEGER NOT NULL REFERENCES ingredients(id) ON DELETE CASCADE,
    PRIMARY KEY (grocery_list_id, ingredient_id)
);

-- Create indexes for better query performance
CREATE INDEX idx_recipes_title ON recipes(title) WHERE is_deleted = FALSE;
CREATE INDEX idx_recipes_deleted ON recipes(is_deleted);
CREATE INDEX idx_ingredients_name ON ingredients(name) WHERE is_deleted = FALSE;
CREATE INDEX idx_ingredients_deleted ON ingredients(is_deleted);
CREATE INDEX idx_recipe_lists_name ON recipe_lists(name) WHERE is_deleted = FALSE;
CREATE INDEX idx_recipe_lists_deleted ON recipe_lists(is_deleted);
CREATE INDEX idx_grocery_lists_name ON grocery_lists(name) WHERE is_deleted = FALSE;
CREATE INDEX idx_grocery_lists_deleted ON grocery_lists(is_deleted);
CREATE INDEX idx_recipe_ingredients_recipe ON recipe_ingredients(recipe_id);
CREATE INDEX idx_recipe_ingredients_ingredient ON recipe_ingredients(ingredient_id);
CREATE INDEX idx_steps_recipe ON steps(recipe_id);
CREATE INDEX idx_ratings_recipe ON ratings(recipe_id);
CREATE INDEX idx_favorites_recipe ON favorites(recipe_id);

-- Create triggers to update the updated_at timestamp
CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ language 'plpgsql';

CREATE TRIGGER update_recipes_updated_at BEFORE UPDATE ON recipes
    FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER update_ingredients_updated_at BEFORE UPDATE ON ingredients
    FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER update_recipe_lists_updated_at BEFORE UPDATE ON recipe_lists
    FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER update_grocery_lists_updated_at BEFORE UPDATE ON grocery_lists
    FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

-- Migrate data from MySQL dump (example queries)
-- These would need to be run after importing the MySQL data

-- Example: Insert sample data (comment out if migrating from MySQL)
/*
INSERT INTO ingredients (name, last_added) VALUES
    ('Pasta', '2024-04-17'),
    ('Parmesan Cheese', '2024-04-17'),
    ('Black Pepper', '2024-04-17'),
    ('Chicken', '2024-04-17'),
    ('Mozzarella Cheese', '2024-04-17'),
    ('Pizza Sauce', '2024-04-17'),
    ('Dough', '2024-04-17');

INSERT INTO recipes (title, description, date_published) VALUES
    ('Mac', 'Cheesier and delicious!', '2024-04-17'),
    ('Pizza', 'Cheat Meal', '2024-04-17'),
    ('Chicken Parm', 'So good!', '2024-04-16');

INSERT INTO instructions (recipe_id, cook_time, prep_time, servings, calories) VALUES
    (1, '12 min', '5 min', 5, 1500),
    (2, '25 mins', '10', 3, 1000),
    (3, '20 mins', '15 mins', 3, 1000);

INSERT INTO recipe_lists (name, description) VALUES
    ('Pastas', 'For the italians'),
    ('Uno', 'Healthy foods!');

INSERT INTO grocery_lists (name, description) VALUES
    ('Busy Week', 'For when time is running low'),
    ('GL2', 'For pizza');
*/

-- Grant permissions (adjust as needed)
-- GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO your_app_user;
-- GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO your_app_user;