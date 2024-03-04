import json
import os
from services.add_recipe import add

"""
JSON STRUCTURE
*everything is a string*
name
rating
notes
ingredients
  name: amount
  name: amount
  name: amount
"""

# USER INPUT
def write():
    rName = input("Recipe Name: ").lower().replace('\\','')
    rating = input("Rating (optional): ").replace('\\','') or None
    notes = input("Notes (optional): ").replace('\\','') or None
    print("Add ingredients and any amount metric below ('done' to finish).")
    
    ingredients=[]
    while True:
        iName = input("Ingredient: ").lower().replace('\\','')
        if iName.endswith('s'):
            iName = iName[:-1]
        if iName == "done":
            break    
        ingredients.append(iName)

    rData = {
            "name": rName.replace(" ","_"),
            "rating": rating,
            "notes": notes,
            "ingredients": ingredients
    }

    add(rData)

if __name__ == "__main__":
    write()
