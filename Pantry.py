"""

------------------------------------------------------------------------------------------------------------------------------------



Program: Pantry

Author:Alex Johnston

Version 1.4

5/11/2024


------------------------------------------------------------------------------------------------------------------------------------

                                                    Program Purpose:

The purpose of this program is to allow the user to select ingrediants they redily have available to them and finds recipes using
only the ingrediants the user has. This saves the user signifigant time trying to sort through the hundreds and thousands of online
recipes that oftentimes require imgrediants the user may not have available. The Pantry app is the newest partner for anybody who
mayhave limitations in their kitchen and need to cook something with the minimum amount of ingrediants. New ingrediants are extremly
easyto add to the program and create test data, templates have been made for programmer convienence. If a programmer is looking to
adda signifigant amount of recipes, a second  recipe list panel may need to be created and the buttons for the recipe steps that will
need to be placed onto that panel.

------------------------------------------------------------------------------------------------------------------------------------


"""

#______________________________________________________________________________________________________________________________________

                                                        #Imports- Page 1

from breezypythongui import EasyFrame,EasyCanvas
import tkinter
from tkinter.font import Font
from tkinter import PhotoImage


#____________________________________________________________________________________________________________________________________

                                         # Emtpy list for user choices - Page 2
 

Ingrediants = []


#___________________________________________________________________________________________________________________________________

                                                  # Predefined recipes - Page 3


                                             

grilledCheese = ["Cheese","Butter","Bread"]
cheeseburger = ["Cheese","Hamburger","Bread",]
spaghettiAndMeatballs = ["Spaghetti Noodles","Tomato Sauce","Hamburger"]
FriedEgg = ["Eggs","Oil"]
ScrambledEgg=["Eggs","Milk"]
CheeseOmlet=["Eggs","Milk","Cheese"]





            # ANY NEW RECIPES WITH INGREDIANTS NOT LISTED MUST HAVE A CHECK BUTTON CREATED FOR USER INPUT
          # ALONG WITH A NEW 'COOKNOW' BUTTON ON THE SECOND WINDOW AND A CALL EVENT FOR THE STEPS ON A THIRD WINDOW

#__________________________________________________________________________________________________________________________________


                                                       #Main Application - Page 4
          

class MyWindow(EasyFrame): #Creates Main Window
    def __init__(self):

        EasyFrame.__init__(self,title="Pantry",background="Grey")

        MainPanel = self.addPanel(row=0, column=0,rowspan=14, columnspan=10, background="Grey") #Creates A panel to add wigits 

        self.myFirstLabel = self.addLabel(text="Pantry", row=0, column=0) #First Custom Label for title

        #Sets font style of Label
        
        font = Font(family="Verdana", size=20, slant="italic") 
        self.myFirstLabel["font"] = font
        self.myFirstLabel["foreground"] = "Purple"
        self.myFirstLabel["background"] = "Grey"  

        self.addLabel(text="Created By: Alex Johnston", row=1, column=0,background="Grey")
        self.addLabel(text="Pantry App: Version 1.0", row=2, column=0, background="Grey")
        self.addLabel(text="Start By Selecting Ingrediants", row=3, column=0, background="Grey", foreground="Purple")
        self.addLabel(text="That You Have Available.", row=4, column=0, background="Grey", foreground="Purple")
        self.addLabel(text="Click 'GET RECIPES' To Find Recipes", row=5, column=0, background="Grey", foreground="Purple")
        self.addLabel(text="With Your Chosen Ingrediants.", row=6, column=0, background="Grey", foreground="Purple")
    
    # Creates a column of check buttons that add user selected 'ingrediants' to a list

        self.checkbutton = self.addCheckbutton(text="Cheese", row=1, column=3,command = self.add_cheese)
        self.checkbutton["background"] = "Grey"
        self.checkbutton = self.addCheckbutton(text="Bread", row=2, column=3,command = self.add_bread)
        self.checkbutton["background"] = "Grey"
        self.checkbutton = self.addCheckbutton(text="Butter", row=3, column=3,command = self.add_butter)
        self.checkbutton["background"] = "Grey"
        self.checkbutton = self.addCheckbutton(text="Hamburger", row=4, column=3,command = self.add_HB)
        self.checkbutton["background"] = "Grey"
        self.checkbutton = self.addCheckbutton(text="Milk", row=5, column=3,command = self.add_milk)
        self.checkbutton["background"] = "Grey"
        self.checkbutton = self.addCheckbutton(text="Oil", row=1, column=4,command = self.add_oil)
        self.checkbutton["background"] = "Grey"
        self.checkbutton = self.addCheckbutton(text="Ketchup", row=2, column=4,command = self.add_ketchup)
        self.checkbutton["background"] = "Grey"
        self.checkbutton = self.addCheckbutton(text="Mustard", row=3, column=4,command = self.add_Mustard)
        self.checkbutton["background"] = "Grey"
        self.checkbutton = self.addCheckbutton(text="Pickles", row=4, column=4,command = self.add_Pickle) 
        self.checkbutton["background"] = "Grey"     
        self.checkbutton = self.addCheckbutton(text="Spaghetti Noodles", row=5, column=4,command = self.add_SN)
        self.checkbutton["background"] = "Grey"
        self.checkbutton = self.addCheckbutton(text="Tomato Sauce", row=6, column=3,command = self.add_TS)
        self.checkbutton["background"] = "Grey"
        self.checkbutton = self.addCheckbutton(text="Eggs", row=6, column=4,command = self.add_eggs)
        self.checkbutton["background"] = "Grey"
       
        self.addButton(text="Get Recipes", row=14, column=0, command = self.recipes_type_Page)
        self.addButton(text="All Recipes", row=14, column=2, command = self.Recipes_on)


