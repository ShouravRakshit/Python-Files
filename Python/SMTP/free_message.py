import smtplib
import os
from email.message import EmailMessage
import datetime as dt
import random

with open("quotes.txt", mode="r") as file:
    quotes = file.readlines()
    random_quote = random.choice(quotes)
    print(random_quote)


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


week_day = dt.datetime.now().strftime("%A")

if week_day == "Monday":
    email_alert("Motivational Quote", f"{random_quote}", "shouravivan1000@gmail.com")
