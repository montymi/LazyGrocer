import requests
import json
import os
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from services.add_recipe import add


def url():
    url = input("Recipe URL: ")

    parsed_url = urlparse(url)
    domain_name = parsed_url.netloc
    
    if domain_name in ["www.allrecipes.com", "allrecipes.com"]:
        rName = url.split("/")[-2]
        rName = rName.lower().replace("-","_")
    else:
        raise("ERROR: Link must be from www.allrecipes.com")
    
    rating = input("Rating (optional): ") or None
    notes = input("Notes (optional): ") or None
    
    print("RETRIEVING: ingredients list from URL...")
    ingredients=[]
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.HTTPError as error:
        if error.response.status_code == 404:
            print("ERROR: Page not found")
        else:
            print("ERROR:", error)

    soup = BeautifulSoup(response.content, 'html.parser')
    try:
        spans = soup.find_all('span', {'data-ingredient-name': True})
        for span in spans:
            ing=span.text
            ingredient=ing.replace(" to taste", "")
            ingredients.append(ingredient)
    except:
        raise("WARNING: No spans found with attribute data-ingredient-name")

    rData = {
            "name": rName,
            "rating": rating,
            "notes": notes,
            "url": url,
            "ingredients": ingredients
    }

    add(rData)

if __name__ == "__main__":
    url()