#_________________________________________________________________________________________________________________________________
        
                                                #Creates a Mock Main Panel to call on - Page 5
        
    def SecondaryMainPanel(self):

        MainPanel = self.addPanel(row=0, column=0,rowspan=15, columnspan=10, background="Grey")

        self.myFirstLabel = self.addLabel(text="Pantry", row=0, column=0)

        font = Font(family="Verdana", size=20, slant="italic")
        self.myFirstLabel["font"] = font
        self.myFirstLabel["foreground"] = "Purple"
        self.myFirstLabel["background"] = "Grey"  

        self.addLabel(text="Created By: Alex Johnston", row=1, column=0,background="Grey")
        self.addLabel(text="Pantry App: Version 1.0", row=2, column=0, background="Grey")
        self.addLabel(text="Start By Selecting Ingrediants", row=3, column=0, background="Grey", foreground="Purple")
        self.addLabel(text="That You Have Available.", row=4, column=0, background="Grey", foreground="Purple")
        self.addLabel(text="Click 'GET RECIPES' To Find Recipes", row=5, column=0, background="Grey", foreground="Purple")
        self.addLabel(text="With Your Chosen Ingrediants.", row=6, column=0, background="Grey", foreground="Purple")

        self.checkbutton = self.addCheckbutton(text="Cheese", row=1, column=3,command = self.add_cheese)
        self.checkbutton["background"] = "Grey"
        self.checkbutton = self.addCheckbutton(text="Bread", row=2, column=3,command = self.add_bread)
        self.checkbutton["background"] = "Grey"
        self.checkbutton = self.addCheckbutton(text="Butter", row=3, column=3,command = self.add_butter)
        self.checkbutton["background"] = "Grey"
        self.checkbutton = self.addCheckbutton(text="Hamburger", row=4, column=3,command = self.add_HB)
        self.checkbutton["background"] = "Grey"
        self.checkbutton = self.addCheckbutton(text="Milk", row=5, column=3,command = self.add_milk)
        self.checkbutton["background"] = "Grey"
        self.checkbutton = self.addCheckbutton(text="Oil", row=1, column=4,command = self.add_oil)
        self.checkbutton["background"] = "Grey"
        self.checkbutton = self.addCheckbutton(text="Ketchup", row=2, column=4,command = self.add_ketchup)
        self.checkbutton["background"] = "Grey"
        self.checkbutton = self.addCheckbutton(text="Mustard", row=3, column=4,command = self.add_Mustard)
        self.checkbutton["background"] = "Grey"
        self.checkbutton = self.addCheckbutton(text="Pickles", row=4, column=4,command = self.add_Pickle) 
        self.checkbutton["background"] = "Grey"     
        self.checkbutton = self.addCheckbutton(text="Spaghetti Noodles", row=5, column=4,command = self.add_SN)
        self.checkbutton["background"] = "Grey"
        self.checkbutton = self.addCheckbutton(text="Tomato Sauce", row=6, column=3,command = self.add_TS)
        self.checkbutton["background"] = "Grey"
        self.checkbutton = self.addCheckbutton(text="Eggs", row=6, column=4,command = self.add_eggs)
        self.checkbutton["background"] = "Grey"      

        self.addButton(text="Get Recipes", row=14, column=0, command = self.recipes_type_Page)

        self.addButton(text="All Recipes", row=14, column=2, command = self.Recipes_on)

#________________________________________________________________________________________________________________________________        

                                                    

                                       #Adds user choices to the empty list 'Ingrediants' - Page 6
        

    def add_cheese(self):
        Ingrediants.append("Cheese")
    def add_bread(self):
        Ingrediants.append("Bread")
    def add_butter(self):
        Ingrediants.append("Butter")
    def add_HB(self):
        Ingrediants.append("Hamburger")
    def add_milk(self):
        Ingrediants.append("Milk")
    def add_oil(self):
        Ingrediants.append("Oil")
    def add_ketchup(self):
        Ingrediants.append("Ketchup")
    def add_Mustard(self):
        Ingrediants.append("Mustard")
    def add_Pickle(self):
        Ingrediants.append("Pickles")
    def add_SN(self):
        Ingrediants.append("Spaghetti Noodles")
    def add_TS(self):
        Ingrediants.append("Tomato Sauce")
    def add_eggs(self):
        Ingrediants.append("Eggs")


