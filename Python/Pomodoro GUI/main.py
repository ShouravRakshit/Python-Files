import math
from tkinter import *

# CONSTANTS
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 20
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
checker = ""


# This method resets everything.
def reset():
    window.after_cancel(timer)
    canvas.itemconfig(time_text, text="00:00")
    label_timer.config(text="Timer", fg=GREEN)
    checkbox.config(text="")


def second_to_minute():
    global reps
    reps += 1
    work_time = WORK_MIN * 60
    break_time = SHORT_BREAK_MIN * 60
    big_break_time = LONG_BREAK_MIN * 60

    # If reps is even then, it is on work mode. If reps is odd, then it is on short break.
    # If reps is evenly divided by 8, then it is on long break.
    if reps % 8 == 0:
        count_down(big_break_time)
        label_timer.config(text="Big Break", fg=RED)
        label_timer.place(x=160, y=90)

    elif reps % 2 != 0:
        count_down(work_time)
        label_timer.config(text="Timer", fg=GREEN)
        label_timer.place(x=200, y=90)

    elif reps % 2 == 0:
        count_down(break_time)
        label_timer.config(text="Break", fg=PINK)
        label_timer.place(x=200, y=90)


def count_down(time_remain):
    # Formatting the time to 00:00.
    minutes = math.floor(time_remain / 60)
    seconds = time_remain % 60
    global checker
    if seconds < 10:
        seconds = f"0{seconds}"

    if minutes < 10:
        minutes = f"0{minutes}"

    if time_remain > 0:
        global timer
        canvas.itemconfig(time_text, text=f"{minutes}:{seconds}")
        timer = window.after(50, count_down, time_remain - 1)
    else:
        second_to_minute()
        # After every two rep one tik mark is added.
        if reps % 2 == 0:
            checker = checker + "✓"
            checkbox.config(text=checker)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.config(bg=YELLOW)
window.title("Pomodoro")
window.minsize(width=500, height=600)
canvas = Canvas(width=230, height=394, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(120, 270, image=tomato_image)
time_text = canvas.create_text(120, 300, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
label_timer = Label()
label_timer.config(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 30, "bold"))
label_timer.place(x=200, y=90)
start_button = Button()
start_button.config(text="Start", highlightthickness=0, command=second_to_minute)
start_button.place(x=120, y=400)
reset_button = Button()
reset_button.config(text="Reset", highlightthickness=0, command=reset)
reset_button.place(x=330, y=400)
checkbox = Label()
checkbox.config(highlightthickness=0, text="", bg=YELLOW, fg=GREEN)
checkbox.place(x=240, y=420)
canvas.pack()
window.mainloop()
