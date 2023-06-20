from time import sleep
import re
from colorama import Fore, Style
import config
import requests
from tqdm import trange
from textwrap import TextWrapper
API_URL = "https://tasty.p.rapidapi.com/recipes/list"
API_KEY = config.API_KEY


class RecipeClass:
    
    """ Creates an instance of recipeClass"""

    def __init__(self, name, description, instructions):

        self.name = name
        self.instructions = instructions
        self.description = description

    def print_data(self):
        wrapper = TextWrapper()
        description =  wrapper.wrap(self.description)
        print("\nTitle:\n")
        print(f"     {self.name}\n")
        print("Description:\n")
        for desc in description:
            print(f"     {desc} \n" )

        instructions = self.instructions
        instructions_number = 0
        print("Instructions:")
        for instr in instructions:
            instructions_number+= 1
            print(f"""
    {instructions_number}""", instr['display_text'])

class ErrorAlertClass:

    """ Creates an instance for ErrorAlertClass"""
    def print_error(self, error):
        return print(Fore.RED, f"\n/!\ {error} ", Style.RESET_ALL)
        
        

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
            #sleep(0.90)

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
                    print(Fore.GREEN, "\n Preparing your recipe... \n", Style.RESET_ALL)
                    return ingredients
                elif option == 3:
                    print(Fore.GREEN, "\n Starting again...", Style.RESET_ALL)
                    ingredients = []
                    continue            
                                 

        except ValueError as e:
            error = ErrorAlertClass()
            error.print_error(f"{e}")
            continue

def recipe_by_food_inputs():
    """
    Get a recipe name from input and returns it
    """
    food = []
    while True:
        try:
            recipe = input( '\n \n--> Add recipe name. Ex: chicken curry\n\n')
            match_string = re.match(r'^[a-zA-Z\s]+$', recipe)
            if match_string == None:
                raise ValueError(f"Please enter a valid text format")
            else:
                food.append(recipe)
                print(Fore.GREEN,f"\n You have selected " + ", " .join(food)+ Style.RESET_ALL)
                print(Fore.GREEN, "\n Preparing your recipe... \n", Style.RESET_ALL)
                return food
                                 

        except ValueError as e:
            error = ErrorAlertClass()
            error.print_error(f"{e}")
            continue


 


def display_more_options():
    """
    Displays an input and returns the value options 1, 2 or 3
    """
    while True:      
        option_selected = input(""" 
--> Select options:
      1 To add another ingredient     3 To start again   
      2 To get recipe
      
 \n""")
        
        if option_selected == '1':
            return 1
        elif option_selected == '2':
            return 2      
        elif option_selected == '3':
            return 3  
        else:
            error = ErrorAlertClass()
            error.print_error("Please enter a valid option")
            continue

def make_request(ingredients):
    """
    Gets a list of ingredients and make a request to the API
    """
    QUERYSTRING = {"from": "1", "size": "10", "q": ", ".join(ingredients)}
    HEADERS = {
        "X-RapidAPI-Key": API_KEY,
        "X-RapidAPI-Host": "tasty.p.rapidapi.com"
    }
    try:
        response = requests.get(API_URL, headers=HEADERS, params=QUERYSTRING, timeout=60)
        response.raise_for_status()

        for i in trange(100):
            sleep(0.03)
        data = response.json()
        if len(data['results']) == 0:
            print(Fore.BLUE, """
        ___________________________________________________
       |                                                   |
       | Sorry, no results found.                          |
       |                                                   |
       | Please double-check your spelling and try again.  |
       |___________________________________________________|


        """,Style.RESET_ALL)
            return False
        else:
            return data       
    except requests.exceptions.HTTPError as err:
        print("HTTP Error")
        print(err.args[0])
    except requests.exceptions.Timeout:
        print("Time out")
    except requests.exceptions.ConnectionError:
        print("Connection error")
    except requests.exceptions.RequestException:
        print("Exception request")


def display_menu():
    option_selected = input(""" 
--> Select options:
      1 Get recipe by name
      2 Get recipe by ingredients
         
 \n""")
    return option_selected




def main():
    
    """
    Run all programs functions

    """
    display_program_welcome()
    while True:

        option_selected = display_menu()

        if option_selected == '1':
            food = recipe_by_food_inputs()
            recipe = make_request(food)
            if recipe != False:
                recipe_name = recipe['results'][0]['name']
                recipe_description = recipe['results'][0]['description']
                recipe_instructions =  recipe['results'][0]['instructions']
                new_recipe = RecipeClass( recipe_name, recipe_description, recipe_instructions)
                print(new_recipe.print_data()) 


        elif option_selected == '2':
            ingredients =  ingredient_inputs()
            recipe = make_request(ingredients)
            if recipe != False:
                recipe_name = recipe['results'][0]['name']
                recipe_description = recipe['results'][0]['description']
                recipe_instructions =  recipe['results'][0]['instructions']
                new_recipe = RecipeClass( recipe_name, recipe_description, recipe_instructions)
                print(new_recipe.print_data())
        else:
            error = ErrorAlertClass()
            error.print_error("Please enter a valid option")
            continue



main()

