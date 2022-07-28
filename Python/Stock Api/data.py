import requests
import os

STOCK = "GOOGL"


class Data:

    def __init__(self):
        self.google_password = os.environ.get("stock_api")
        self.news_password = os.environ.get("news_api")

    # Getting the news data from the api.
    def get_news(self):
        news_parameters = {
            "country": "us",
            "category": "business",
            "q": STOCK,
            "apiKey": self.news_password

        }

        news_url = "https://newsapi.org/v2/top-headlines"
        response = requests.get(news_url, params=news_parameters)
        return response.json()

    # Getting the stock data from the api.
    def get_stock_data(self):
        stock_parameters = {
            "function": "TIME_SERIES_DAILY",
            "symbol": STOCK,
            "apikey": self.google_password
        }

        stock_url = 'https://www.alphavantage.co/query'
        r = requests.get(stock_url, params=stock_parameters)
        return r.json()
