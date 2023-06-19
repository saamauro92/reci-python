from time import sleep
import re
from colorama import Fore, Style
import config
import requests

API_URL = "https://tasty.p.rapidapi.com/recipes/list"
API_KEY = config.API_KEY


class RecipeClass:
    
    """ Creates an instance of recipeClass"""

    def __init__(self, name, instructions):

        self.name = name
        self.instructions = instructions

    def print_data(self):
        return f"""
        {self.name}\n \n

        Instructions: \n \n
        {self.instructions}
        """

def display_program_welcome():

    """
    Prints program title.
    Gets initial_text file and prints line every 2 seconds
    """
    print(Fore.GREEN,
        """
 █▀▄ ██▀ ▄▀▀ █    █▀▄ ▀▄▀ ▀█▀ █▄█ ▄▀▄ █▄ █
 █▀▄ █▄▄ ▀▄▄ █ ▀▀ █▀   █   █  █ █ ▀▄▀ █ ▀█

    """ + Style.RESET_ALL)

    with open('initial_text.txt', 'r') as file:
        for line in file:
            print(line, flush=True, end='') 
            #sleep(1)

def ingredient_inputs():
    """
    Get an ingredient and returns a list
    """
    ingredients = []
    while True:
        try:
            ingredient = input( '\n \n--> Add an ingredient. Ex: chicken\n\n')
            match_string = re.match(r'^[a-zA-Z\s]+$', ingredient)
            if match_string == None:
                raise ValueError(f"Please enter a valid text format")
            else:
                ingredients.append(ingredient)
                print(Fore.GREEN,f"\n You have selected " + ", " .join(ingredients)+ Style.RESET_ALL)
                option = display_more_options() 
                if option == 1:                  
                    continue
                elif option == 2:
                    return ingredients
                elif option == 3:
                    print(Fore.GREEN, "\n Starting again...", Style.RESET_ALL)
                    ingredients = []
                    continue            
                                 

        except ValueError as e:
            print(Fore.RED, f"\n/!\ {e} ", Style.RESET_ALL)  
            continue


 


def display_more_options():
    """
    Displays an input and returns the value options 1, 2 or 3
    """
    while True:      
        option_selected = input(""" 
--> Select options:
      1 To add another ingredient
      2 To get recipe
      3 To start again   
 """)
        
        if option_selected == '1':
            return 1
        elif option_selected == '2':
            return 2      
        elif option_selected == '3':
            return 3  
        else:
            print(Fore.RED, "\n/!\ Please enter a valid option"+ Style.RESET_ALL)
            continue

def make_request(ingredients):
    """
    Gets a list of ingredients and make a request to the API
    """
    print("LOADING...")
    QUERYSTRING = {"from": "1", "size": "10", "q": ", ".join(ingredients)}
    HEADERS = {
        "X-RapidAPI-Key": API_KEY,
        "X-RapidAPI-Host": "tasty.p.rapidapi.com"
    }
    response = requests.get(API_URL, headers=HEADERS, params=QUERYSTRING)
    data = response.json()
    if len(data['results']) == 0:
        print(Fore.BLUE, """
        ___________________________________________________
       |                                                   |
       | Sorry, no results found.                          |
       |                                                   |
       | Please double-check your spelling and try again.  |
       |___________________________________________________|


        """)
    else:
        return data


def main():
    
    """
    Run all programs functions

    """

    display_program_welcome()
    ingredients =  ingredient_inputs()
    while True:
            recipe = make_request(ingredients)
            if recipe:
                recipe_name = recipe['results'][0]['name']
                recipe_instructions =  recipe['results'][0]['instructions']
                new_recipe = RecipeClass( recipe_name,  recipe_instructions)
                print(new_recipe.print_data())


main()

