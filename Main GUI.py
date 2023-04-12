from tkinter import *
from tkinter import ttk
root = Tk()
root.title("Global Travel Generator")
root.config(bg='#FFBFA9')
root.geometry("600x400")

topLabel = Label(root, text="Global Travel Generator!", background="#FFBFA9", font=("fangsong ti", 30))
topLabel.pack(pady=35)

def select(event):
    myLabel = Label(root, text=selected.get()).pack()
  

selected = StringVar()
selected.set(options[0])

menu = OptionMenu(root, selected, *options, command=select)
menu.pack(pady=20)



#myButton = Button(root, text="Click to select continent", commmand=select)
#myButton.pack()


root.mainloop() 
