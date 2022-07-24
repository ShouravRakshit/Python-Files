from quiz_brain import QuizBrian
from tkinter import *
from bs4 import BeautifulSoup

THEME_COLOR = "#375362"
question_number = 0
score = 0
question_list = QuizBrian()
question_bank = question_list.get_questions()
answer_list = question_list.answer()


# Method for showing the next question in the list.
def next_question():
    if question_number == 10:
        field_text.itemconfig(my_text, text=f"Thank you for playing this game.\n"
                                            f"Your score is {score}.")
        field_text.configure(bg="blue")
    else:
        field_text.itemconfig(my_text, text=f'{BeautifulSoup(question_bank[question_number], "lxml").text}')
        field_text.configure(bg="white")


# Method for the tik button.
def right_button():
    global question_number
    global score
    if answer_list[question_number] == "True":
        field_text.configure(bg="green")
        score += 1
        score_label.config(text=f"Score: {score}")

    else:
        field_text.configure(bg="red")
    question_number += 1

    timer = window.after(1500, next_question)


# Method for the cross button.
def wrong_button():
    global question_number
    global score
    if answer_list[question_number] == "False":
        field_text.configure(bg="green")
        score += 1
        score_label.config(text=f"Score: {score}")

    else:
        field_text.configure(bg="red")
    question_number += 1

    timer = window.after(1500, next_question)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.minsize(width=400, height=550)
window.title("Quizzler")
window.config(padx=10, pady=10, bg=THEME_COLOR, bd=0, relief='ridge')

field_text = Canvas(width=320, height=297, bg="white")
field_text_space = PhotoImage()
field_text.create_image(100, 50, image=field_text_space)
my_text = field_text.create_text(170, 120, text=f'{BeautifulSoup(question_bank[0], "lxml").text}', font=("Purisa", 15),
                                 width=150)
field_text.place(x=30, y=60)

correct_picture = Canvas(width=200, height=197)
correct_picture_logo = PhotoImage(file="images/true.png")
correct_picture.create_image(50, 100, image=correct_picture_logo)
correct_button = Button(image=correct_picture_logo, bd=0, relief='ridge', command=right_button)
correct_button.place(x=30, y=400)

false_picture = Canvas(width=100, height=197)
false_picture_logo = PhotoImage(file="images/false.png")
false_picture.create_image(50, 100, image=false_picture_logo)
false_button = Button(image=false_picture_logo, bd=0, relief='ridge', command=wrong_button)
false_button.place(x=250, y=400)

score_label = Label(text="Score: 0", bg=THEME_COLOR, fg="white", font=("Purisa", 15))
score_label.place(x=270, y=15)

window.mainloop()
