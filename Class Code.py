from tkinter import *
from tkinter import ttk





class Travel_Explorer(Tk):
    '''
    EXPLAIN WHAT THIS OBJECT IS
    '''
    #List of all states and countries and optionmenu
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        
        self.label1 = Label(self, text= "Global Travel Explorer!", background="#a8ccc7", font=("Ink Free", 23))
        self.label1.grid(row=0,column=1)
        self.states = ["Alabamba", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Deleware", "Flordia", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts","Michigan", "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Vermont", "Virgina", "Washington", "West Virginia", "Wisconsin", "Wyoming"]
        self.sacountries = ["Columbia", "Ecuador", "Bolivia", "Brazil", "Argentina", "Venezuela", "Chile", "Paraguay", "Peru", "Uruguay", "Suriname", "Guyana"]
        self.eu =["Albania", "Andorra", "Armenia", "Austria", "Azerbaijan", "Belarus", "Belgium", "Bosnia & Herzegovina", "Bulgaria", "Croatia", "Cyprus", "Czech Republic", "Denmark", "Estonia", "Finland", "France", "Georgia", "Germany", "Greece", "Hungary","Iceland", "Ireland", "Italy", "Kosovo", "Latvia", "Liechtenstein", "Lithuania", "Luxembourg", "Malta", "Moldova","Monaco", "Montenegro", "Netherlands", "North Macedonia", "Norway", "Poland", "Portugal", "Romania", "Russia", "San Marino", "Serbia", "Slovakia", "Slovenia","Spain", "Sweden", "Switzerland", "Turkey", "Ukraine", "United Kingdom", "Vatican City"]
        self.acountries = ["New South Wales", "Queensland", "South Australia", "Tasmania", "Victoria", "Western Autstrlia"]
        self.afcountries = ["Algeria", "Angola", "Benin", "Botswana", "Burkina Faso", "Burundi", "Cabo Verde", "Cameroon", "Central African Republic (CAR)", "Chad", "Comoros", "Democratic Republic of the Congo", "Republic of the Congo", "Cote d'Ivoire", "Djibouti", "Egypt", "Equatorial Guinea", "Eritrea", "Eswatini (formerly Swaziland)", "Ethiopia", "Gabon", "Gambia", "Ghana", "Guinea", "Guinea-Bissau", "Kenya", "Lesotho", "Liberia", "Libya", "Madagascar", "Malawi", "Mali", "Mauritania", "Mauritius", "Morocco", "Mozambique","Namibia", "Niger", "Nigeria", "Rwanda", "Sao Tome and Principe", "Senegal", "Seychelles", "Sierra Leone", "Somalia", "South Africa", "South Sudan", "Sudan", "Tanzania", "Togo", "Tunisia", "Uganda", "Zambia", "Zimbabwe"]
        self.ascountries = ["China", "India", "Indonesia", "Pakistan", "Bangladesh", "Japan", "Philippines", "Vietnam", "Turkey", "Iran", "Thailand", "South Korea", "Afganistan", "Saudi Arabia", "Uzbekistan", "Malaysia", "Yemen", "Nepal"," Sri Lanka", "Kazakhstan", "Syria", "Cambodia", "Jordan", "Isereal", "Laos", "Lebanon", "Singapore", "Georgia", "Mongolia", "Armenia", "Bhutan", "Maldives"]
        self.antcountries = ["Antartica"]
        self.continents=["Africa","Antartica","Asia", "Australia","Europe","North America", "South America"]
        self.choose_continent()
        
        
        self.title("Global Travel Explorer")
        
       
    #Main componenet that allows user to choose a continent
    def choose_continent(self):
        self.label1 = Label(self.master, text="Pick A Continent: ", background="#A8CCC7",font=("Ink Free", 20))
        self.label1.grid(row=2,column=1)

        self.selected_continent = StringVar()
        self.selected_continent.set("Click for Continent")
        self.optionmenu = OptionMenu(
            self.master, 
            self.selected_continent, 
            *self.continents,
            command=self.choose_country,
            )
        self.optionmenu.grid(row=3,column=1)

        self.word_label = Label(self.master, text="")
        self.word_label.grid(row=2, column=0)
        
    #Function that allows user to choose continent
    def choose_country(self, *args):
        if self.selected_continent.get() == "South America":
            label2 = Label(self.master, text="Pick a number (0-11):", background="#A8CCC7", font=("Ink Free", 20))
            label2.grid(row=4,column=1)
            self.south_america()
        elif self.selected_continent.get() == "Asia":
            label3 = Label(self.master, text="Pick a number(0-30): ", background="#A8CCC7", font=("Ink Free", 20))
            label3.grid(row=4,column=1)
            self.asia()
        elif self.selected_continent.get() == "North America":
            label4 = Label(self.master, text="Pick a number (0-49):", background="#A8CCC7", font=("Ink Free", 20))
            label4.grid(row=4,column=1)
            self.north_america()
        elif self.selected_continent.get() == "Europe":
            label5 = Label(self.master, text="Pick a number (0-49):", background="#A8CCC7", font=("Ink Free", 20))
            label5.grid(row=4,column=1)
            self.europe()
        elif self.selected_continent.get() == "Africa":
            label6 = Label(self.master, text="Pick a number (0-53):", background="#A8CCC7", font=("Ink Free", 20))
            label6.grid(row=4,column=1)
            self.africa()
        elif self.selected_continent.get() == "Antartica":
            label7 = Label(self.master, text="Pick a number (0):", background="#A8CCC7", font=("Ink Free", 20))
            label7.grid(row=4,column=1)
            self.antartica()
        elif self.selected_continent.get() == "Australia":
            label8 = Label(self.master, text="Pick a number (0-5):", background="#A8CCC7", font=("Ink Free", 20))
            label8.grid(row=4,column=1)
            self.australia() 
    
    #Function that allows user to choose number for US states
    def north_america(self, *args):
        #number2 = int(self.choose_country.get())-1
        self.selected_state = StringVar()
        self.selected_state.set("Click For A State")
        self.state_options = OptionMenu(
            self.master, 
            self.selected_state, 
            *range(len(self.states)),
            command=self.show_state
        )
        self.state_options.grid(row=5,column=1)
    def show_state(self, *args):
            self.word_label.config(text=self.states[int(self.selected_state.get())])
            self.word_label.grid(row=10, column=1,padx=10, pady=10)
            label1= Label(self, text="Congrats your next destination is...", background="#A8CCC7", font=("Ink Free", 15))
            label1.grid(row=9, column=1, padx=10, pady=10)
            command=self.show_state
            self.word_label
        

        
    #Function that allows user to choose number for SA countries
    def south_america(self, *args):
        self.selected_sacountries= StringVar()
        self.selected_sacountries.set("Click For A Country")
        self.sacountry_options = OptionMenu(
            self.master,
            self.selected_sacountries,
            *range(len(self.sacountries)),
            command=self.show_sacountry
        )
        self.sacountry_options.grid(row=5, column =1)
    def show_sacountry(self, *args):
        self.word_label.config(text=self.sacountries[int(self.selected_sacountries.get())])
        self.word_label.grid(row=10, column=1, padx=10, pady=10)
        label1= Label(self, text="Congrats your next destination is...", background="#A8CCC7", font=("Ink Free", 15))
        label1.grid(row=9, column=1, padx=10, pady=10)
        command=self.show_sacountry


    #Function that allows user to choose number for Asia countries
    def asia(self, *args):
        self.selected_ascountries= StringVar()
        self.selected_ascountries.set("Click For A Country")
        self.asia_options = OptionMenu(
            self.master,
            self.selected_ascountries,
            *range(len(self.ascountries)),
            command=self.show_ascountry
        )
        self.asia_options.grid(row=4, column=1)
    def show_ascountry(self, *args):
        self.word_label.config(text=self.ascountries[int(self.selected_ascountries.get())])
        self.word_label.grid(row=10, column=1, padx=10, pady=10)
        label1= Label(self, text="Congrats your next destination is...", background="#A8CCC7", font=("Ink Free", 15))
        label1.grid(row=9, column=1, padx=10, pady=10)
        command=self.show_ascountry

    #Function that allows user to choose number for Europe countries
    def europe(self, *args):
        self.selected_europe= StringVar()
        self.selected_europe.set("Click For A Country")
        self.europe_options = OptionMenu(
            self.master,
            self.selected_europe,
            *range(len(self.eu)),
            command=self.show_europe
        )
        self.europe_options.grid(row=5, column=1)
    def show_europe(self, *args):
        self.word_label.config(text=self.eu[int(self.selected_europe.get())])
        self.word_label.grid(row=10, column=1, padx=10, pady=10)
        label1= Label(self, text="Congrats your next destination is...", background="#A8CCC7", font=("Ink Free", 15))
        label1.grid(row=9, column=1, padx=10, pady=10)
        command=self.show_europe

    #Function that allows user to choose number for Africa countries
    def africa(self, *args):
        self.selected_africa= StringVar()
        self.selected_africa.set("Click For A Country")
        self.africa_options = OptionMenu(
            self.master,
            self.selected_africa,
            *range(len(self.afcountries)),
            command=self.show_africa
        )
        self.africa_options.grid(row=5, column=1)
    def show_africa(self, *args):
        self.word_label.config(text=self.afcountries[int(self.selected_africa.get())])
        self.word_label.grid(row=10, column=1, padx=10, pady=10)
        label1= Label(self, text="Congrats your next destination is...", background="#A8CCC7", font=("Ink Free", 15))
        label1.grid(row=9, column=1, padx=10, pady=10)
        command=self.show_africa


    #Function that allows user to choose number for Australia countries
    def australia(self, *args):
        self.selected_australia= StringVar()
        self.selected_australia.set("Click For A Country")  
        self.australia_options = OptionMenu(
            self.master,
            self.selected_australia,
            *range(len(self.acountries)),
            command=self.show_australia
        )
        self.australia_options.grid(row=5, column=1)
    def show_australia(self, *args):
        self.word_label.config(text=self.acountries[int(self.selected_australia.get())])
        self.word_label.grid(row=10, column=1, padx=10, pady=10)
        label1= Label(self, text="Congrats your next destination is...", background="#A8CCC7", font=("Ink Free", 15))
        label1.grid(row=9, column=1, padx=10, pady=10)
        command=self.show_australia

    def antartica(self, *args):
        self.selected_antartica= StringVar()
        self.selected_antartica.set("Click For A Country")
        self.antartica_options = OptionMenu(
            self.master,
            self.selected_antartica,
            *range(len(self.antcountries)),
            command=self.show_antartica
        )
        self.antartica_options.grid(row=5, column=1)
    def show_antartica(self, *args):
        self.word_label.config(text=self.antcountries[int(self.selected_antartica.get())])
        self.word_label.grid(row=10, column=1, padx=10, pady=10)
        label1= Label(self, text="Congrats your next destination is...", background="#A8CCC7", font=("Ink Free", 15))
        label1.grid(row=9, column=1, padx=10, pady=10)
        label2= Label(self, text="It might be a little cold here.", background="#A8CCC7", font=("Ink Free", 15))
        label2.grid(row=11, column=1, padx=10, pady=10)
        command=self.show_antartica





#Lets everything function
app1 = Travel_Explorer()
app1.config(bg='#A8CCC7')
app1.mainloop()