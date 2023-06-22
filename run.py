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
        print("\nTitle:")
        print(f"     {self.name}")
        print("\nDescription:")
        for desc in description:
            print(f"     {desc}" )

        instructions = self.instructions
        instructions_number = 0
        print("\nInstructions:")
        for instr in instructions:
            instructions_number+= 1
            print(f"    {instructions_number}-  {instr['display_text']}")

        return """
                       _                                     ___  
                _     | |                                   / _ \ 
 ____    ___  _| |_   | |__   _____  ____   ____   _   _   (_( ) )
|  _ \  / _ \(_   _)  |  _ \ (____ ||  _ \ |  _ \ | | | |     (_/ 
| | | || |_| | | |_   | | | |/ ___ || |_| || |_| || |_| |     _   
|_| |_| \___/   \__)  |_| |_|\_____||  __/ |  __/  \__  |    (_)  
                                    |_|    |_|    (____/          
        Try again!
        """

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


def recipe_input(by_type):
    """
    Gets a recipe or ingredients and either return the recipe name or display a list of options
    """
    food = []
    while True:
        try:
            if by_type == "recipe":
                type_of_food = input( '\n \n--> Add recipe name. Ex: chicken curry\n\n')
            elif by_type == "ingredients":
                type_of_food = input( '\n \n--> Add an ingredient. Ex: chicken\n\n')
            else:
                raise ValueError("Invalid input type")

            match_string = re.match(r'^[a-zA-Z\s]+$', type_of_food)

            if match_string is None:
                raise ValueError("Please enter a valid text format")
            else:
                food.append(type_of_food)
                print(Fore.GREEN,f"\n You have selected " + ", " .join(food)+ Style.RESET_ALL)

                if by_type == 'ingredients':
                    option = display_more_options()
                    if option == 1:                  
                        continue
                    elif option == 2:
                        print(Fore.GREEN, "\n Preparing your recipe... \n", Style.RESET_ALL)
                        return food
                    elif option == 3:
                        print(Fore.GREEN, "\n Starting again...", Style.RESET_ALL)
                        food = []
                        continue    
                elif by_type == 'recipe':
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
    option_selected = input("""\n 
--> Select options:
      1 Get recipe by name              0 Exit Program
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
            food = recipe_input('recipe')
            recipe = make_request(food)
            if recipe is not False:
                recipe_name = recipe['results'][0]['name']
                recipe_description = recipe['results'][0]['description']
                recipe_instructions =  recipe['results'][0]['instructions']
                new_recipe = RecipeClass( recipe_name, recipe_description, recipe_instructions)
                print(new_recipe.print_data()) 


        elif option_selected == '2':
            ingredients = recipe_input('ingredients')
            recipe = make_request(ingredients)
            if recipe is not False:
                recipe_name = recipe['results'][0]['name']
                recipe_description = recipe['results'][0]['description']
                recipe_instructions =  recipe['results'][0]['instructions']
                new_recipe = RecipeClass( recipe_name, recipe_description, recipe_instructions)
                print(new_recipe.print_data())
        elif option_selected == '0':
            print("Thanks for using RECI-PYTHON, hope to see you again!")
            break
        else:
            error = ErrorAlertClass()
            error.print_error("Please enter a valid option")
            continue



main()

