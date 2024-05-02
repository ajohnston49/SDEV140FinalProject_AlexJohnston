from breezypythongui import EasyFrame
from tkinter.font import Font
import tkinter
Ingrediants = []

class MyWindow(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title="Final Project SDEV140",width=1300,height=950 )
        self.myFirstLabel = self.addLabel(text="Pantry App", row=0, column=0)
        font = Font(family="Verdana", size=20, slant="italic")
        self.myFirstLabel["font"] = font
        self.myFirstLabel["foreground"] = "Purple"
        self.myFirstLabel["background"] = "White"
        # Create a checkbox
        self.checkbutton = self.addCheckbutton(text="Cheese", row=1, column=3,command = Ingrediants.append("Cheese"))
        self.checkbutton = self.addCheckbutton(text="Bread", row=2, column=3,command = Ingrediants.append("Bread"))
        self.checkbutton = self.addCheckbutton(text="Butter", row=4, column=3,command = Ingrediants.append("Butter"))
        self.checkbutton = self.addCheckbutton(text="Hamburger", row=5, column=3,command = Ingrediants.append("Hamburger"))
        self.checkbutton = self.addCheckbutton(text="Milk", row=6, column=3,command = Ingrediants.append("Milk")) 
        self.checkbutton = self.addCheckbutton(text="Oil", row=7, column=3,command = Ingrediants.append("Oil"))
        self.checkbutton = self.addCheckbutton(text="Ketchup", row=8, column=3,command = Ingrediants.append("Ketchup"))
        self.checkbutton = self.addCheckbutton(text="Mustard", row=9, column=3,command = Ingrediants.append("Mustard"))
        self.checkbutton = self.addCheckbutton(text="Pickles", row=10, column=3,command = Ingrediants.append("Pickles"))
        self.checkbutton = self.addCheckbutton(text="Spaghetti Noodles", row=11, column=3,command = Ingrediants.append("Spaghetti Noodles"))
        self.checkbutton = self.addCheckbutton(text="Tomato Sauce", row=12, column=3,command = Ingrediants.append("Tomato Sauce"))
        self.checkbutton = self.addCheckbutton(text="Eggs", row=13, column=3,command = Ingrediants.append("Eggs"))
        # Create a button
        self.addButton(text="Get Recipes", row=14, column=0, command = (self.addLabel(text= Ingrediants, row=15, column=1)))

class RecipesPage(EasyFrame):
     def __init__(self):
        EasyFrame.__init__(self, title="Recipes",width=1300,height=950 )
        self.RecipesPage = tkinter.Toplevel()
        self.RecipesPage.title("Recipes Page")
        self.addLabel(text="Pantry App", row=0, column=0)
        font = Font(family="Verdana", size=20, slant="italic")
        self.myFirstLabel["font"] = font
        self.myFirstLabel["foreground"] = "Black"
        self.myFirstLabel["background"] = "Gray"
        

    
if __name__ == "__main__":
    window = MyWindow()
    window.mainloop()

    def RecipesPage(self):
        self.newWindow = tkinter.Toplevel()
        self.newWindow.title("New Window")

