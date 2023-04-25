from tkinter import *
from tkinter import ttk



class Travel_Explorer(Tk):
    '''
    EXPLAIN WHAT THIS OBJECT IS
    '''
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        
        self.label1 = Label(self, text= "Global Travel Option Explorer!")
        self.label1.pack()
        self.states = ["Alabamba", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Deleware", "Flordia", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts","Michigan", "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Vermont", "Virgina", "Washington", "West Virginia", "Wisconsin", "Wyoming"]
        self.sacountries = ["Columbia", "Ecuador", "Bolivia", "Brazil", "Argentina", "Venezuela", "Chile", "Paraguay", "Peru", "Uruguay", "Suriname", "Guyana"]
        self.continents=["Africa","Antartica","Asia", "Australia","Europe","North America", "South America"]
        self.choose_continent()
        self.geometry("400x400")

    def choose_continent(self):
        self.label1 = Label(self.master, text="Pick A Continent: ")
        self.label1.pack()

        self.selected_continent = StringVar()
        self.selected_continent.set("Click for Continent")
        self.optionmenu = OptionMenu(
            self.master, 
            self.selected_continent, 
            *self.continents,
            command=self.choose_country
            )
        self.optionmenu.pack()

        self.word_label = Label(self.master, text="")
        self.word_label.pack()

    def choose_country(self, *args):
        if self.selected_continent.get() == "South America":
            label2 = Label(self.master, text="Pick a number (1-12):", command=self.south_america)
            label2.pack()
        elif self.selected_continent.get() == "Asia":
            label3 = Label(self.master, text="Pick a number(1-31): ")
            label3.pack()
        elif self.selected_continent.get() == "North America":
            label4 = Label(self.master, text="Pick a numner (1-50):")
            label4.pack()
            self.north_america()
    

    def south_america(self, *args):
        number = int(self.choose_country.get())
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
    
    def north_america(self, *args):
        #number2 = int(self.choose_country.get())-1
        self.selected_state = StringVar()
        self.selected_state.set("Click for State")
        self.state_options = OptionMenu(
            self.master, 
            self.selected_state, 
            *range(len(self.states))
            #command=self.show_state
        )



    

        


app1 = Travel_Explorer()
app1.mainloop()