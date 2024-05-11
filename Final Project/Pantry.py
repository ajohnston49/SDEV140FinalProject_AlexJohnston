from breezypythongui import EasyFrame,EasyCanvas
import tkinter
from tkinter.font import Font
from tkinter import PhotoImage

# Emtpy list for user choices
 
Ingrediants = []


# Predefined recipes

grilledCheese = ["Cheese","Butter","Bread"]
cheeseburger = ["Cheese","Hamburger","Bread",]
spaghettiAndMeatballs = ["Spaghetti Noodles","Tomato Sauce","Hamburger"]

# ANY NEW RECIPES WITH INGREDIANTS NOT LISTED MUST HAVE A CHECK BUTTON CREATED FOR USER INPUT
# ALONG WITH A NEW 'COOKNOW' BUTTON ON THE SECOND WINDOW AND A CALL EVENT FOR THE STEPS ON A THIRD WINDOW

class MyWindow(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self,title="Pantry",background="Grey")
        MainPanel = self.addPanel(row=0, column=0,rowspan=14, columnspan=10, background="Grey")
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
       
        self.addButton(text="Get Recipes", row=14, column=0, command = self.recipes_Page)
        self.addButton(text="All Recipes", row=14, column=2, command = self.Recipes_on)


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
       
        self.addButton(text="Get Recipes", row=14, column=0, command = self.recipes_Page)
        self.addButton(text="All Recipes", row=14, column=2, command = self.Recipes_on)

        def add_cheese(SecondaryMainPanel):
            Ingrediants.append("Cheese")
        def add_bread(SecondaryMainPanel):
            Ingrediants.append("Bread")
        def add_butter(SecondaryMainPanel):
            Ingrediants.append("Butter")
        def add_HB(SecondaryMainPanel):
            Ingrediants.append("Hamburger")
        def add_milk(SecondaryMainPanel):
            Ingrediants.append("Milk")
        def add_oil(SecondaryMainPanel):
            Ingrediants.append("Oil")
        def add_ketchup(SecondaryMainPanel):
            Ingrediants.append("Ketchup")
        def add_Mustard(SecondaryMainPanel):
            Ingrediants.append("Mustard")
        def add_Pickle(SecondaryMainPanel):
            Ingrediants.append("Pickles")
        def add_SN(SecondaryMainPanel):
            Ingrediants.append("Spaghetti Noodles")
        def add_TS(SecondaryMainPanel):
            Ingrediants.append("Tomato Sauce")
        def add_eggs(SecondaryMainPanel):
            Ingrediants.append("Eggs")



    #Adds user choices to the empty list 'Ingrediants'

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

    
    def Recipes_on(self):
        RecipesOn = self.addPanel(row=0, column=0,rowspan=18, columnspan=10, background="Grey")
        self.addLabel(text="All Available Recipes", row = 0, column= 1,background="Grey",foreground="Purple")
        self.addButton(text = "Cook Now" , row=3, column=3, command= self.SM_Recipe2)
        self.addLabel(text="Spaghetti & Meatballs", row = 3, column= 2,background="Grey")
        self.addButton(text = "Cook Now" , row=1, column=3, command= self.GC_Recipe2)
        self.addLabel(text="Grilled Cheese", row = 1, column= 2,background="Grey")
        self.addButton(text = "Cook Now" , row=2, column=3, command= self.CB_Recipe2)
        self.addLabel(text="CheeseBurger", row = 2, column= 2,background="Grey")
        self.addButton(text = "Back" , row=0, column=4, command=self.execute_multiple_commands)
        self.addLabel(text="CheeseBurger", row = 2, column= 2,background="Grey")
        
    

# Steps for making a grilled cheese

    def GC_Recipe(self):
        GCRecipe = self.addPanel(row=0, column=0,rowspan=18, columnspan=10, background="Grey")
        self.addLabel(text="Start by buttering one side of two pieces of bread", row=1, column=0,background="Grey")
        self.addLabel(text="Next, With the butter side facing out, put a slice of cheese between your bread", row=2, column=0,background="Grey")
        self.addLabel(text="Then fry it on a hot skillet flipping it about every 3 minutes or ", row=3, column=0,background="Grey")
        self.addLabel(text="Until Desired color and texture is achieved.", row=4, column=0,background="Grey")
        self.addLabel(text=" ", row=5, column=0,background="Grey")
        self.addLabel(text="Enjoy by itself or with your favorite soup!", row=6, column=0,background="Grey")
        self.addButton(text= "Go Back To Choices", row = 0,column = 3, command = self.recipes_Page )
        self.addButton(text = "Main Menu" , row=0, column=4, command=self.execute_multiple_commands)

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
        


