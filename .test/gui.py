import curses

# Sample data - list of recipes and ingredients
recipes = [
    {"name": "Spaghetti Carbonara", "ingredients": ["spaghetti", "eggs", "bacon", "parmesan cheese"]},
    {"name": "Chicken Curry", "ingredients": ["chicken", "curry sauce", "rice", "onion", "garlic"]},
    {"name": "Caesar Salad", "ingredients": ["romaine lettuce", "croutons", "parmesan cheese", "caesar dressing"]}
]

# Function to draw the header
def draw_header(stdscr):
    stdscr.addstr(0, 0, "Recipe List - Commands: [A]dd [E]dit [D]elete [Q]uit")
    stdscr.refresh()

# Function to draw the list of recipes
def draw_recipes(stdscr, selected_row):
    stdscr.clear()
    draw_header(stdscr)
    for i, recipe in enumerate(recipes):
        x = 2
        y = i + 2
        if i == selected_row:
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(y, x, f"{recipe['name']}")
            stdscr.attroff(curses.color_pair(1))
        else:
            stdscr.addstr(y, x, f"{recipe['name']}")
    stdscr.refresh()

# Function to handle user input
def main(stdscr):
    # Initialize color pair for selected row
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    # Turn off cursor display
    curses.curs_set(0)
    # Set up keyboard input
    stdscr.keypad(True)
    
    current_row = 0
    draw_recipes(stdscr, current_row)
    
    while True:
        key = stdscr.getch()
        stdscr.clear()
        
        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        elif key == curses.KEY_DOWN and current_row < len(recipes) - 1:
            current_row += 1
        elif key == ord('q'):
            break
        
        draw_recipes(stdscr, current_row)

curses.wrapper(main)

