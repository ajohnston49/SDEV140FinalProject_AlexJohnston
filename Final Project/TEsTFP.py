"""
Program Name: Test.py.FinalProdjectLogic
Author: Alex Johnston
4/26/24
/// Program allows user to enter a number of strings(ingrediants) and tests to see if the users
inputs complete any of the defined lists. If the inputs find a match, the repice name is displayed.
This was a testing application to try and build off of for my "Pantry" breezypythongui application
"""

# Predefined lists of valid strings(or Recipes)
grilledCheese = ["cheese","butter","bread"]
cheeseburger = ["cheese","hamburger","ketchup","mustard","bread","pickle"]
spaghettiAndMeatballs = ["spaghetti","tomatosauce","meatballs"]
# Initializes an empty list to store user inputs
user_inputs = []

# Prompts the user to enter a predifined number of ingrediants
for i in range(10):#predifines number of ingrediants user is allowed to input ***Can be adjusted as needed***
    user_input = input(f"Enter Ingrediant {i + 1}: ")
    if user_input == "":#Allows user to hit enter anytime to test inputs if they dont need all 10 ingrediants
        break
    user_inputs.append(user_input.lower())  # Convert input to lowercase for case-insensitive comparison
print("")
print("")
# Check if user inputs match the predefined recipes
matching_GCrecipe = [s for s in user_inputs if s in grilledCheese ]

if len(matching_GCrecipe) == 3:
    print("Grilled Cheese")
    print("")
matching_CBrecipe = [s for s in user_inputs if s in cheeseburger ]

if len(matching_CBrecipe) == 6:
    print("CheeseBurger")
    print("")

matching_SPrecipe = [s for s in user_inputs if s in spaghettiAndMeatballs ]

if len(matching_SPrecipe) == 3:
    print("Spaghetti And Meatballs")
    print("")