#___________________________________________________________________________________________________________________________________
        

                    #Creates a recipes page that is called when hitting the 'get recipes' button on the parent window - Page 7

        

    def recipes_type_Page(self):
        
        RecipesTypePage = self.addPanel(row=0, column=0,rowspan=18, columnspan=10, background="Grey")

        #Adds a title
        self.myFirstLabel= self.addLabel(text="All Recipes Available To Cook Now", row=0, column=0)
        
        font = Font(family="Verdana", size=20, slant="italic")
        self.myFirstLabel["font"] = font
        self.myFirstLabel["foreground"] = "Purple"
        self.myFirstLabel["background"] = "Grey"
        
        #back Button
        
        self.addButton(text = "Main Menu" , row=0, column=4, command=self.execute_multiple_commands)

        self.addButton(text = "Breakfast" , row=2, column=4, command=self.recipes_Page1)
        self.addButton(text = "Lunch/Dinner" , row=3, column=4, command=self.recipes_Page2) #More buttons can be added for extra panels

    #creates a panel that displays Recipes the user is available to cook with their chosen ingrediants
    #This method allows the programmer to add more catagories of food to include much more recipes

    def recipes_Page1(self):
        
        RecipesPage = self.addPanel(row=0, column=0,rowspan=18, columnspan=10, background="Grey")
        self.myFirstLabel= self.addLabel(text="Breakfast Recipes ", row=0, column=0)
        
        font = Font(family="Verdana", size=20, slant="italic")
        self.myFirstLabel["font"] = font
        self.myFirstLabel["foreground"] = "Purple"
        self.myFirstLabel["background"] = "Grey"
        self.addButton(text = "Main Menu" , row=0, column=4, command=self.execute_multiple_commands)
        self.addButton(text= "Back" , row = 0, column = 3, command=self.recipes_type_Page)
#_______________________________________________________________________________________________________________________________



                                                    #Test Data - Page 9

        

        
                # Tests the number of matching user inputs to the predefined recipes and if the number
                # Of matches equals to the number of ingrediants within the list, it displays a button  
                                # That if clicked will display the steps To cook the recipe
                            
                    #In order to Add more recipes, more tests need to be added for each recipe.
               

        matching_FErecipe = [s for s in Ingrediants if s in FriedEgg ]

        if len(matching_FErecipe) >= 2:
            self.addButton(text = "Cook Now" , row=2, column=3, command= self.FE_Recipe)
            self.addLabel(text="Fried Egg", row = 2, column= 2,background="Grey")

        matching_SErecipe = [s for s in Ingrediants if s in ScrambledEgg ]

        if len(matching_SErecipe) >= 2:
            self.addButton(text = "Cook Now" , row=3, column=3, command= self.SE_Recipe)
            self.addLabel(text="Scrambled Egg", row = 3, column= 2,background="Grey")

        matching_OMrecipe = [s for s in Ingrediants if s in CheeseOmlet ]

        if len(matching_OMrecipe) >= 3:
            self.addButton(text = "Cook Now" , row=4, column=3, command= self.OM_Recipe)
            self.addLabel(text="Cheese Omlet", row = 4, column= 2,background="Grey")

    #Creates a second panel for another catagory for programmer to add more recipes
            
    def recipes_Page2(self):
        
        RecipesPage = self.addPanel(row=0, column=0,rowspan=18, columnspan=10, background="Grey")
        self.myFirstLabel= self.addLabel(text="Lunch / Dinner", row=0, column=0)
        
        font = Font(family="Verdana", size=20, slant="italic")
        self.myFirstLabel["font"] = font
        self.myFirstLabel["foreground"] = "Purple"
        self.myFirstLabel["background"] = "Grey"
        self.addButton(text = "Main Menu" , row=0, column=4, command=self.execute_multiple_commands)
        self.addButton(text= "Back" , row = 0, column = 3, command=self.recipes_type_Page)

        matching_GCrecipe = [s for s in Ingrediants if s in grilledCheese ]

        if len(matching_GCrecipe) >= 3:
            self.addButton(text = "Cook Now" , row=1, column=3, command= self.GC_Recipe)
            self.addLabel(text="Grilled Cheese", row = 1, column= 2,background="Grey")
            
        matching_CBrecipe = [s for s in Ingrediants if s in cheeseburger ]

        if len(matching_CBrecipe) >= 3:
            self.addButton(text = "Cook Now" , row=2, column=3, command= self.CB_Recipe)
            self.addLabel(text="CheeseBurger", row = 2, column= 2,background="Grey")
            
        matching_SMrecipe = [s for s in Ingrediants if s in spaghettiAndMeatballs ]

        if len(matching_SMrecipe) >= 3:
            self.addButton(text = "Cook Now" , row=3, column=3, command= self.SM_Recipe)
            self.addLabel(text="Spaghetti & Meatballs", row = 3, column= 2,background="Grey")
            
       #       You would place more test data here.....................


