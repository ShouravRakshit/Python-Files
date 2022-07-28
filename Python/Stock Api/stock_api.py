import datetime
import smtplib
import os
from data import Data
from email.message import EmailMessage

information = Data()
stock_data = information.get_stock_data()
news_data = information.get_news()


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


today = datetime.date.today()
day = 1

while True:
    # If this section of the code fails because of KeyError, then it will just go back one more previous day to check
    # if there is data on the previous day. If not, then it will just continue doing the same task.
    try:
        yesterday = str(today - datetime.timedelta(days=day - 1))
        today_stock_price = float(stock_data["Time Series (Daily)"][yesterday]["4. close"])
        day_before_yesterday = str(today - datetime.timedelta(days=day))
        day_before_yesterday_stock_price = float(stock_data["Time Series (Daily)"][day_before_yesterday]["4. close"])
        break
    except KeyError:
        day += 1

# print(f"Today's stock price is : {today_stock_price}")
# print(f"Yesterday's stock price was : {day_before_yesterday_stock_price}")
# If the today's stock price increased 5 percent then yesterday's, then it will send an email to notify me.
if (day_before_yesterday_stock_price * .05) + day_before_yesterday_stock_price <= today_stock_price:
    news_title = news_data["articles"][0]["title"]
    news_description = news_data["articles"][0]["description"]
    email_alert(news_title, news_description, "shouravivan1000@gmil.com")
