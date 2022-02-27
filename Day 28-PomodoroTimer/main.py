# Pomodoro Technique Timer #
from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
timer = NONE


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global REPS
    REPS = 0
    window.after_cancel(timer)
    title.config(text="Timer", fg=GREEN, font=(FONT_NAME, 35, "bold"))
    canvas.itemconfig(timer_text, text="00:00")
    checkmarks.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global REPS
    REPS += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if REPS % 8 == 0:
        count_down(long_break_sec)
        title.config(text="Break", fg=RED, font=(FONT_NAME, 35, "bold"))
    elif REPS % 2 == 0:
        count_down(short_break_sec)
        title.config(text="Break", fg=PINK, font=(FONT_NAME, 35, "bold"))
    else:
        count_down(work_sec)
        title.config(text="Work", fg=GREEN, font=(FONT_NAME, 35, "bold"))


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:  # Readme#
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count >= 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        work_cycles = math.floor(REPS/2)
        for _ in range(work_cycles):
            marks = ""
            marks += "✓"
            checkmarks.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato)
timer_text = canvas.create_text(100, 132, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)


title = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 35, "bold"))
title.config(bg=YELLOW)
title.grid(column=1, row=0)

checkmarks = Label(fg=GREEN, bg=YELLOW, )
checkmarks.grid(column=1, row=3)

start_button = Button(text="Start", command=start_timer)
start_button.grid(column=0, row=2)
reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(column=2, row=2)


window.mainloop()