#                                        Example

#       matching_GCrecipe = [s for s in Ingrediants if s in grilledCheese ]

#       if len(matching_GCrecipe) >= 3:
#           self.addButton(text = "Cook Now" , row=1, column=3, command= self.GC_Recipe)
#           self.addLabel(text="Grilled Cheese", row = 1, column= 2,background="Grey")


            
#____________________________________________________________________________________________________________________________________

        
                                                        #All Recipes Pages - Page 10




        #I went ahead and added a secondary list of infrediants to make it easier for a programmer to add more ingrediants based
              #off of type of meal. Reading into this logic should help explain how to create a third panel if need be
        


#                               Creates a panel that lists the catagories of "all recipes"


    
    def Recipes_on(self):

        RecipesOn = self.addPanel(row=0, column=0,rowspan=18, columnspan=10, background="Grey")

        #Adds a title

        self.addLabel(text="Recipe Catagories", row = 0, column= 1,background="Grey",foreground="Purple")
        
        #back Button
        
        self.addButton(text = "Back" , row=0, column=4, command=self.execute_multiple_commands)

        self.addButton(text = "Breakfast" , row=2, column=1, command=self.RecipeList1)
        
        self.addButton(text = "Lunch / Dinner" , row=3, column=1, command=self.RecipeList2)
        
        
#____________________________________________________________________________________________________________________________________



#                       Creates a panel that displays the first catagory of recipes within "all recipes" - Page 11



    def RecipeList1(self):

        RecipesList1 = self.addPanel(row=0, column=0,rowspan=18, columnspan=10, background="Grey")

        #Adds a title

        self.addLabel(text="Breakfast Recipes", row = 0, column= 1,background="Grey",foreground="Purple")
        
        #back Button
        
        self.addButton(text = "Back" , row=0, column=4, command=self.Recipes_on)

        #Recipe buttons---Can popy and paste most of this code and edit parameters

        self.addButton(text = "Cook Now" , row=1, column=3, command= self.FE_Recipe2)
        self.addLabel(text="Fried Egg", row = 1, column= 2,background="Grey")

        self.addButton(text = "Cook Now" , row=2, column=3, command= self.SE_Recipe2)
        self.addLabel(text="Scrambled Eggs", row = 2, column= 2,background="Grey")

        self.addButton(text = "Cook Now" , row=3, column=3, command= self.OM_Recipe2)   
        self.addLabel(text="Cheese Omlet", row = 3, column= 2,background="Grey")
        

#____________________________________________________________________________________________________________________________________
       



#                       Creates a second panel that displays another catagory of recipes within "all recipes" - Page 12



        
    def RecipeList2(self):

        RecipesList2 = self.addPanel(row=0, column=0,rowspan=18, columnspan=10, background="Grey")

        #Adds a title

        self.addLabel(text="Lunch/Dinner", row = 0, column= 1,background="Grey",foreground="Purple")
        
        #back Button
        
        self.addButton(text = "Back" , row=0, column=4, command=self.Recipes_on)

        #Recipe buttons---Can popy and paste most of this code and edit parameters
        
        self.addButton(text = "Cook Now" , row=1, column=3, command= self.GC_Recipe2)
        self.addLabel(text="Grilled Cheese", row = 1, column= 2,background="Grey")

        self.addButton(text = "Cook Now" , row=2, column=3, command= self.CB_Recipe2)
        self.addLabel(text="CheeseBurger", row = 2, column= 2,background="Grey")

        self.addButton(text = "Cook Now" , row=3, column=3, command= self.SM_Recipe2)
        self.addLabel(text="Spaghetti & Meatballs", row = 3, column= 2,background="Grey")



                
        
#___________________________________________________________________________________________________________________________________
        

                            # Steps for making a grilled cheese if user enters his own ingrediants - Page 13
                            

    def GC_Recipe(self):

        GCRecipe = self.addPanel(row=0, column=0,rowspan=18, columnspan=10, background="Grey")

        self.addLabel(text="Start by buttering one side of two pieces of bread", row=1, column=0,background="Grey")
        self.addLabel(text="Next, With the butter side facing out, put a slice of cheese between your bread", row=2, column=0,background="Grey")
        self.addLabel(text="Then fry it on a hot skillet flipping it about every 3 minutes or ", row=3, column=0,background="Grey")
        self.addLabel(text="Until Desired color and texture is achieved.", row=4, column=0,background="Grey")
        self.addLabel(text=" ", row=5, column=0,background="Grey")
        self.addLabel(text="Enjoy by itself or with your favorite soup!", row=6, column=0,background="Grey")

        #Directional Buttons
        
        self.addButton(text= "Go Back To Choices", row = 0,column = 3, command = self.recipes_type_Page )
        self.addButton(text = "Main Menu" , row=0, column=4, command=self.execute_multiple_commands)
        
#Steps for making a grilled cheese if user clicks "All Recipes"

