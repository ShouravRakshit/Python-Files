from tkinter import *
import requests
import os
import datetime
import smtplib
from email.message import EmailMessage


# This function sends the message.
def email_alert(subject, body, to):
    msg = EmailMessage()
    msg.set_content(body)
    msg["subject"] = subject
    msg["to"] = to
    user = "skyfiresmith25@gmail.com"
    password = os.environ["Email_password"]
    msg["from"] = user
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(user, password)
    server.send_message(msg)
    server.quit()


# Getting the news data from the news api.
def news_data(stock_company, news_password):
    news_parameters = {
        "country": "us",
        "category": "business",
        "q": stock_company,
        "apiKey": news_password
    }

    news_url = "https://newsapi.org/v2/top-headlines"
    return requests.get(news_url, params=news_parameters).json()


# Getting the stock data from alphavantage api.
def stock_data(stock_company, google_password):
    stock_parameters = {
        "function": "TIME_SERIES_DAILY",
        "symbol": stock_company,
        "apikey": google_password
    }

    stock_url = 'https://www.alphavantage.co/query'
    return requests.get(stock_url, params=stock_parameters).json()


def get_data():
    stock_company = search_bar_entry.get()
    google_password = os.environ.get("stock_api")
    news_password = os.environ.get("news_api")

    news = news_data(stock_company, news_password)
    stock = stock_data(stock_company, google_password)

    today = datetime.date.today()
    day = 1

    while True:
        # If this section of the code fails because of KeyError,
        # then it will just go back one more previous day to check
        # if there is data on the previous day. If not, then it will just continue doing the same task.
        try:
            yesterday = str(today - datetime.timedelta(days=day - 1))
            today_stock_price = float(stock["Time Series (Daily)"][yesterday]["4. close"])
            day_before_yesterday = str(today - datetime.timedelta(days=day))
            day_before_yesterday_stock_price = float(
                stock["Time Series (Daily)"][day_before_yesterday]["4. close"])
            break
        except KeyError:
            day += 1

    print(f"Today's stock price is : {today_stock_price}")
    print(f"Yesterday's stock price was : {day_before_yesterday_stock_price}")
    # If the today's stock price increased 5 percent then yesterday's, then it will notify me through email.
    if (day_before_yesterday_stock_price * .05) + day_before_yesterday_stock_price <= today_stock_price:
        news_title = news["articles"][0]["title"]
        news_description = news["articles"][0]["description"]
        email_alert(news_title, news_description, "shouravivan1000@gmil.com")

    if today_stock_price > day_before_yesterday_stock_price:
        image = PhotoImage(file="stock_up.png")
        imageLabel.configure(image=image)
        imageLabel.image = image
    else:
        image = PhotoImage(file="stock_down.png")
        imageLabel.configure(image=image)
        imageLabel.image = image


BG = "#404040"
FONT = "Helvetica 15 bold"

window = Tk()
window.title("Stock App")
window.minsize(width=1050, height=600)

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
button = Button(image=search_icon_logo, borderwidth=0, command=get_data, bg=BG, activebackground="#404040")
button.place(x=400, y=53)

imageLabel = Label()
imageLabel.pack(side=LEFT)

window.mainloop()
