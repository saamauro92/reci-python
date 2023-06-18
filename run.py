from time import sleep

class recipeClass:
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





def main():
    display_program_welcome()

    new_recipe = recipeClass("fake recipe", "fake instructions...")
    print(new_recipe.print_data())


main()




