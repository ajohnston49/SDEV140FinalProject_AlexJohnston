from breezypythongui import EasyFrame
from tkinter.font import Font
import tkinter
Ingrediants = []
grilledCheese = ["Cheese","Butter","Bread"]
cheeseburger = ["Cheese","Hamburger","Ketchup","Mustard","Bread","Pickles"]
spaghettiAndMeatballs = ["Spaghetti Noodles","Tomato Sauce","Meatballs"]
class MyWindow(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title="Final Project SDEV140",width=1300,height=950 )
        self.myFirstLabel = self.addLabel(text="Pantry App", row=0, column=0)
        font = Font(family="Verdana", size=20, slant="italic")
        self.myFirstLabel["font"] = font
        self.myFirstLabel["foreground"] = "Purple"
        self.myFirstLabel["background"] = "White"    
        # Create a checkbox
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
        # Create a button

        self.addButton(text="Get Recipes", row=14, column=0, command = recipes_Page )

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
def recipes_Page():
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
                self.addButton(text = "Grilled Cheese" , row=1, column=2, command= GC_Recipe)
    if __name__ == "__main__":
        window = RecipesPage()
        window.mainloop()

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

if __name__ == "__main__":
    window = MyWindow()
    window.mainloop()

print(Ingrediants)
