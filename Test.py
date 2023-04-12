from tkinter import *
from tkinter import ttk
root = Tk()
root.title("Global Travel Generator")
root.config(bg='#FFBFA9')
root.geometry("600x400")

topLabel = Label(root, text="Global Travel Generator!", background="#FFBFA9", font=("fangsong ti", 30))
topLabel.pack(pady=35)


#When user selects continent from dropdown the range in which the a user should enter a number will show up.
def select(event):
    #myLabel = Label(root, text=selected.get()).pack()
    if selected.get() == "South America":
        myLabel = Label(root, text="Pick a number(0-11): ",bg='#FFBFA9', font=("fangsong ti", 15))
        myLabel.pack()
    elif  selected.get() == "North America":
        myLabel = Label(root, text="Pick a number (0-50):").pack()
    elif selected.get() == "Africa":
        myLabel = Label(root, text= "Pick a number (0-30):").pack()
    elif selected.get() == "Europe":
        myLabel = Label(root, text="Pick a number (0-30):").pack()
    elif selected.get() == "Asia":
        myLabel = Label(root, text="Pick a number (0-31):").pack()
    elif selected.get() == "Australia":
        myLabel = Label(root, text="Pick a number (0-5):").pack()
    elif selected.get() == "Antarctica":
        myLabel = Label(root, text="Pick a number (0):").pack()
    else:
        myLabel = Label(root, text=selected.get()).pack().pack()
        
options = [
    "Pick A Continenet",
    "South America",
    "North America",
    "Africa",
    "Europe",
    "Asia",
    "Antarctica",
    "Australia"
]

selected = StringVar()
selected.set(options[0])

menu = OptionMenu(root, selected, *options, command=select)
menu.pack(pady=20)


#myButton = Button(root, text="Click to select continent", commmand=select)
#myButton.pack()


root.mainloop()
