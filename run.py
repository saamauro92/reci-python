from time import sleep
import re
from colorama import Fore
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
              WELCOME TO

 █▀▄ ██▀ ▄▀▀ █    █▀▄ ▀▄▀ ▀█▀ █▄█ ▄▀▄ █▄ █
 █▀▄ █▄▄ ▀▄▄ █ ▀▀ █▀   █   █  █ █ ▀▄▀ █ ▀█

             (RECI-PYTHON)

    
    """)

    with open('initial_text.txt', 'r') as file:
        for line in file:
            print(line, flush=True, end='\n') 
            #sleep(2)

def ingredient_inputs():
    """
    Get an ingredient and returns a list
    """
    ingredients = []
    while True:
        try:
            ingredient = input(Fore.YELLOW +'\n--> Type and enter your ingredient ex: chicken\n\n')
            match_string = re.match(r'^[a-zA-Z\s]+$', ingredient)
            if match_string == None:
                raise ValueError(f"Please enter a valid text format")
            else:
                ingredients.append(ingredient)
                print(Fore.GREEN,f"\n --You have selected " + ", ".join(ingredients))
                option = display_more_options() 
                if option == 1:                  
                    continue
                elif option == 2:
                    return ingredients
                elif option == 3:
                    ingredients = []
                    continue            
                                 

        except ValueError as e:
            print(Fore.MAGENTA, f"\n // {e} ")  
            continue


 


def display_more_options():
    """
    Displays an input and returns the value options 1, 2 or 3
    """
    while True:      
        option_selected = input(Fore.YELLOW + """
                
--> Select options:
        Type 1 and enter to add other ingredient
        Type 2 and enter to get the recipe
        type 3 to start again   
            
                    """)
        
        if option_selected == '1':
            return 1
        elif option_selected == '2':
            return 2      
        elif option_selected == '3':
            return 3  
        else:
            print(Fore.MAGENTA, "\n // Please enter a valid option")
            continue

def make_request(ingredients):
    """
    Gets a list of ingredients and make a request to the API 
    """
    QUERYSTRING = {"from": "1", "size": "1", "q": ", ".join(ingredients)}
    HEADERS = {
        "X-RapidAPI-Key": API_KEY,
        "X-RapidAPI-Host": "tasty.p.rapidapi.com"
    }
    response = requests.get(API_URL, headers=HEADERS, params=QUERYSTRING)
    print(response.json())




def main():
    
    """
    Run all programs functions

    """

    display_program_welcome()
    # new_recipe = RecipeClass("fake recipe", "fake instructions...")
    # print(new_recipe.print_data())

    ingredients =  ingredient_inputs()
    make_request(ingredients)



main()

