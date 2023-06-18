
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
    Prints 'welcome to the reci-python program'
    """
    print(
        """
              WELCOME TO

 █▀▄ ██▀ ▄▀▀ █    █▀▄ ▀▄▀ ▀█▀ █▄█ ▄▀▄ █▄ █
 █▀▄ █▄▄ ▀▄▄ █ ▀▀ █▀   █   █  █ █ ▀▄▀ █ ▀█

             (RECI-PYTHON)

    """)


def main():
    display_program_welcome()

    new_recipe = recipeClass("fake recipe", "fake instructions...")
    print(new_recipe.print_data())


main()
