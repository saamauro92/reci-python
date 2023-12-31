from time import sleep
import re
from colorama import Fore, Style
import config
import requests
from tqdm import trange
from textwrap import TextWrapper
import sys
import time

API_URL = config.API_URL
API_KEY = config.API_KEY


class RecipeClass:
    """ Creates an instance of recipeClass"""

    def __init__(self, name, description, instructions):

        self.name = name
        self.instructions = instructions
        self.description = description

    def print_data(self):
        wrapper = TextWrapper()
        description = wrapper.wrap(self.description)
        text_slowly("\nTitle: \n")
        text_slowly(f"\n     {self.name} \n")
        text_slowly("\nDescription: \n")
        for desc in description:
            text_slowly(f"\n     {desc} \n")

        instructions = self.instructions
        instructions_number = 0
        text_slowly("\nInstructions: \n")
        for instr in instructions:
            instructions_number += 1
            text_slowly(f" \n{instructions_number}) {instr['display_text']}\n")
        # print art text not happy? try again
        with open("not_happy.txt", 'r') as file:
            not_happy_art_text = file.read()
        text_slowly(not_happy_art_text)
        return (Fore.LIGHTYELLOW_EX +
                "\n ** SCROLL UP TO SEE FULL RECIPE *** "
                + Style.RESET_ALL)


class ErrorAlertClass:

    """ Creates an instance for ErrorAlertClass"""
    def print_error(self, error):
        return print(Fore.RED, f"\n \U0001F6AB " f" {error}{Style.RESET_ALL}")


def text_slowly(string):
    """
    This function will take a string and print it slowly like simulating typing
    """
    for letter in string:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(3.0/300)


def display_program_welcome():

    """
    Prints program title.
    Gets initial_text file and prints line every 2 seconds
    """
    with open("logo.txt", "r") as file:
        logo_art = file.read()
    print(Fore.GREEN, logo_art + Style.RESET_ALL)

    with open('initial_text.txt', 'r') as file:
        for line in file:
            print(line, flush=True, end='')


def recipe_input(by_type):
    """
    Gets a recipe or ingredients and either return
    the recipe name or display a list of options
    """
    food = []
    while True:
        try:
            if by_type == "recipe":
                type_of_food = input(
                 f"\n\n{Fore.CYAN}-->" +
                 f"{Style.RESET_ALL}"
                 + " Add recipe name. Ex: chicken curry\n\n")
            elif by_type == "ingredients":
                type_of_food = input(
                 f"\n\n{Fore.CYAN}-->" +
                 f"{Style.RESET_ALL}" +
                 " Add one ingredient. Ex: chicken\n\n")
            else:
                raise ValueError("Invalid input type")

            match_string = re.match(r'^[a-zA-Z\s]+$', type_of_food)
            if match_string is None:
                raise ValueError("Please enter a valid text format")
            elif len(type_of_food) < 3:
                raise ValueError("Please enter more than 3 characters")
            else:
                food.append(type_of_food)
                print(Fore.GREEN, "\n You have selected " + ", ".join(food)
                                                            + Style.RESET_ALL)
                if by_type == 'ingredients':
                    option = display_more_options()
                    if option == 1:
                        continue
                    elif option == 2:
                        print(f"""{Fore.GREEN}
                        \n Preparing your recipe/s... \n
                        {Style.RESET_ALL}""")
                        return food
                    elif option == 3:
                        print(f"""{Fore.GREEN}
                        \n Starting again...
                        {Style.RESET_ALL}""")
                        food = []
                        return False
                elif by_type == 'recipe':
                    print(f"""{Fore.GREEN}
                    \n Preparing your recipe... \n
                    {Style.RESET_ALL}""")
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
        option_selected = input(
           f"\n{Fore.CYAN}-->{Style.RESET_ALL} Select options:\n" +
           "      1 To add another ingredient     3 To start again\n" +
           "      2 To get recipe \n")
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
    Gets a list of ingredients and requests to API
    """
    QUERYSTRING = {"from": "1", "size": "10", "q": ", ".join(ingredients)}
    HEADERS = {
        "X-RapidAPI-Key": API_KEY,
        "X-RapidAPI-Host": "tasty.p.rapidapi.com"
    }
    try:
        response = requests.get(API_URL, headers=HEADERS, params=QUERYSTRING,
                                timeout=60)
        response.raise_for_status()

        for i in trange(100):
            sleep(0.03)
        data = response.json()
        if len(data['results']) == 0:
            print(Fore.BLUE, """
        ___________________________________________________
       |                                                   |
       | Sorry, no results were found.                     |
       |                                                   |
       | Please double-check your spelling and try again.  |
       |___________________________________________________|
        """, Style.RESET_ALL)
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
    """
    This function displays the main menu input that returns the selected option
    """
    option_selected = input(
        f"\n{Fore.CYAN}" +
        f"\n-->{Style.RESET_ALL} Select option: \n" +
        "      1 Get the recipe by name              0 Exit Program\n"
        "      2 Get the recipe by ingredients \n")
    return option_selected


def recipe_data_format(recipe):
    """
    Get recipe data and creates an instance of RecipeClass with the data
    """
    recipe_name = recipe['name']
    recipe_description = recipe['description']
    recipe_instructions = recipe['instructions']
    new_recipe = RecipeClass(recipe_name, recipe_description,
                             recipe_instructions)
    print(new_recipe.print_data())


def select_recipe_options(recipes):
    """
    Gets the recipes and displays a list of them to choose them
    """
    while True:
        print("\n We have prepared these recipes: \n")
        recipe_counter = 1
        for res in recipes['results']:
            print(f"{recipe_counter} - {res['name']}")
            recipe_counter += 1
            # get a max of 5 recipes
            if recipe_counter == 6:
                break
        print("\n0 - To go back to main")
        recipe_choosen = input(
            "\n" + Fore.CYAN + "--> " + Style.RESET_ALL +
            "Select the recipe you want \n")
        if recipe_choosen == "0":
            break
        elif (recipe_choosen.isdigit() and
                int(recipe_choosen) in
                range(0, len(recipes['results']) + 1)):
            recipe_data_format(recipes['results'][int(recipe_choosen) - 1])
        else:
            error = ErrorAlertClass()
            error.print_error(f"Please select a valid option")


def process_recipe_input(input_type):
    """
    Process recipe inputs based on the input type and returns the recipe
    """
    if input_type == "recipe":
        food = recipe_input('recipe')
    elif input_type == "ingredients":
        ingredients = recipe_input('ingredients')
        food = ingredients
    if food is not False:
        recipes = make_request(food)
        if recipes is not False:
            select_recipe_options(recipes)
    else:
        return None


def main():
    """
    Run all programs functions

    """
    display_program_welcome()
    while True:

        option_selected = display_menu()

        if option_selected == '1':
            process_recipe_input("recipe")
        elif option_selected == '2':
            process_recipe_input("ingredients")
        elif option_selected == '0':
            print("Thanks for using RECI-PYTHON, hope to see you again!")
            break
        else:
            error = ErrorAlertClass()
            error.print_error("Please enter a valid option")
            continue


main()

