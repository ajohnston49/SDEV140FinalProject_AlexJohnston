from breezypythongui import EasyFrame
from tkinter.font import Font
import tkinter
from tkinter import PhotoImage
import breezypythongui as bpg 

class RecipesWindow(bpg.EasyDialog):
    def __init__(self):
        super().__init__(self.Mywindow, title="My Custom Dialog")
        
if __name__ == "__main__":
    dialog = RecipesWindow()


