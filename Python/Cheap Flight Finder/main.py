import json
import requests
import airportsdata
from tkinter import *
import datetime
import os

BG = "#404040"
FONT = "Helvetica 18 bold"
API_KEY = os.environ.get("airplane_api")


def getting_flight():
    # Taking the input from the entry boxes.
    country_from = from_entry.get()
    country_to = to_entry.get()
    date_from = date_from_entry.get()
    date_to = date_to_entry.get()

    # Loading the data from the airportsdata
    airports = airportsdata.load()
    current_place = []
    destinations = []
    # Looping through all the item in the airports dictionary and checking if the city name matches with
    # input I have given in the entry box.
    for airport in airports:
        if airports[airport]["city"] == country_from:
            current_place.append(airports[airport]["iata"])
        if airports[airport]["city"] == country_to:
            destinations.append(airports[airport]["iata"])

    current_place = list(filter(lambda string: string.strip(), current_place))
    destinations = list(filter(lambda string: string.strip(), destinations))

    header = {
        "apikey": API_KEY
    }
    item = 20

    # optional and required parameters for this api to work.
    parameters = {
        "fly_from": f"{current_place[0]}",
        "fly_to": f"{destinations[0]}",
        "date_from": f"{date_from}",
        "date_to": f"{date_to}",
        "adults": 1,
        "selected_cabins": "M",
        "limit": item
    }

    tequila_endpoint = "https://tequila-api.kiwi.com/v2/search"
    response = requests.get(url=tequila_endpoint, params=parameters, headers=header)
    response.raise_for_status()
    data = (response.json())

    with open('plane.txt', 'w') as json_file:
        json.dump(data, json_file, indent=4)

    with open('plane.txt', 'r') as f:
        json_file = json.load(f)["data"]
    # print(json_file)

    ticket_prices = []
    for low_price in range(item):
        ticket_prices.append(json_file[low_price]["price"])
    # print(ticket_prices)
    lowest_price = min(ticket_prices)
    blue_bar.itemconfig(price_text, text=lowest_price)

    index = ticket_prices.index(lowest_price)

    # Formatting the time.
    d1 = datetime.datetime.strptime(f"{json_file[index]['local_departure']}", "%Y-%m-%dT%H:%M:%S.%fZ")
    d2 = datetime.datetime.strptime(f"{json_file[index]['local_arrival']}", "%Y-%m-%dT%H:%M:%S.%fZ")
    new_format = "%Y-%m-%d"
    d2.strftime(new_format)
    d1.strftime(new_format)

    blue_bar.itemconfig(depart_text, text=d1)
    blue_bar.itemconfig(arrival_text, text=d2)
    blue_bar.itemconfig(airline_text, text=json_file[index]["airlines"][0])


window = Tk()
window.title("Plane Ticket")
window.minsize(width=1030, height=600)

# The plane logo on the gui.
plane = Canvas(width=475, height=350)
plane_logo = PhotoImage(file="images.jpg")
plane.create_image(250, 100, image=plane_logo)
plane.place(x=250, y=10)

# Input box for the country you are currently residing.
from_entry = Entry(width=13, font=("poppins", 25, "bold"))
from_entry.config(fg="white", bg=BG, border=0, justify='center')
from_entry.place(x=95, y=25)

from_label = Label(text="From : ", font=FONT)
from_label.place(x=5, y=25)

# Input box for the country you wish to visit.
to_entry = Entry(width=13, font=("poppins", 25, "bold"))
to_entry.config(fg="white", bg=BG, border=0, justify='center')
to_entry.place(x=95, y=100)

to_label = Label(text="To : ", font=FONT)
to_label.place(x=15, y=100)

# Input box for the first date you are available to travel.
date_from_entry = Entry(width=13, font=("poppins", 25, "bold"))
date_from_entry.config(fg="white", bg=BG, border=0, justify='center')
date_from_entry.place(x=780, y=25)

date_from_label = Label(text="Date From : ", font=FONT)
date_from_label.place(x=630, y=25)

# Input box for the last date you are available to travel.
date_to_entry = Entry(width=13, font=("poppins", 25, "bold"))
date_to_entry.config(fg="white", bg=BG, border=0, justify='center')
date_to_entry.place(x=780, y=100)

date_to_label = Label(text="Date To : ", font=FONT)
date_to_label.place(x=640, y=100)

# Button for searching the cheapest flight.
show_flight_button = Button(text="Show flights", font=FONT, command=getting_flight)
show_flight_button.place(x=420, y=250)

# This is the blue bar on the bottom that shows the price, departure time,
# arrival time and airlines for the search result.
blue_bar = Canvas(width=820, height=100, bd=0, highlightthickness=0, relief='ridge')
blue_bar_logo = PhotoImage(file="box.png")
blue_bar.create_image(380, 40, image=blue_bar_logo)
blue_bar.place(x=140, y=500)
blue_bar.create_text(70, 20, fill="white", font=FONT, text="PRICE")

blue_bar.create_text(260, 20, fill="white", font=FONT, text="DEPART")

blue_bar.create_text(460, 20, fill="white", font=FONT, text="ARRIVAL")

blue_bar.create_text(660, 20, fill="white", font=FONT, text="AIRLINE")

price_text = blue_bar.create_text(70, 60, fill="black", font=FONT, text="...")

depart_text = blue_bar.create_text(260, 60, fill="black", font="Helvetica 15 bold", text="...")

arrival_text = blue_bar.create_text(480, 60, fill="black", font="Helvetica 15 bold", text="...")

airline_text = blue_bar.create_text(660, 60, fill="black", font=FONT, text="...")

window.mainloop()
