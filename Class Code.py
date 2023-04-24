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

    def continents(self, *args):
        if self.dropdown == "South America":
            label2 = Label(self.master, text="Pick a number (1-12):", command=self.south_america)
            label2.pack()
        elif self.dropdown == "Asia":
            label3 = Label(self.master, text="Pick a number(1-31): ")
            label3.pack()
        elif self.dropdown == "North America":
            label4 = Label(self.master, text="Pick a numner (1-50):")
            label4.pack()
    

    def south_america(self, *args):
        number = int(self.dropdown.get())
        if number == 1:
            country = "Columbia"
        elif number == 2:
            country = "Ecuador"
        elif number == 3:
            country = "Bolivia"
        elif number == 4:
            country = "Brazil"
        elif number== 5:
            country = "Argentina"
        elif number==6:
            country = "Venezuela"
        elif number == 7:
            country = "Chile"
        elif number == 8:
            country = "Paraguay"
        elif number == 9:
            country = "Peru"
        elif number == 10:
            country = "Uruguay"
        elif number == 11:
            country = "Suriname"
        elif number == 12:
            country= "Guyana"
        self.word_label.config(text=self.word_label)



root.mainloop()
