from breezypythongui import EasyFrame, EasyCanvas, EasyDialog
from tkinter.font import Font
import tkinter
from tkinter import PhotoImage
import tkinter as tk
from SecondWindow_Test import RecipesWindow
import breezypythongui as bpg


# Emtpy list for user choices
 
Ingrediants = []

# Predefined recipes
# ANY NEW RECIPES WITH INGREDIANTS NOT LISTED MUST HAVE A CHECK BUTTON CREATED FOR USER INPUT
# ALONG WITH A NEW 'COOKNOW' BUTTON ON THE SECOND WINDOW AND A CALL EVENT FOR THE STEPS ON A THIRD WINDOW
grilledCheese = ["Cheese","Butter","Bread"]
cheeseburger = ["Cheese","Hamburger","Bread",]
spaghettiAndMeatballs = ["Spaghetti Noodles","Tomato Sauce","Hamburger"]

# Creates the main window

class MyWindow(bpg.EasyDialog):
    def __init__(self):
        EasyDialog.__init__(self, title="Final Project SDEV140")
        self.myFirstLabel = self.addLabel(text="Pantry App", row=0, column=0)
        
       
        font = Font(family="Verdana", size=20, slant="italic")
        self.myFirstLabel["font"] = font
        self.myFirstLabel["foreground"] = "Purple"
        self.myFirstLabel["background"] = "White"    
    
    # Creates a column of check buttons that add user selected 'ingrediants' to a list

        self.checkbutton = self.addCheckbutton(text="Cheese", row=1, column=3,command = self.add_cheese)
        self.checkbutton = self.addCheckbutton(text="Bread", row=2, column=3,command = self.add_bread)
        self.checkbutton = self.addCheckbutton(text="Butter", row=4, column=3,command = self.add_butter)
        self.checkbutton = self.addCheckbutton(text="Hamburger", row=5, column=3,command = self.add_HB)
        self.checkbutton = self.addCheckbutton(text="Milk", row=6, column=3,command = self.add_milk)
        self.checkbutton = self.addCheckbutton(text="Oil", row=7, column=3,command = self.add_oil)
        self.checkbutton = self.addCheckbutton(text="Ketchup", row=8, column=3,command = self.add_ketchup)
        self.checkbutton = self.addCheckbutton(text="Mustard", row=9, column=3,command = self.add_Mustard)
        self.checkbutton = self.addCheckbutton(text="Pickles", row=10, column=3,command = self.add_Pickle)  
        self.checkbutton = self.addCheckbutton(text="Spaghetti Noodles", row=11, column=3,command = self.add_SN)
        self.checkbutton = self.addCheckbutton(text="Tomato Sauce", row=12, column=3,command = self.add_TS)
        self.checkbutton = self.addCheckbutton(text="Eggs", row=13, column=3,command = self.add_eggs)
        self.addButton(text="Get Recipes", row=14, column=0, command = recipes_Page )
        self.addButton(text="Get Recipes window", row=14, column=1, command = RecipesWindow)
        
    
        
    
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
        Ingrediants.append("Spaghtetti Noodles")
    def add_TS(self):
        Ingrediants.append("Tomato Sauce")
    def add_eggs(self):
        Ingrediants.append("Eggs")

# Steps for making a grilled cheese

def GC_Recipe():
    class GCRecipe(EasyFrame):
        def __init__(self):
            EasyFrame.__init__(self,title="Grilled Cheese Instructions")
            self.addLabel(text="Start by buttering one side of two pieces of bread", row=1, column=0)
            self.addLabel(text="Next, With the butter side facing out, put a slice of cheese between your bread", row=2, column=0)
            self.addLabel(text="Then fry it on a hot skillet flipping it about every 3 minutes or ", row=3, column=0)
            self.addLabel(text="Until Desired color and texture is achieved.", row=4, column=0)
            self.addLabel(text=" ", row=5, column=0)
            self.addLabel(text="Enjoy by itself or with your favorite soup!", row=6, column=0)
    if __name__ == "__main__":
        window = GCRecipe()
        window.mainloop()

# Steps for making a cheeseburger

def CB_Recipe():
    class CBRecipe(EasyFrame):
        def __init__(self, resizeable = True):
            EasyFrame.__init__(self,title="Cheeseburger Instructions")
            self.addLabel(text="Start by forming the raw Hamburger into a patty like shape.", row=1, column=0)
            self.addLabel(text="Next, get a pan hot on medium/hot setting(varying, depends on your appliance)", row=2, column=0)
            self.addLabel(text="Then fry the patty, flipping every 3 minutes or so until desired color and texture is acheived. ", row=3, column=0)
            self.addLabel(text="NOTE: Raw meat can contain bacteria harmful to your health.", row=4, column=0)
            self.addLabel(text=" Once the patty is cooked, turn off the heat, flip your patty so the hottest side is facing up, ", row=5, column=0)
            self.addLabel(text=" And lay your cheese on top the patty and cover the pan for 5 minutes.", row=6, column=0)
            self.addLabel(text="While the cheese melts, get your bread ready and gather all your toppings to make your cheeseburger! ", row=7, column=0)
            self.addLabel(text=" ", row=8, column=0)
            self.addLabel(text="Enjoy by itself or with your favorite sides!", row=9, column=0)
    if __name__ == "__main__":
        window = CBRecipe()
        window.mainloop()

