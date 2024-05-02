from breezypythongui import EasyFrame
from tkinter.font import Font
import tkinter
from Ingrediants_list import Ingrediants
grilledCheese = ["Cheese","Butter","Bread"]
cheeseburger = ["Cheese","Hamburger","Ketchup","Mustard","Bread","Pickles"]
spaghettiAndMeatballs = ["Spaghetti Noodles","Tomato Sauce","Meatballs"]

class RecipesPage(EasyFrame):
     def __init__(self):
        EasyFrame.__init__(self, title="Recipes",width=1300,height=950 )
        self.myFirstLabel = self.addLabel(text="Pantry App", row=0, column=0)
        self.addLabel(text="Recipes", row=0, column=1)
        font = Font(family="Verdana", size=20, slant="italic")
        self.myFirstLabel["font"] = font
        self.myFirstLabel["foreground"] = "Black"
        self.myFirstLabel["background"] = "Gray"
        
        matching_GCrecipe = [s for s in Ingrediants if s in grilledCheese ]

        if len(matching_GCrecipe) == 3:
            self.GCbutton = self.addButton(text = "Grilled Cheese" , row=1, column=2)
if __name__ == "__main__":
    window = RecipesPage()
    window.mainloop()