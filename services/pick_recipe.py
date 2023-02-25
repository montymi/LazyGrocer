import os
import json
import curses
import sqlite3
from sqlite3 import Error


class ItemSelector:
    def __init__(self, items):
        self.items = items
        self.selected_items = []

        self.stdscr = curses.initscr()
        curses.cbreak()
        curses.noecho()
        self.stdscr.keypad(True)

        self.stdscr.addstr(0, 0, "Select items:")
        for i, item in enumerate(self.items):
            self.stdscr.addstr(i + 1, 1, f"{i+1}. {item}")
        self.stdscr.addstr(len(self.items) + 2, 0, "Press space to select an item, enter to finish.")

        self.current_row = 1
        self.selections = [False] * len(self.items)
        self.run()

    def run(self):
    # Initialize the current row to the first row
        current_row = 0

        while True:
            # Clear the screen
            self.stdscr.clear()

            self.stdscr.addstr(0, 0, "Use arrow keys to move cursor, space to select/deselect items, and enter to finish.")

            # Iterate over the items and print them to the screen
            for i, item in enumerate(self.items):
                # Check if the current item is selected and highlight it if it is
                if i == current_row:
                    self.stdscr.addstr(i+1, 0, "[>]\t" + item, curses.A_REVERSE)
                else:
                    self.stdscr.addstr(i+1, 0, "[ ]\t" + item)

                 # Add a checkmark next to the item if it's selected
                if self.selections[i]:
                    self.stdscr.addstr(i+1, 0, "[X]\t" + item, curses.A_REVERSE) if i == current_row else self.stdscr.addstr(i+1, 0, "[X]\t" + item)

            # Refresh the screen to display the updated content
            self.stdscr.refresh()

            self.stdscr.addstr(len(self.items) + 1, 0, "Resulting grocery list will be printed upon completion.")

            # Wait for user input
            key = self.stdscr.getch()

            # Check which key was pressed and update the current row or selection as necessary
            if key == curses.KEY_UP:
                current_row = max(0, current_row - 1)
            elif key == curses.KEY_DOWN:
                current_row = min(len(self.items) - 1, current_row + 1)
            elif key == ord(" "):
                self.selections[current_row] = not self.selections[current_row]
            elif key == ord("\n"):
                for i, item in enumerate(self.items):
                    if self.selections[i]:
                        self.selected_items.append(item)
                break

        # Restore the terminal settings
        curses.echo()
        curses.nocbreak()
        curses.endwin()

def pick():
    DB = r"recipe.db"
    GROCERIES=[]
    conn = None
    try:
        conn = sqlite3.connect(DB)
        cur = conn.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS recipes
                    (recipe_id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, rating INTEGER, notes TEXT, url TEXT)''')
        cur.execute('''CREATE TABLE IF NOT EXISTS ingredients
                    (recipe_id INTEGER, ingredient TEXT)''')
    except Error as e:
        print("ERROR: ", e)
    cur = conn.cursor()
    cur.execute('''SELECT name FROM recipes''')
    items = [item[0] for item in cur.fetchall()]
    selector = ItemSelector(items)
    ingredientsQuery = "SELECT ingredient FROM ingredients JOIN recipes ON ingredients.recipe_id = recipes.recipe_id WHERE name = ?"
    for item in selector.selected_items:
        cur.execute(ingredientsQuery, (item,))
        items = [ingredient[0] for ingredient in cur.fetchall()]
        GROCERIES.extend(items)

    cur.close()
    conn.close()
    return GROCERIES

if __name__ == "__main__":
    groceryList = pick()
