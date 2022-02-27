from tkinter import *


def mi_to_km():
    miles = int(textfield.get())
    kilos = round(miles * 1.609)
    ans_label.config(text=kilos)


#SCREEN
window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=200, height=150)
window.config(padx=20, pady=20)

#LABELS
mi_label = Label(text="Miles", font=("Ariel", 12,))
mi_label.grid(column=4, row=0)
mi_label.config(padx=5, pady=5)

km_label = Label(text="Km", font=("Ariel", 12,))
km_label.grid(column=4, row=2)
km_label.config(padx=5, pady=5)

eq_label = Label(text="is equal to", font=("Ariel", 12,))
eq_label.grid(column=2, row=2)
eq_label.config(padx=5, pady=5)

ans_label = Label(text="0", font=("Ariel", 12,))
ans_label.grid(column=3, row=2)
ans_label.config(padx=5, pady=5)


#BUTTON
button = Button(text="Calculate", command=mi_to_km)
button.grid(column=3, row=3)


#ENTRY
textfield = Entry(width=10)
textfield.grid(column=3, row=0)


window.mainloop()