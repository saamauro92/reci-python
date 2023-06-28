
# Reci-Python
  ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)   ![NodeJS](https://img.shields.io/badge/node.js-6DA55F?style=for-the-badge&logo=node.js&logoColor=white) ![Heroku](https://img.shields.io/badge/heroku-%23430098.svg?style=for-the-badge&logo=heroku&logoColor=white) ![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)
  
  
  
**Reci-Python** is a command line program developed in Python that allows users to conveniently search for recipes based on their names or ingredients. The program provides a simple and efficient way to explore a wide variety of recipes and discover new culinary ideas.

Live version  [Here](https://reci-python-6494e488519a.herokuapp.com/)

  
  

![Main](https://github.com/saamauro92/reci-python/raw/main/assets/images/main.png)

  # Table of contents


- [Features](#features)

   - [Main menu](#main-menu)
   - [Secondary menu](#secondary-menu)
   - [Recipe List](#recipe-list)
   - [Recipe](#recipe)

 - [Flowchart](#flowchart)

- [Testing](#testing)
   - [Validator Testing](#validator-testing)
   - [Manual testing](#manual-testing)
   
- [Known Bugs](#known-bugs)

- [Deployment ](#deployment)

- [Technologies Used](#technologies-used)

- [Credits](#credits)
  - [Content](#content)

- [Acknowledgements](#acknowledgments)


---

## Features

 
#####  Main Menu
  

- This section will allow the user to select the way to get a recipe or to exit the program.

 ![main_menu](https://github.com/saamauro92/reci-python/raw/main/assets/images/main_menu.png)

##### Secondary Menu 

  
- When in main menu option 2 was selected an ingredient will be added and then the secondary menu would be displayed and to allow the user to select another ingredient, get the recipe or to start again.
  

![secondary_menu](https://github.com/saamauro92/reci-python/raw/main/assets/images/secondary_menu.png)

  


##### Recipe List 

  
- This section displays the list of recipe/s prepared and the user could choose between them or go back to the main menu
  
![recipes_list](https://github.com/saamauro92/reci-python/raw/main/assets/images/recipes_list.png)
  

##### Recipe

 
- This section displays the recipe with title, description and instructions. 
  

![recipe](https://github.com/saamauro92/reci-python/raw/main/assets/images/display_recipe.png)




## **Flowchart**

![flowchart](https://github.com/saamauro92/reci-python/raw/main/assets/images/Flowchart.png)


  


## Testing

  

### Validator Testing

Using PEP8CI Python validator only found 3 no relevant warnings

![validator](https://github.com/saamauro92/reci-python/raw/main/assets/images/validator.png)
  

### Manual testing
 ![tests](https://badgen.net/badge/all/pass/green)

All inputs in this program are validated, and would display an error message if there was a format issue. In menus, there is always an option to go back and even to exit the program.

  
| Feature | Expect | Action | Result |
|--|--|--|--|
| Main menu| When select CORRECT option will proceed to the action | selected 1, 2, 0  in different tries  | action perfectly executed |
| Main menu| When select an INCORRECT option or text format will proceed display a message validator | typed 4, and in other try "cheese" | a validation message was displayed|
| Add Recipe by name input| When type and enter any string will start preparing the recipe | typed a string  | action perfectly executed |
| Add Recipe by name input| When type and enter any string mixed with numbers or just numbers will display an validator message | typed a string mixed with a number and then a number  | validator message displayed 
| Add Recipe by ingredient input| When type and enter any string will display the secondary menu | typed a string  | secondary menu displayed |
| Add Recipe by ingredient input| When type and enter any string mixed with number or just numbers will display a validator message| typed a string mixed with number | validator message displayed |
| Secondary menu| When select CORRECT option will proceed to the action | selected 1, 2, 3  in different tries  | action perfectly executed |
| Secondary menu| When select an INCORRECT option or text format will proceed display a message validator | typed 4, and in other try "chicken" | a validation message was displayed|
| Recipes list menu| When select CORRECT option will proceed to the display the recipe | selected 1, 2, 3, 4 ,5 in different tries  | action displays the recipe |
| Recipes list menu| When select an INCORRECT option or text format will proceed display a message validator | typed 8, and in other try "ham" | a validation message was displayed|
| Recipes list menu| When select option 0 will go back to main menu | typed 0 and enter | main menu was displayed|
| Main menu| When select option 0 will exit program | typed 0 and enter| Program was shut off|

Also the program was tested using the NodeJS template in a local environment before uploading to Heroku.

  

### Known Bugs

   
 -  In add "recipe by name" and "recipe by ingredient" inputs any type of string is valid like "chicken" or also "akjdalskdj", this would let  you continue, but it would just return a wrong recipe message at a later stage like the following image.
 
![known-bug](https://github.com/saamauro92/reci-python/raw/main/assets/images/known-bug.png)
 

## Deployment

The Program was deployed in Heroku.
 
1.  Log in to your Heroku account and access the dashboard.
2.  Look for the "New" button and click on it to create a new app.
3.  Provide a unique name for your app, select the region that is  closest to you, and click "Create app."
4.  In the app's settings, locate the "Reveal Config Vars" button and click on it.
5. Create a configuration variable "API_URL" and the value "https://tasty.p.rapidapi.com/recipes/list"
6.  Get your API key and create a configuration variable "API_KEY" and complete the value with your key.
7.  Create another configuration variable "PORT" and the value to "8000," and click "Add."
8.  To specify the dependencies for your app, go to the "Add Buildpack" section.
9.  Select "Python" as the first dependency and "Node.js" as the second. The order of the dependencies is crucial.
10.  Navigate to the "Deploy" tab and choose "GitHub" as the deployment method.
11.  Connect your Heroku account to your GitHub account and select the repository you want to deploy.
12.  Enable the "Automatic Deploy" option if you want Heroku to rebuild your project automatically every time you push a new commit.

## Technologies Used
  ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)   ![NodeJS](https://img.shields.io/badge/node.js-6DA55F?style=for-the-badge&logo=node.js&logoColor=white) ![Heroku](https://img.shields.io/badge/heroku-%23430098.svg?style=for-the-badge&logo=heroku&logoColor=white) ![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)
  
  - I developed the program using Python, the template uses HTML, CSS and Javascript
  

  - [RapidAPI - Tasty](https://rapidapi.com/apidojo/api/tasty/) - Tasty API from RapidApi was used to get recipes 
 -  [GitHub](https://github.com/join/welcome) and [Git](https://git-scm.com/) were used to document the development process
   -  [Heroku](https://www.heroku.com/) was used for deployment.
  - [PEP8CI](https://pep8ci.herokuapp.com/) used to validate Python code.
  -  [StackEdit](https://stackedit.io/) to write README
  - [Lucidchart](https://lucid.app/) was used to made the flowchart.
  - [VSC IDE](https://code.visualstudio.com/) 
  - [ASCII Art Generator](https://fsymbols.com/generators/carty/) - to create logo and art messages
  - [Badgnen](https://badgen.net/) - for readme badges



  

## Credits

### Content

- Code institute student programme
- Command Line Interface Guidelines [clig.dev](https://clig.dev/)
- Code snippet for request API [RapidApi](https://rapidapi.com/apidojo/api/tasty/)
- Exception handling for python requests  [StackOverflow](https://stackoverflow.com/questions/9054820/python-requests-exception-handling)
- Exception handling for python requests [geeksforgeeks](https://www.geeksforgeeks.org/exception-handling-of-python-requests-module/)
- Working with credentials and configs in Python [tutorial](https://janakiev.com/blog/python-credentials-and-configuration/)
- Best way to navigate a nested JSON in Python [Stackoverflow](https://stackoverflow.com/questions/70782902/best-way-to-navigate-a-nested-json-in-python)
-   How to check if a variable is a string [tutorial](https://pythonprinciples.com/blog/check-if-var-is-string/)
- Check if a string contains only letters  [tutorial](https://bobbyhadz.com/blog/python-check-if-string-contains-only-letters)
- Using textwrap module [docs.python](https://docs.python.org/3/library/textwrap.html)
- To get invalid emoji [Stackoverflow](https://stackoverflow.com/questions/30470079/emoji-value-range)
- Progress bar module [Github - tqdm](https://github.com/tqdm/tqdm)
- How to print simulate typing [Stackoverflow](https://stackoverflow.com/questions/4099422/printing-slowly-simulate-typing)




  

### Acknowledgments

- The code institute
- Alan Bushell my cohort facilitator for support and advice.
- Graeme Taylor my mentor for support and advice.
