from tkinter import *
from tkinter import ttk



class Travel_Explorer(Tk):
    '''
    EXPLAIN WHAT THIS OBJECT IS
    '''
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        
        self.label1 = Label(self, text= "Global Travel Option Explorer!", background="#FFBFA9", font=("Ink Free", 23))
        self.label1.pack(pady=10)
        self.states = ["Alabamba", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Deleware", "Flordia", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts","Michigan", "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Vermont", "Virgina", "Washington", "West Virginia", "Wisconsin", "Wyoming"]
        self.sacountries = ["Columbia", "Ecuador", "Bolivia", "Brazil", "Argentina", "Venezuela", "Chile", "Paraguay", "Peru", "Uruguay", "Suriname", "Guyana"]
        self.continents=["Africa","Antartica","Asia", "Australia","Europe","North America", "South America"]
        self.choose_continent()
        
        self.geometry("400x400")
        
       

    def choose_continent(self):
        self.label1 = Label(self.master, text="Pick A Continent: ", background="#FFBFA9",font=("Ink Free", 20))
        self.label1.pack()

        self.selected_continent = StringVar()
        self.selected_continent.set("Click for Continent")
        self.optionmenu = OptionMenu(
            self.master, 
            self.selected_continent, 
            *self.continents,
            command=self.choose_country,
            )
        self.optionmenu.pack()

        self.word_label = Label(self.master, text="")
        self.word_label.pack()
        

    def choose_country(self, *args):
        if self.selected_continent.get() == "South America":
            label2 = Label(self.master, text="Pick a number (1-10):", background="#FFBFA9", font=("Ink Free", 20))
            label2.pack()
            self.south_america()
        elif self.selected_continent.get() == "Asia":
            label3 = Label(self.master, text="Pick a number(1-30): ", background="#FFBFA9", font=("Ink Free", 20))
            label3.pack()
            self.asia()
        elif self.selected_continent.get() == "North America":
            label4 = Label(self.master, text="Pick a number (1-50):", background="#FFBFA9", font=("Ink Free", 20))
            label4.pack()
            self.north_america()
        elif self.selected_continent.get() == "Europe":
            label5 = Label(self.master, text="Pick a number (1-29):", background="#FFBFA9", font=("Ink Free", 20))
            label5.pack()
            self.europe()
        elif self.selected_continent.get() == "Africa":
            label6 = Label(self.master, text="Pick a number (1-29):", background="#FFBFA9", font=("Ink Free", 20))
            label6.pack()
            self.africa()
        elif self.selected_continent.get() == "Antartica":
            label7 = Label(self.master, text="Pick a number (1):", background="#FFBFA9", font=("Ink Free", 20))
            label7.pack()
            self.antartica()
        elif self.selected_continent.get() == "Australia":
            label8 = Label(self.master, text="Pick a number (1-4):", background="#FFBFA9", font=("Ink Free", 20))
            label8.pack()
            self.australia()
    

    #def south_america(self, *args):
        #number = int(self.choose_country.get())
        #if number == 1:
            #country = "Columbia"
        #elif number == 2:
            #country = "Ecuador"
        #elif number == 3:
            #country = "Bolivia"
        #elif number == 4:
            #country = "Brazil"
        #elif number== 5:
            #country = "Argentina"
        #elif number==6:
            #country = "Venezuela"
        #elif number == 7:
            #country = "Chile"
        #elif number == 8:
            #country = "Paraguay"
        #elif number == 9:
            #country = "Peru"
        #elif number == 10:
            #country = "Uruguay"
        #elif number == 11:
            #country = "Suriname"
        #elif number == 12:
            #country= "Guyana"
        #self.word_label.config(text=self.word_label)
    
    def north_america(self, *args):
        #number2 = int(self.choose_country.get())-1
        self.selected_state = StringVar()
        self.selected_state.set("Click For A State")
        self.state_options = OptionMenu(
            self.master, 
            self.selected_state, 
            *range(len(self.states))
            #command=self.show_state
        )

    def south_america(self, *args):
        self.selected_sacountries= StringVar()
        self.selected_sacountries.set("Click For A Country")
        self.sacountry_options = OptionMenu(
            self.master,
            self.selected_sacountries,
            *range(len(self.sacountries)),
            #command=self.show_sacountry
        )
    def asia(self, *args):
        self.selected_asia= StringVar()
        self.selected_asia.set("Click For A Country")
        self.asia_options = OptionMenu(
            self.master,
            self.selected_asia,
            *range(len(self.asia))
        )
    def europe(self, *args):
        self.selected_europe= StringVar()
        self.selected_europe.set("Click For A Country")
        self.europe_options = OptionMenu(
            self.master,
            self.selected_europe,
            *range(len(self.europe))
        )
    def africa(self, *args):
        self.selected_africa= StringVar()
        self.selected_africa.set("Click For A Country")
        self.africa_options = OptionMenu(
            self.master,
            self.selected_africa,
            *range(len(self.africa))
        )
    def australia(self, *args):
        self.selected_australia= StringVar()
        self.selected_australia.set("Click For A Country")
        self.australia_options = OptionMenu(
            self.master,
            self.selected_australia,
            *range(len(self.australia))
        )
    def antartica(self, *args):
        self.selected_antartica= StringVar()
        self.selected_antartica.set("Click For A Country")
        self.antartica_options = OptionMenu(
            self.master,
            self.selected_antartica,
            *range(len(self.antartica))
        )




app1 = Travel_Explorer()
app1.config(bg='#FFBFA9')
app1.mainloop()