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
    Get an ingredient and returns a list
    """
    ingredients = []
    while True:
        try:
            ingredient = input('\nType and enter your ingredient\n')
            match_string = re.match(r'^[a-zA-Z\s]+$', ingredient)
            if match_string == None:
                raise ValueError(f"Please enter a valid text format")
            else:
                ingredients.append(ingredient)
                option = display_more_options() 
                if option == 1:                  
                    continue
                elif option == 2:
                    return ingredients
                else:
                    print("Please enter a valid option")
                    continue                   
                                 

        except ValueError as e:
            print(f"error:{e} ")  
            continue


 


def display_more_options():
    """
    Displays an input and returns the value of it, options 1 or 2 if not returns an error
    """
    option_selected = int(input("""
            
                \n
Select options:
     Type 1 and enter to add other ingredient
     Type 2 and enter to get the recipe   
        
                """))
     
    if option_selected == 1:
        return 1
    elif option_selected == 2:
        return 2
    else:
         return ValueError



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

