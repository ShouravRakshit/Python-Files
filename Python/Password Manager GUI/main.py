from tkinter import *
from tkinter import messagebox
from password import Password
import pyperclip
import json

new_password = Password()


def generate_password():
    strong_password = new_password.random_password()
    password_entry.insert(0, strong_password)
    # Automatically copies the password in the clipboard.
    pyperclip.copy(strong_password)


def info_from_entry():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    return [website, email, password]


def search_info():
    entry_data = info_from_entry()
    try:
        with open("data.json", mode="r") as load_file:
            # Loading the file.
            data = json.load(load_file)
            messagebox.showinfo(title=data[entry_data[0]], message=f'Email: {data[entry_data[0]]["email"]}\n'
                                                                   f'Password: {data[entry_data[0]]["password"]}')
    except KeyError as lost_key:
        print(f"You don't have any website that has the name {lost_key}")


def add_info():
    entry_data = info_from_entry()
    new_data = {
        entry_data[0]: {
            "email": entry_data[1],
            "password": entry_data[2]
        }
    }
    if len(entry_data[0]) < 2 or len(entry_data[2]) < 2:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        details = messagebox.askokcancel(title=entry_data[0],
                                         message=f"These are details you have entered\n Email: {entry_data[1]}\n Password: {entry_data[2]}")
        if details:

            try:
                with open("data.json", mode="r") as load_file:
                    # Loading the file.
                    data = json.load(load_file)
                    # Updating the file.
                    data.update(new_data)

            except FileNotFoundError:
                with open("data.json", mode="w") as data_file:
                    # Writing the file.
                    json.dump(new_data, data_file, indent=4)

            else:
                with open("data.json", mode="w") as data_file:
                    # Writing the file.
                    json.dump(data, data_file, indent=4)
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.minsize(width=400, height=400)
window.title("Password Manager")
window.config(padx=30, pady=30)
logo = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200)
canvas.create_image(60, 100, image=logo)
canvas.grid(column=1, row=0)

# Website label
website_label = Label()
website_label.config(text="Website : ")
website_label.grid(column=0, row=1, pady=3)
website_label.focus()

# Website text field
website_entry = Entry(width=22)
website_entry.place(x=100, y=207)

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

# Button for adding the info in the data.json file.
add_button = Button(width=33, text="Add", command=add_info)
add_button.place(x=100, y=290)

search_button = Button(text="Search", command=search_info)
search_button.place(x=245, y=203)
search_button.config(width=13)

window.mainloop()
