from breezypythongui import EasyFrame
from tkinter.font import Font
import tkinter
Ingrediants = []
class RecipesPage(EasyFrame):
     def __init__(self):
        EasyFrame.__init__(self, title="Recipes",width=1300,height=950 )
        self.addLabel(text="Pantry App", row=0, column=0)
        font = Font(family="Verdana", size=20, slant="italic")
        self.myFirstLabel["font"] = font
        self.myFirstLabel["foreground"] = "Black"
        self.myFirstLabel["background"] = "Gray"