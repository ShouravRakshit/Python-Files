from tkinter import Tk, Label, Button, Entry

window = Tk()
window.title("My Game")
window.minsize(width=500, height=600)

label = Label(text="I am a label", font=("Arial", 20, "bold"))
label.grid(column=0, row=0)
label["text"] = "I am Super"


def button_click():
    new_message = (user_input.get())
    if new_message == "on":
        label.config(text="On")
    else:
        label.config(text="Off")


def new_button_click():
    print("Shinsuke Nakamura")


button = Button(text="Click here", command=button_click)
button.grid(column=1, row=1)

new_button = Button(text="New Button", command=new_button_click)
new_button.grid(column=2, row=0)
user_input = Entry(width=15)

user_input.grid(column=3, row=2)
window.mainloop()