#The reason for being two pages is to allow the user to go back to his "options based off his chosen ingrediants" when in
#the Recipes Page

#The second option allows user to go back and see "All recipes". The button has a different direction based on where the user
#is in the application        
    
    def GC_Recipe2(self):

        GCRecipe = self.addPanel(row=0, column=0,rowspan=18, columnspan=10, background="Grey")

        self.addLabel(text="Start by buttering one side of two pieces of bread", row=1, column=0,background="Grey")
        self.addLabel(text="Next, With the butter side facing out, put a slice of cheese between your bread", row=2, column=0,background="Grey")
        self.addLabel(text="Then fry it on a hot skillet flipping it about every 3 minutes or ", row=3, column=0,background="Grey")
        self.addLabel(text="Until Desired color and texture is achieved.", row=4, column=0,background="Grey")
        self.addLabel(text=" ", row=5, column=0,background="Grey")
        self.addLabel(text="Enjoy by itself or with your favorite soup!", row=6, column=0,background="Grey")

        self.addButton(text= "Go Back To Choices", row = 0,column = 3, command = self.Recipes_on )
        self.addButton(text = "Main Menu" , row=0, column=4, command=self.execute_multiple_commands)
        

#_____________________________________________________________________________________________________________________________________


                                            # Steps for making a cheeseburger - Page 14

                                            

#        Tested Recipe "Get Recipe"

    def CB_Recipe(self):

        CBRecipe  = self.addPanel(row=0, column=0,rowspan=18, columnspan=10, background="Grey")

        self.addLabel(text="Start by forming the raw Hamburger into a patty like shape.", row=1, column=0,background="Grey")
        self.addLabel(text="Next, get a pan hot on medium/hot setting(varying, depends on your appliance)", row=2, column=0,background="Grey")
        self.addLabel(text="Then fry the patty, flipping every 3 minutes or so until desired color and texture is acheived. ", row=3, column=0,background="Grey")
        self.addLabel(text="NOTE: Raw meat can contain bacteria harmful to your health.", row=4, column=0,background="Grey")
        self.addLabel(text=" Once the patty is cooked, turn off the heat, flip your patty so the hottest side is facing up, ", row=5, column=0,background="Grey")
        self.addLabel(text=" And lay your cheese on top the patty and cover the pan for 5 minutes.", row=6, column=0,background="Grey")
        self.addLabel(text="While the cheese melts, get your bread ready and gather all your toppings to make your cheeseburger! ", row=7, column=0,background="Grey")
        self.addLabel(text=" ", row=8, column=0,background="Grey")
        self.addLabel(text="Enjoy by itself or with your favorite sides!", row=9, column=0,background="Grey")

        self.addButton(text= "Go Back To Choices", row = 0,column = 3, command = self.recipes_type_Page)
        self.addButton(text = "Main Menu" , row=0, column=4, command=self.execute_multiple_commands)

#       Non-Tested Recipe "All Recipes"

    def CB_Recipe2(self):

        CBRecipe  = self.addPanel(row=0, column=0,rowspan=18, columnspan=10, background="Grey")

        self.addLabel(text="Start by forming the raw Hamburger into a patty like shape.", row=1, column=0,background="Grey")
        self.addLabel(text="Next, get a pan hot on medium/hot setting(varying, depends on your appliance)", row=2, column=0,background="Grey")
        self.addLabel(text="Then fry the patty, flipping every 3 minutes or so until desired color and texture is acheived. ", row=3, column=0,background="Grey")
        self.addLabel(text="NOTE: Raw meat can contain bacteria harmful to your health.", row=4, column=0,background="Grey")
        self.addLabel(text=" Once the patty is cooked, turn off the heat, flip your patty so the hottest side is facing up, ", row=5, column=0,background="Grey")
        self.addLabel(text=" And lay your cheese on top the patty and cover the pan for 5 minutes.", row=6, column=0,background="Grey")
        self.addLabel(text="While the cheese melts, get your bread ready and gather all your toppings to make your cheeseburger! ", row=7, column=0,background="Grey")
        self.addLabel(text=" ", row=8, column=0,background="Grey")
        self.addLabel(text="Enjoy by itself or with your favorite sides!", row=9, column=0,background="Grey")

        self.addButton(text= "Go Back To Choices", row = 0,column = 3, command = self.Recipes_on)
        self.addButton(text = "Main Menu" , row=0, column=4, command=self.execute_multiple_commands)


#_____________________________________________________________________________________________________________________________________        


                                              #Steps for making Spaghetti and Meatballs - Page 15

        
