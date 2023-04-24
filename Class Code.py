from tkinter import *
from tkinter import ttk
root = Tk()
root.geometry("400x400")

label1 = Label(root, text= "Global Travel Generator!")
label1.pack()

class Generator:
 
    def __init__ (self,master):
        self.master = master
        self.dropdown()
        

    def dropdown(self):
        self.label1 = Label(self.master, text="Pick A Continent: ")
        self.label1.pack()

        self.label_var = StringVar()
        self.label_var.set("Click for Continent")
        self.label_optionmenu = OptionMenu(self.master, self.label_var, "Africa","Antartica","Asia", "Australia","Europe","North America", "South America", command=self.continents)
        self.label_optionmenu.pack()

        self.word_label = Label(self.master, text="")
        self.word_label.pack()
