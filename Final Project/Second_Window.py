from breezypythongui import EasyFrame
from tkinter.font import Font
import tkinter
from tkinter import PhotoImage

class SecondWindow(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title="Final Project SDEV140",width=1300,height=950 )
        self.myFirstLabel = self.addLabel(text="Recipes", row=0, column=0)
        font = Font(family="Verdana", size=20, slant="italic")
        self.myFirstLabel["font"] = font
        self.myFirstLabel["foreground"] = "Purple"
        self.myFirstLabel["background"] = "White"

if __name__ == "__main__":
    window = SecondWindow()
    window.mainloop()
        