#        Tested Recipe "Get Recipe"

    def SM_Recipe(self):

        SMRecipe = self.addPanel(row=0, column=0,rowspan=18, columnspan=10, background="Grey")

        self.addLabel(text="Start by getting a deep pan of water boiling, and then add your noodles.", row=1, column=0,background="Grey")
        self.addLabel(text="Next, roll your hamburger into inch size balls, place them on a flat pan and bake them at 375 for 20 minutes.", row=2, column=0,background="Grey")
        self.addLabel(text="Once the spaghetti is cooked to the desired softness, drain the water and add your suace and throw back on low heat.", row=3, column=0,background="Grey")
        self.addLabel(text="Once the Meatballs are done, drain any grease and add them to your spahetti and cover for another 15 minutes.", row=4, column=0,background="Grey")
        self.addLabel(text=" Your spaghetti is now ready to enjoy to enjoy!", row=5, column=0,background="Grey")
        self.addLabel(text=" ", row=5, column=0,background="Grey")
        self.addLabel(text="Enjoy by itself or with your favorite bread!", row=6, column=0,background="Grey")

        self.addButton(text= "Go Back To Choices", row = 0,column = 3, command = self.recipes_type_Page )
        self.addButton(text = "Main Menu" , row=0, column=4, command=self.execute_multiple_commands)

#       Non-Tested Recipe "All Recipes"

    def SM_Recipe2(self):

        SMRecipe = self.addPanel(row=0, column=0,rowspan=18, columnspan=10, background="Grey")

        self.addLabel(text="Start by getting a deep pan of water boiling, and then add your noodles.", row=1, column=0,background="Grey")
        self.addLabel(text="Next, roll your hamburger into inch size balls, place them on a flat pan and bake them at 375 for 20 minutes.", row=2, column=0,background="Grey")
        self.addLabel(text="Once the spaghetti is cooked to the desired softness, drain the water and add your suace and throw back on low heat.", row=3, column=0,background="Grey")
        self.addLabel(text="Once the Meatballs are done, drain any grease and add them to your spahetti and cover for another 15 minutes.", row=4, column=0,background="Grey")
        self.addLabel(text=" Your spaghetti is now ready to enjoy to enjoy!", row=5, column=0,background="Grey")
        self.addLabel(text=" ", row=5, column=0,background="Grey")
        self.addLabel(text="Enjoy by itself or with your favorite bread!", row=6, column=0,background="Grey")

        self.addButton(text= "Go Back To Choices", row = 0,column = 3, command = self.Recipes_on)

        self.addButton(text = "Main Menu" , row=0, column=4, command=self.execute_multiple_commands)

        

#__________________________________________________________________________________________________________________________________


                                                    #Steps for making Fried Egg - page 16

        
#        Tested Recipe "Get Recipe"

    def FE_Recipe(self):

        FERecipe  = self.addPanel(row=0, column=0,rowspan=18, columnspan=10, background="Grey")

        self.addLabel(text="", row=1, column=0,background="Grey")
        self.addLabel(text="", row=2, column=0,background="Grey")
        self.addLabel(text="", row=3, column=0,background="Grey")
        self.addLabel(text="", row=4, column=0,background="Grey")
        self.addLabel(text="", row=5, column=0,background="Grey")
        self.addLabel(text="", row=6, column=0,background="Grey")
        self.addLabel(text="", row=7, column=0,background="Grey")
        self.addLabel(text="", row=8, column=0,background="Grey")
        self.addLabel(text="", row=9, column=0,background="Grey")

        self.addButton(text= "Go Back To Choices", row = 0,column = 3, command = self.recipes_type_Page)
        self.addButton(text = "Main Menu" , row=0, column=4, command=self.execute_multiple_commands)

#       Non-Tested Recipe "All Recipes"

    def FE_Recipe2(self):

        FERecipe  = self.addPanel(row=0, column=0,rowspan=18, columnspan=10, background="Grey")

        self.addLabel(text="", row=1, column=0,background="Grey")
        self.addLabel(text="", row=2, column=0,background="Grey")
        self.addLabel(text="", row=3, column=0,background="Grey")
        self.addLabel(text="", row=4, column=0,background="Grey")
        self.addLabel(text="", row=5, column=0,background="Grey")
        self.addLabel(text="", row=6, column=0,background="Grey")
        self.addLabel(text="", row=7, column=0,background="Grey")
        self.addLabel(text="", row=8, column=0,background="Grey")
        self.addLabel(text="", row=9, column=0,background="Grey")

        self.addButton(text= "Go Back To Choices", row = 0,column = 3, command = self.Recipes_on)
        self.addButton(text = "Main Menu" , row=0, column=4, command=self.execute_multiple_commands)

        

#_________________________________________________________________________________________________________________________________


                                                #Steps for making Scramble Eggs - Page 17

#        Tested Recipe "Get Recipe"

    def SE_Recipe(self):

        SERecipe  = self.addPanel(row=0, column=0,rowspan=18, columnspan=10, background="Grey")

        self.addLabel(text="", row=1, column=0,background="Grey")
        self.addLabel(text="", row=2, column=0,background="Grey")
        self.addLabel(text="", row=3, column=0,background="Grey")
        self.addLabel(text="", row=4, column=0,background="Grey")
        self.addLabel(text="", row=5, column=0,background="Grey")
        self.addLabel(text="", row=6, column=0,background="Grey")
        self.addLabel(text="", row=7, column=0,background="Grey")
        self.addLabel(text="", row=8, column=0,background="Grey")
        self.addLabel(text="", row=9, column=0,background="Grey")

        self.addButton(text= "Go Back To Choices", row = 0,column = 3, command = self.recipes_type_Page)
        self.addButton(text = "Main Menu" , row=0, column=4, command=self.execute_multiple_commands)

