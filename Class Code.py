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
        self.states = ["","Alabamba", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Deleware", "Flordia", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts","Michigan", "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Vermont", "Virgina", "Washington", "West Virginia", "Wisconsin", "Wyoming"]
        self.sacountries = ["","Columbia", "Ecuador", "Bolivia", "Brazil", "Argentina", "Venezuela", "Chile", "Paraguay", "Peru", "Uruguay", "Suriname", "Guyana"]
        self.eu =["","Albania", "Andorra", "Armenia", "Austria", "Azerbaijan", "Belarus", "Belgium", "Bosnia & Herzegovina", "Bulgaria", "Croatia", "Cyprus", "Czech Republic", "Denmark", "Estonia", "Finland", "France", "Georgia", "Germany", "Greece", "Hungary","Iceland", "Ireland", "Italy", "Kosovo", "Latvia", "Liechtenstein", "Lithuania", "Luxembourg", "Malta", "Moldova","Monaco", "Montenegro", "Netherlands", "North Macedonia", "Norway", "Poland", "Portugal", "Romania", "Russia", "San Marino", "Serbia", "Slovakia", "Slovenia","Spain", "Sweden", "Switzerland", "Turkey", "Ukraine", "United Kingdom", "Vatican City"]
        self.acountries = ["","New South Wales", "Queensland", "South Australia", "Tasmania", "Victoria", "Western Autstrlia"]
        self.afcountries = ["","Algeria", "Angola", "Benin", "Botswana", "Burkina Faso", "Burundi", "Cabo Verde", "Cameroon", "Central African Republic (CAR)", "Chad", "Comoros", "Democratic Republic of the Congo", "Republic of the Congo", "Cote d'Ivoire", "Djibouti", "Egypt", "Equatorial Guinea", "Eritrea", "Eswatini (formerly Swaziland)", "Ethiopia", "Gabon", "Gambia", "Ghana", "Guinea", "Guinea-Bissau", "Kenya", "Lesotho", "Liberia", "Libya", "Madagascar", "Malawi", "Mali", "Mauritania", "Mauritius", "Morocco", "Mozambique","Namibia", "Niger", "Nigeria", "Rwanda", "Sao Tome and Principe", "Senegal", "Seychelles", "Sierra Leone", "Somalia", "South Africa", "South Sudan", "Sudan", "Tanzania", "Togo", "Tunisia", "Uganda", "Zambia", "Zimbabwe"]
        self.ascountries = ["","China", "India", "Indonesia", "Pakistan", "Bangladesh", "Japan", "Philippines", "Vietnam", "Turkey", "Iran", "Thailand", "South Korea", "Afganistan", "Saudi Arabia", "Uzbekistan", "Malaysia", "Yemen", "Nepal"," Sri Lanka", "Kazakhstan", "Syria", "Cambodia", "Jordan", "Isereal", "Laos", "Lebanon", "Singapore", "Georgia", "Mongolia", "Armenia", "Bhutan", "Maldives"]
        self.antcountries = ["","Antartica"]
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
            label5 = Label(self.master, text="Pick a number (1-50):", background="#FFBFA9", font=("Ink Free", 20))
            label5.pack()
            self.europe()
        elif self.selected_continent.get() == "Africa":
            label6 = Label(self.master, text="Pick a number (1-54):", background="#FFBFA9", font=("Ink Free", 20))
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
        self.state_options.pack()


    def south_america(self, *args):
        self.selected_sacountries= StringVar()
        self.selected_sacountries.set("Click For A Country")
        self.sacountry_options = OptionMenu(
            self.master,
            self.selected_sacountries,
            *range(len(self.sacountries)),
            #command=self.show_sacountry
        )
        self.sacountry_options.pack()

    def asia(self, *args):
        self.selected_ascountries= StringVar()
        self.selected_ascountries.set("Click For A Country")
        self.asia_options = OptionMenu(
            self.master,
            self.selected_ascountries,
            *range(len(self.ascountries))
        )
        self.asia_options.pack()


    def europe(self, *args):
        self.selected_europe= StringVar()
        self.selected_europe.set("Click For A Country")
        self.europe_options = OptionMenu(
            self.master,
            self.selected_europe,
            *range(len(self.eu))
        )
        self.europe_options.pack()

    def africa(self, *args):
        self.selected_africa= StringVar()
        self.selected_africa.set("Click For A Country")
        self.africa_options = OptionMenu(
            self.master,
            self.selected_africa,
            *range(len(self.afcountries))
        )
        self.africa_options.pack()
    def australia(self, *args):
        self.selected_australia= StringVar()
        self.selected_australia.set("Click For A Country")
        self.australia_options = OptionMenu(
            self.master,
            self.selected_australia,
            *range(len(self.acountries))
        )
        self.australia_options.pack()
    def antartica(self, *args):
        self.selected_antartica= StringVar()
        self.selected_antartica.set("Click For A Country")
        self.antartica_options = OptionMenu(
            self.master,
            self.selected_antartica,
            *range(len(self.antcountries))
        )
        self.antartica_options.pack()




app1 = Travel_Explorer()
app1.config(bg='#FFBFA9')
app1.mainloop()