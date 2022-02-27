from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

try:
    card_df = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    og_data = pandas.read_csv("data/french_words.csv")
    to_learn = og_data.to_dict(orient="records")
else:
    to_learn = card_df.to_dict(orient="records")
    current_card = {}


def next_card():
    global current_card, canvas_timer
    window.after_cancel(canvas_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(lang_label, text="French", fill="black")
    canvas.itemconfig(word_label, text=current_card["French"], fill="black")
    canvas_timer = window.after(3000, card_flip)


def card_flip():
    canvas.itemconfig(card_canvas, image=card_back)
    canvas.itemconfig(lang_label, text="English", fill="White")
    canvas.itemconfig(word_label, text=current_card["English"], fill="White")


def correct():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()


# --------------------------UI SETTINGS-------------------------#
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
canvas_timer = window.after(3000, card_flip)

canvas = Canvas(height=525, width=800, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
card_canvas = canvas.create_image(400, 275, image=card_front)
canvas.grid(row=0, column=0, columnspan=2)

lang_label = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
word_label = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))

# buttons
check_img = PhotoImage(file="images/right.png")
correct_button = Button(image=check_img, highlightthickness=0, command=correct)
correct_button.grid(row=1, column=1)
cross_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=cross_img, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)

next_card()

window.mainloop()