#       Non-Tested Recipe "All Recipes"

    def SE_Recipe2(self):

        SERecipe  = self.addPanel(row=0, column=0,rowspan=18, columnspan=10, background="Grey")

        self.addLabel(text="", row=1, column=0,background="Grey")
        self.addLabel(text="", row=2, column=0,background="Grey")
        self.addLabel(text="", row=3, column=0,background="Grey")
        self.addLabel(text="", row=4, column=0,background="Grey")
        self.addLabel(text="", row=5, column=0,background="Grey")
        self.addLabel(text="", row=6, column=0,background="Grey")
        self.addLabel(text="", row=7, column=0,background="Grey")
        self.addLabel(text="", row=8, column=0,background="Grey")
        self.addLabel(text="", row=9, column=0,background="Grey")

        self.addButton(text= "Go Back To Choices", row = 0,column = 3, command = self.Recipes_on)
        self.addButton(text = "Main Menu" , row=0, column=4, command=self.execute_multiple_commands)

#_________________________________________________________________________________________________________________________________

#                                           Steps for making Cheese Omlet - Page 18                                                         

    def OM_Recipe(self):

        OMRecipe  = self.addPanel(row=0, column=0,rowspan=18, columnspan=10, background="Grey")

        self.addLabel(text="", row=1, column=0,background="Grey")  
        self.addLabel(text="", row=2, column=0,background="Grey")
        self.addLabel(text="", row=3, column=0,background="Grey")
        self.addLabel(text="", row=4, column=0,background="Grey")
        self.addLabel(text="", row=5, column=0,background="Grey")
        self.addLabel(text="", row=6, column=0,background="Grey")
        self.addLabel(text="", row=7, column=0,background="Grey")
        self.addLabel(text="", row=8, column=0,background="Grey")
        self.addLabel(text="", row=9, column=0,background="Grey")

        self.addButton(text= "Go Back To Choices", row = 0,column = 3, command = self.recipes_type_Page)

        self.addButton(text = "Main Menu" , row=0, column=4, command=self.execute_multiple_commands)

    def OM_Recipe2(self):

        OMRecipe  = self.addPanel(row=0, column=0,rowspan=18, columnspan=10, background="Grey")

        self.addLabel(text="", row=1, column=0,background="Grey")
        self.addLabel(text="", row=2, column=0,background="Grey")
        self.addLabel(text="", row=3, column=0,background="Grey")
        self.addLabel(text="", row=4, column=0,background="Grey")
        self.addLabel(text="", row=5, column=0,background="Grey")
        self.addLabel(text="", row=6, column=0,background="Grey")
        self.addLabel(text="", row=7, column=0,background="Grey")
        self.addLabel(text="", row=8, column=0,background="Grey")
        self.addLabel(text="", row=9, column=0,background="Grey")

        self.addButton(text= "Go Back To Choices", row = 0,column = 3, command = self.Recipes_on)
        self.addButton(text = "Main Menu" , row=0, column=4, command=self.execute_multiple_commands)
#_________________________________________________________________________________________________________________________________




#                                           Empty Page for Extra Recipe Steps -  Page 19




#_________________________________________________________________________________________________________________________________




#                                           Empty Page for Extra Recipe Steps -  Page 20



#_________________________________________________________________________________________________________________________________



#                                           Empty Page for Extra Recipe Steps -  Page 21


#_________________________________________________________________________________________________________________________________



#                                           Empty Page for Extra Recipe Steps -  Page 22


#_________________________________________________________________________________________________________________________________

        
                                                 #Resets the program - Page 23

            
            
    def execute_multiple_commands(self):
        
        self.command1()

        self.command2()

        self.command3()

    def command1(self):

        self.destroy()

    def command2(self):

        MyWindow()

    def command3(self):

        Ingrediants.clear()

#___________________________________________________________________________________________________________________________________

                                                        #Calls Main Window - Page 24

        
if __name__ == "__main__":
    window = MyWindow()
    window.mainloop()

#___________________________________________________________________________________________________________________________________


#                                       Prints user chosen ingrediants within IDE for testing - Page 25


print(Ingrediants)



#______________________________________________________________________________________________________________________________


#                                     EASY TO USE TEMPLATES FOR CREATING NEW RECIPES



#                                                   NOTE TO PROGRAMMER:

#                               There are 4 steps to add another Recipe to the application

#                           1) Must define a list of what ingrediants go in the recipe (Page 3)

#                           2) Create the steps for the recipe using the template and paste and edit it within Pages 19-22

#                           3) Create a pathway to your recipe in the "all recipes" Page
#                               (Paste and edit templates in pages 11 or 12 for "all recipes")