# Steps for making a cheeseburger

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
        self.addButton(text= "Go Back To Choices", row = 0,column = 3, command = self.recipes_Page)
        self.addButton(text = "Main Menu" , row=0, column=4, command=self.execute_multiple_commands)

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
        
#Steps for making Spaghetti and Meatballs 

    def SM_Recipe(self):
        SMRecipe = self.addPanel(row=0, column=0,rowspan=18, columnspan=10, background="Grey")
        self.addLabel(text="Start by getting a deep pan of water boiling, and then add your noodles.", row=1, column=0,background="Grey")
        self.addLabel(text="Next, roll your hamburger into inch size balls, place them on a flat pan and bake them at 375 for 20 minutes.", row=2, column=0,background="Grey")
        self.addLabel(text="Once the spaghetti is cooked to the desired softness, drain the water and add your suace and throw back on low heat.", row=3, column=0,background="Grey")
        self.addLabel(text="Once the Meatballs are done, drain any grease and add them to your spahetti and cover for another 15 minutes.", row=4, column=0,background="Grey")
        self.addLabel(text=" Your spaghetti is now ready to enjoy to enjoy!", row=5, column=0,background="Grey")
        self.addLabel(text=" ", row=5, column=0,background="Grey")
        self.addLabel(text="Enjoy by itself or with your favorite bread!", row=6, column=0,background="Grey")
        self.addButton(text= "Go Back To Choices", row = 0,column = 3, command = self.recipes_Page )
        self.addButton(text = "Main Menu" , row=0, column=4, command=self.execute_multiple_commands)

    def SM_Recipe2(self):
        SMRecipe = self.addPanel(row=0, column=0,rowspan=18, columnspan=10, background="Grey")
        self.addLabel(text="Start by getting a deep pan of water boiling, and then add your noodles.", row=1, column=0,background="Grey")
        self.addLabel(text="Next, roll your hamburger into inch size balls, place them on a flat pan and bake them at 375 for 20 minutes.", row=2, column=0,background="Grey")
        self.addLabel(text="Once the spaghetti is cooked to the desired softness, drain the water and add your suace and throw back on low heat.", row=3, column=0,background="Grey")
        self.addLabel(text="Once the Meatballs are done, drain any grease and add them to your spahetti and cover for another 15 minutes.", row=4, column=0,background="Grey")
        self.addLabel(text=" Your spaghetti is now ready to enjoy to enjoy!", row=5, column=0,background="Grey")
        self.addLabel(text=" ", row=5, column=0,background="Grey")
        self.addLabel(text="Enjoy by itself or with your favorite bread!", row=6, column=0,background="Grey")
        self.addButton(text= "Go Back To Choices", row = 0,column = 3, command = self.Recipes_on )
        self.addButton(text = "Main Menu" , row=0, column=4, command=self.execute_multiple_commands)

#Creates a recipes page that is called when hitting the 'get recipes' button on the parent window

    def recipes_Page(self):
        RecipesPage = self.addPanel(row=0, column=0,rowspan=18, columnspan=10, background="Grey")
        self.myFirstLabel= self.addLabel(text="Recipes Available to Cook Now", row=0, column=0)
        
        font = Font(family="Verdana", size=20, slant="italic")
        self.myFirstLabel["font"] = font
        self.myFirstLabel["foreground"] = "Purple"
        self.myFirstLabel["background"] = "Grey"
        self.addButton(text = "Main Menu" , row=0, column=4, command=self.execute_multiple_commands)
         # Tests the number of matching user inputs to the predefined recipes and if the number
         # Of matches equals to the number of ingrediants within the list, it displays a button  
         # That will display the steps To cook the recipe

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
               

    #Resets the program
            
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

        
if __name__ == "__main__":
    window = MyWindow()
    window.mainloop()


#Prints user chosen ingrediants within IDE for testing
print(Ingrediants)
