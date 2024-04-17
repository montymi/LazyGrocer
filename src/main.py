import logging
import argparse

from controller.dataControllerv2 import DataController2 as DataController
from model.enums.scripts import SelectScripts, InsertScripts

def main(db):
    print("Select Service:\n1. Create\n2. Read\n3. Update\n4. Replace")
    service = input("Enter Service Key Number: ")
    if service == 1: # create
        print("Select CREATE Service:\n1. Recipe\n2. Grocery List\n3. Recipe List")
        create_service = input("Enter CREATE Key Number: ")
        if create_service == 1: # recipe
            pass 
        elif create_service == 2: # grocery list
            pass 
        elif create_service == 3: # recipe list
            pass
        else:
            pass 
    elif service == 2: # read
        print("Select READ Service:\n1. Recipe\n2. Ingredient 3. Grocery List\n4. Recipe List")
        read_service = input("Enter READ Key Number: ")
        if read_service == 1: # recipe
            pass 
        elif read_service == 2: # ingredient
            pass 
        elif read_service == 3: # grocery list
            pass
        elif read_service == 4: # recipe list
            pass
        else:
            pass  
    elif service == 3: # update
        print("Select UPDATE Service:\n1. Recipe\n2. Ingredient 3. Grocery List\n4. Recipe List")
        update_service = input("Enter UPDATE Key Number: ")
        if update_service == 1: # recipe
            pass 
        elif update_service == 2: # ingredient
            pass 
        elif update_service == 3: # grocery list
            pass
        elif update_service == 4: # recipe list
            pass
        else:
            pass  
        pass 
    elif service == 4: # delete
        print("Select UPDATE Service:\n1. Recipe\n2. Ingredient 3. Grocery List\n4. Recipe List")
        delete_service = input("Enter UPDATE Key Number: ")
        if delete_service == 1: # recipe
            pass 
        elif delete_service == 3: # grocery list
            pass
        elif delete_service == 4: # recipe list
            pass
        else:
            pass  
        pass 

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Run unit tests with different logging levels')
    parser.add_argument('-D', '--debug', action='store_const', const=logging.DEBUG, dest='log_level', 
                        help='Set logging level to DEBUG')
    parser.add_argument('-I', '--info', action='store_const', const=logging.INFO, dest='log_level', 
                        help='Set logging level to INFO (default)')
    parser.add_argument('-W', '--warning', action='store_const', const=logging.WARNING,dest='log_level', 
                        help='Set logging level to WARNING')
    parser.add_argument('-E', '--error', action='store_const', const=logging.ERROR, dest='log_level', 
                        help='Set logging level to ERROR')
    parser.add_argument('-C', '--critical', action='store_const', const=logging.CRITICAL, dest='log_level',
                        help='Set logging level to CRITICAL')
    args = parser.parse_args()

    if args.log_level is not None:
        logging.basicConfig(level=args.log_level)
    else:
        logging.basicConfig(level=logging.INFO)

    db = DataController()
    main(db)