#                       ***At this point programmer should be able to hit run, click on "all recipes", click on the chosen
#                           Catagory, and the new recipe and button should be there. Otherwise, an error was made.

#                           4) Next, create test data for the Recipe on page 9, using the templates provided
#                                   
#                       *** And thats it, the end user should be able to now test to see if they have the required ingrediants
#                           To make the newly added recipe, or they can simply look thru the "all recipes" page and its there
#________________________________________________________________________________________________________________________________


#                                Templates to add recipes to the "all recipes" panels
"""

        self.addButton(text = "Cook Now" , row=1, column=3, command= self.EX_Recipe2)   
        self.addLabel(text="Example Recipe name", row = 1, column= 2,background="Grey")

        """
#                                                   NOTE:

#                                       make sure to use the proper recipe pathway
#                           Remember, we created 2 due to differences in the pages we call back
#________________________________________________________________________________________________________________________________



                       #Template for adding the recipe instruction pages that the button calls on



"""

def Example_Recipe(self):

        EXRecipe  = self.addPanel(row=0, column=0,rowspan=18, columnspan=10, background="Grey")

        self.addLabel(text="", row=1, column=0,background="Grey")  
        self.addLabel(text="", row=2, column=0,background="Grey")
        self.addLabel(text="", row=3, column=0,background="Grey")
        self.addLabel(text="", row=4, column=0,background="Grey")
        self.addLabel(text="", row=5, column=0,background="Grey")
        self.addLabel(text="", row=6, column=0,background="Grey")
        self.addLabel(text="", row=7, column=0,background="Grey")
        self.addLabel(text="", row=8, column=0,background="Grey")
        self.addLabel(text="", row=9, column=0,background="Grey")

        self.addButton(text= "Go Back To Choices", row = 0,column = 3, command = self.recipes_type_Page)

        self.addButton(text = "Main Menu" , row=0, column=4, command=self.execute_multiple_commands)

    def EX_Recipe2(self):

        EXRecipe  = self.addPanel(row=0, column=0,rowspan=18, columnspan=10, background="Grey")

        self.addLabel(text="", row=1, column=0,background="Grey")
        self.addLabel(text="", row=2, column=0,background="Grey")
        self.addLabel(text="", row=3, column=0,background="Grey")
        self.addLabel(text="", row=4, column=0,background="Grey")
        self.addLabel(text="", row=5, column=0,background="Grey")
        self.addLabel(text="", row=6, column=0,background="Grey")
        self.addLabel(text="", row=7, column=0,background="Grey")
        self.addLabel(text="", row=8, column=0,background="Grey")
        self.addLabel(text="", row=9, column=0,background="Grey")

        self.addButton(text= "Go Back To Choices", row = 0,column = 3, command = self.Recipes_on)
        self.addButton(text = "Main Menu" , row=0, column=4, command=self.execute_multiple_commands)

"""

#_________________________________________________________________________________________________________________________________



                    #Template for testing if user has chosen the proper ingrediants to make a recipe




"""

matching_EXAMPLErecipe = [s for s in Ingrediants if s in ExampleRecipe ]

        if len(matching_EXAMPLErecipe) >= <Number of ingrediants required for recipe> :
            self.addButton(text = "Cook Now" , row=4, column=3, command= self.<Recipe Instruction Panel>)
            self.addLabel(text="Example Food", row = 4, column= 2,background="Grey")

"""

#_________________________________________________________________________________________________________________________________

                                    # Template for creating another catagory panel for extra recipes
                                       # This template is used for creating a panel being used in
                                        # The testing format "Get Recipes", not for "All Recipes".

                                # The reasoning for this seperation between buttons is due to only listing the
                                # Available recipes when clicking on "Get recipes". But needs to list all recipes
                                # When user chooses "All Recipes". So the call back buttons need to be different,
                                # One sent to a page where the users data was tested, and another where it displays
                                # All the available recipes


"""
def recipes_Page2(self):
        
        RecipesPage = self.addPanel(row=0, column=0,rowspan=18, columnspan=10, background="Grey")
        self.myFirstLabel= self.addLabel(text="Recipes Available to Cook Now", row=0, column=0)
        
        font = Font(family="Verdana", size=20, slant="italic")
        self.myFirstLabel["font"] = font
        self.myFirstLabel["foreground"] = "Purple"
        self.myFirstLabel["background"] = "Grey"
        self.addButton(text = "Main Menu" , row=0, column=4, command=self.execute_multiple_commands)
        self.addButton(text= "Back" , row = 0, column = 3, command=self.recipes_type_Page)

#       You would place more test data here.....................


#                                        Example

#       matching_GCrecipe = [s for s in Ingrediants if s in grilledCheese ]

#       if len(matching_GCrecipe) >= 3:
#           self.addButton(text = "Cook Now" , row=1, column=3, command= self.GC_Recipe)
#           self.addLabel(text="Grilled Cheese", row = 1, column= 2,background="Grey")

"""

