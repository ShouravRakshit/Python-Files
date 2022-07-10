from tkinter import *
from tkinter import messagebox
import random
import string


# This function generates random password for the users if they click the generate password button.
def generate_password():
    alphabet = list(string.ascii_letters)
    symbols = ['~', ':', "'", '+', '[', '\\', '@', '^', '{', '%', '(', '-', '"', '*', '|', ',', '&', '<', '`', '}', '.',
               '_', '=', ']', '!', '>', ';', '?', '#', '$', ')', '/']
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    strong_password_list = random.sample(alphabet, random.randint(1, 4)) + random.sample(symbols,
                                                                                         random.randint(1, 4)) + \
                           random.sample(numbers, random.randint(1, 4))
    strong_password = ""
    for key in range(len(strong_password_list)):
        strong_password = strong_password + str(strong_password_list[key])

    password_entry.insert(0, strong_password)


def add_info():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    if len(website) < 2 or len(password) < 2:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        details = messagebox.askokcancel(title=website,
                                         message=f"These are details you have entered\n Email: {email}\n Password: {password}")
        if details:
            with open("data.txt", mode="a") as f:
                store_content = f.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.minsize(width=400, height=400)
window.title("Password Manager")
window.config(padx=30, pady=30)
logo = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 150, image=logo)
canvas.grid(column=1, row=0)

# Website label
website_label = Label()
website_label.focus()
website_label.config(text="Website : ")
website_label.grid(column=0, row=1, pady=3)

# Website text field
website_entry = Entry(width=40)
website_entry.grid(column=1, row=1, pady=3)
# Email label
email_label = Label()
email_label.config(text="Email/Username : ")
email_label.grid(column=0, row=2, pady=3)

# Email entry
email_entry = Entry(width=40)
email_entry.grid(column=1, row=2, pady=3)
email_entry.insert(0, "example@email.com")

# Password label
password_label = Label()
password_label.config(text="Password : ")
password_label.grid(column=0, row=3, pady=3)

# Password entry
password_entry = Entry(width=21)
password_entry.place(x=100, y=264)

# Password generate button
button = Button(width=14, text="Generate Password", command=generate_password)
button.place(x=235, y=260)

add_button = Button(width=33, text="Add", command=add_info)
add_button.place(x=100, y=290)
window.mainloop()
