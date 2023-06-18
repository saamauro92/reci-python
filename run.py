from time import sleep

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
            sleep(2)

def ingredient_inputs():
    """
    Gets the ingredients and returns a list of them
    """

    ingredients = []
    try:
        ingredient_1 = input('\n Type and enter your first ingredient\n')
        ingredients.append(ingredient_1)

    except:
        print("error")
    
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

