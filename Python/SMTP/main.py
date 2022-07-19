import pandas
import random
import os
import smtplib
import datetime as dt
from email.message import EmailMessage


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


df = pandas.read_csv('birthdays.csv')
name = (df["name"][0])
month = df["month"][0]
date = df["day"][0]
random_file = random.randint(1, 3)
with open(f"letter_templates/letter_{random_file}.txt", mode="r") as file:
    words_list = file.readlines()

with open(f"letter_templates/letter_{random_file}.txt", mode="w") as f:
    for letters in words_list:
        f.write(letters.replace("[NAME]", name))

if int(dt.datetime.now().strftime("%d")) == date and int(dt.datetime.now().strftime("%m")) == month:
    with open(f"letter_templates/letter_{random_file}.txt", mode="r") as f:
        content = f.readlines()
        words = ""
        for letters in content:
            words = words + letters
        email_alert("Motivational Quote", words, "shouravivan1000@gmail.com")

