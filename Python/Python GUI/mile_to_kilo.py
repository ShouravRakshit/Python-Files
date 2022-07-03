from tkinter import Tk, Entry, Label, Button

window = Tk()
window.title("Converter")
window.minsize(width=100, height=100)
window.config(padx=30, pady=30)
# Created a black space so that user can input a value.
user_input = Entry()
user_input.config(width=10)

# Created four labels.
user_input.grid(column=1, row=0)
label_one = Label()
label_one.config(text="Miles", padx=10, pady=10)
label_one.grid(column=2, row=0)
label_two = Label()
label_two.config(text=f"is equal to")
label_two.grid(column=0, row=1)
label_third = Label()
label_third.grid(column=1, row=1)
label_third.config(text="")
label_four = Label()
label_four.grid(column=2, row=1)
label_four.config(text="Km")


# This function converts the mile to kilometre.
def convert():
    mile = int(user_input.get())
    km = mile * 1.61
    label_third.config(text=str(round(km, 3)))


# Created a button for converting the mile to kilometre.
button = Button(text="Calculate", command=convert)
button.grid(column=1, row=2)

window.mainloop()
