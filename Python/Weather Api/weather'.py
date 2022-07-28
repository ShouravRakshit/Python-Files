from tkinter import *
import requests
import os
from datetime import datetime
# This program lets you type any city name in the top bar.
# The result is that you are going to get the weather of that city.

BG = "#404040"
FONT = "Helvetica 15 bold"

password = os.environ["weather_password"]


def search_country():
    # Taking the input from the entry box.
    city_name = search_bar_entry.get()
    # The required parameters of the api.
    parameters = {
        "q": f"{city_name}",
        "appid": password
    }

    try:
        response = requests.get("https://api.openweathermap.org/data/2.5/weather?", params=parameters)
        response.raise_for_status()

        data = response.json()
        temp_data = data["main"]["temp"] - 273
        wind_data = ((data["wind"]["speed"]) * 3600) / 1000
        humidity_data = data["main"]["humidity"]
        description_data = data["weather"][0]["description"]
        pressure_data = data["main"]["pressure"] * .029613
        feels_like_data = data["main"]["feels_like"] - 273

        # Showing the api datas on the screen.
        blue_bar.itemconfig(wind_text, text=f"{round(wind_data, 2)} km/h", fill="black", font=FONT)
        blue_bar.itemconfig(humidity_text, text=f"{humidity_data}%", fill="black", font=FONT)
        blue_bar.itemconfig(description_text, text=f"{description_data}", fill="black", font=FONT)
        blue_bar.itemconfig(pressure_text, text=f"{round(pressure_data, 2)} inHg", fill="black", font=FONT)

        temp_label.config(text=f"{round(temp_data, 2)} °")
        description_label.config(text=f"{description_data}   |")
        feels_like_label.config(text=f"FEELS LIKE {round(feels_like_data, 2)} °")

    # If there is a HTTPError, then it will show no city name found name on the entry box.
    except requests.HTTPError:
        search_bar_entry.delete(0, END)
        search_bar_entry.config(font="Helvetica 20 bold")
        search_bar_entry.insert(0, "No city name was found")


window = Tk()
window.title("Weather App")
window.minsize(width=850, height=500)

# Creating the search bar.
search_bar = Canvas(width=475, height=100)
search_bar_logo = PhotoImage(file="search.png")
search_bar.create_image(250, 70, image=search_bar_logo)
search_bar.place(x=20, y=10)

# Creating the entry box.
search_bar_entry = Entry(width=22, font=("poppins", 25, "bold"))
search_bar_entry.config(fg="white", bg=BG, border=0, justify='center')
search_bar_entry.place(x=70, y=60)

# The search icon for this program.
search_icon = Canvas(width=60, height=63, bg=BG, highlightthickness=0, border=0)
search_icon_logo = PhotoImage(file="search_icon.png")
search_icon.create_image(26, 23, image=search_icon_logo)

# Making the search icon a button.
button = Button(image=search_icon_logo, command=search_country, borderwidth=0, bg=BG, activebackground="#404040")
button.place(x=400, y=53)

# Creating the weather icon.
weather_icon = Canvas(width=260, height=245, bd=0, highlightthickness=0, relief='ridge')
weather_icon_logo = PhotoImage(file="logo.png")
weather_icon.create_image(130, 100, image=weather_icon_logo)
weather_icon.place(x=120, y=130)

# The label for the temperature.
temp_label = Label(text="", font="Helvetica 35 bold")
temp_label.place(x=400, y=200)

# The label for the description.
description_label = Label(text="", font="Helvetica 10 bold")
description_label.place(x=380, y=260)

# The label for the feels_like.
feels_like_label = Label(text="", font="Helvetica 10 bold")
feels_like_label.place(x=500, y=260)

current_time_label = Label()
current_time_label.place(x=400, y=120)

# The bar for showing the details of the weather.
blue_bar = Canvas(width=820, height=100, bd=0, highlightthickness=0, relief='ridge')
blue_bar_logo = PhotoImage(file="box.png")
blue_bar.create_image(380, 40, image=blue_bar_logo)

blue_bar.create_text(70, 20, fill="white", font=FONT, text="WIND")

blue_bar.create_text(260, 20, fill="white", font=FONT, text="HUMIDITY")

blue_bar.create_text(460, 20, fill="white", font=FONT, text="DESCRIPTION")

blue_bar.create_text(660, 20, fill="white", font=FONT, text="PRESSURE")

wind_text = blue_bar.create_text(70, 60, fill="black", font=FONT, text="...")

humidity_text = blue_bar.create_text(260, 60, fill="black", font=FONT, text="...")

description_text = blue_bar.create_text(460, 60, fill="black", font=FONT, text="...")

pressure_text = blue_bar.create_text(660, 60, fill="black", font=FONT, text="...")

blue_bar.place(x=30, y=380)

window.mainloop()
