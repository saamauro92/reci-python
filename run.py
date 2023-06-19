from time import sleep
import re

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
    print(
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
    Gets the ingredients and returns a list of them
    """

    ingredients = []
    while True:
        try:
            ingredient_1 = input('\nType and enter your first ingredient\n')
            match = re.match(r'^[a-zA-Z\s]+$', ingredient_1)
            if match == None:
                raise TypeError(f"Please enter a valid text format")
            else:              
                ingredients.append(ingredient_1)
                option_selected = int(input("""
                
                \n
                Select options:
                1- Add other ingredient
                2- Get recipe
            
                """
                ))
                
                print("option selected", option_selected)
        
        except TypeError as e:
            print(f"error:{e} ")
        
        return ingredients



def main():

    """
    Run all programs functions

    """
    display_program_welcome()
    # new_recipe = RecipeClass("fake recipe", "fake instructions...")
    # print(new_recipe.print_data())

    ingredients =  ingredient_inputs()
    print(ingredients)

main()