#Steps for making Spaghetti and Meatballs 

def SM_Recipe():
    class SMRecipe(EasyFrame):
        def __init__(self):
            EasyFrame.__init__(self,title="Spaghetti & Meatballs Instructions")
            self.addLabel(text="Start by getting a deep pan of water boiling, and then add your noodles.", row=1, column=0)
            self.addLabel(text="Next, roll your hamburger into inch size balls, place them on a flat pan and bake them at 375 for 20 minutes.", row=2, column=0)
            self.addLabel(text="Once the spaghetti is cooked to the desired softness, drain the water and add your suace and throw back on low heat.", row=3, column=0)
            self.addLabel(text="Once the Meatballs are done, drain any grease and add them to your spahetti and cover for another 15 minutes.", row=4, column=0)
            self.addLabel(text=" Your spaghetti is now ready to enjoy to enjoy!", row=5, column=0)
            self.addLabel(text=" ", row=5, column=0)
            self.addLabel(text="Enjoy by itself or with your favorite bread!", row=6, column=0)
    if __name__ == "__main__":
        window = SMRecipe()
        window.mainloop()

#Creates a recipes page that is called when hitting the 'get recipes' button on the parent window

def recipes_Page():
    class RecipesPage(EasyFrame):
        def __init__(self):
            EasyFrame.__init__(self, width=1300,height=950 )
            self.myFirstLabel= self.addLabel(text="Recipes Available to Cook Now", row=0, column=0)
        
            font = Font(family="Verdana", size=20, slant="italic")
            self.myFirstLabel["font"] = font
            self.myFirstLabel["foreground"] = "Black"
            self.myFirstLabel["background"] = "Gray"
         
         # Tests the number of matching user inputs to the predefined recipes and if the number
         # Of matches equals to the number of ingrediants within the list, it displays a button  
         # That will display the steps To cook the recipe

            matching_GCrecipe = [s for s in Ingrediants if s in grilledCheese ]

            if len(matching_GCrecipe) == 3:
                self.addButton(text = "Cook Now" , row=1, column=3, command= GC_Recipe)
                self.addLabel(text="Grilled Cheese", row = 1, column= 2)
            matching_CBrecipe = [s for s in Ingrediants if s in cheeseburger ]

            if len(matching_CBrecipe) == 3:
                self.addButton(text = "Cook Now" , row=2, column=3, command= CB_Recipe)
                self.addLabel(text="CheeseBurger", row = 2, column= 2)
            
            matching_SMrecipe = [s for s in Ingrediants if s in cheeseburger ]

            if len(matching_SMrecipe) == 3:
                self.addButton(text = "Cook Now" , row=3, column=3, command= SM_Recipe)
                self.addLabel(text="Spaghetti & Meatballs", row = 3, column= 2)

    if __name__ == "__main__":
        window = RecipesPage()
        window.mainloop()

# Instructions for the grilled cheese recipe to be called by button

def GC_Recipe(): 
    class GCRecipe(EasyFrame):
        def __init__(self):
            EasyFrame.__init__(self,title="Grilled Cheese Instructions")
            self.addLabel(text="Start by buttering one side of two pieces of bread", row=1, column=0)
            self.addLabel(text="Next, With the butter side facing out, put a slice of cheese between your bread", row=2, column=0)
            self.addLabel(text="Then fry it on a hot skillet flipping it about every 3 minutes or ", row=3, column=0)
            self.addLabel(text="Until Desired color and texture is achieved.", row=4, column=0)
            self.addLabel(text=" ", row=5, column=0)
            self.addLabel(text="Enjoy by itself or with your favorite soup!", row=6, column=0)
    if __name__ == "__main__":
        window = GCRecipe()
        window.mainloop()

def Second_Window():
    class SecondWindow(EasyFrame):
        def __init__(Alex):
            EasyFrame.__init__(Alex, title="Recipes Page",width=1300,height=950 )
            Alex.myFirstLabel = Alex.addLabel(text="Recipes", row=0, column=0)
            font = Font(family="Verdana", size=20, slant="italic")
            Alex.myFirstLabel["font"] = font
            Alex.myFirstLabel["foreground"] = "Purple"
            Alex.myFirstLabel["background"] = "White"
    if __name__ == "__main__":
        window = SecondWindow()
        window.mainloop()





if __name__ == "__main__":
    window = MyWindow()
    window.mainloop()


#Prints user chosen ingrediants within IDE for testing
print(Ingrediants)
