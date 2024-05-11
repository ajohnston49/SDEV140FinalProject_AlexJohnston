from breezypythongui import EasyFrame

class MyWindow(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title="My Window", width=400, height=300)
        # Create a frame within the window
        my_frame = self.addFrame(row=0, column=0, rowspan=1, columnspan=1)
        # Add widgets (buttons, labels, etc.) to the frame

if __name__ == "__main__":
    MyWindow().mainloop()
