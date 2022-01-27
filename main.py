from tkinter import *


window = Tk()
window.title("First Gui Program")
window.minsize(width=500, height=300)

#Label. Class inside of tkinter

myLabel = Label(text="I am a label", font=("Ariel", 24, "bold"))
myLabel.pack(side="top")
#Can change the value of an option several ways
myLabel["text"] = "New Text"
myLabel.config(text="Diff Text")

#BUTTON - has many optional args,kwargs than can be used. Like text, command. Command is used to initiate
#commands when the button is clicked. Lots of auto detection for the click. function below is what happens
#when the button is clicked.


def button_clicked():
    print("I was clicked")
    myLabel.config(text=textfield.get())


button = Button(text="Click Me", command=button_clicked)
button.pack()


#ENTRY - creates a text field for users to enter data. Code below simply creates and places the textbox.
#Use the .get() method to obtain the data from the entry field.


textfield = Entry(width=10)
textfield.pack()





window.mainloop()