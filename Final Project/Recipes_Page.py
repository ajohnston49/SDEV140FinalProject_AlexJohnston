from breezypythongui import EasyFrame
from tkinter.font import Font
import tkinter
from Ingrediants_list import Ingrediants
grilledCheese = ["cheese","butter","bread"]
cheeseburger = ["cheese","hamburger","ketchup","mustard","bread","pickle"]
spaghettiAndMeatballs = ["spaghetti","tomatosauce","meatballs"]

class RecipesPage(EasyFrame):
     def __init__(self):
        EasyFrame.__init__(self, title="Recipes",width=1300,height=950 )
        self.myFirstLabel = self.addLabel(text="Pantry App", row=0, column=0)
        self.addLabel(text="Pantry App", row=0, column=0)
        font = Font(family="Verdana", size=20, slant="italic")
        self.myFirstLabel["font"] = font
        self.myFirstLabel["foreground"] = "Black"
        self.myFirstLabel["background"] = "Gray"
        self.mySecondLabel = self.addLabel(text = "UGH", row=1, column=2)
if __name__ == "__main__":
    window = RecipesPage()
    window.mainloop()