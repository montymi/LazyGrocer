import curses
from services.write_recipe import write
from services.import_recipe import url
from services.pick_recipe import pick

def main():
    print("Services listed below:\n1. Get Grocery List\n2. Write Recipe\n3. Import Recipe\n4. Edit Recipe")
    userInput = input("Pick by number: ")
    selection = int(userInput)
    print(userInput)
    if selection == 1:
        return pick()
    elif selection == 2:
        write()
    elif selection == 3:
        url()
    elif selection == 4:
        raise("Apologies, that service is not offered yet")
    else:
        raise("Please input a number from 1 to 4")

if __name__ == "__main__":
    main()
