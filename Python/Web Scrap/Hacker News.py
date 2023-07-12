from bs4 import BeautifulSoup
import requests
from pprint import pprint


def sort_stories(list):
    return sorted(list, key=lambda x: x["upvotes"], reverse=True)


def create_custom_news(links, votes):
    news = []
    for index in range(len(links)):
        title = links[index].getText()
        anchor_tag = links[index].find('a')
        try:
            points = int(votes[index].getText().replace(" points", ""))

        except IndexError:
            points = 0
        # print(points)
        href = anchor_tag['href']
        if points > 99:
            news.append({"title": title,
                         "link": href,
                         "upvotes": points})

    return sort_stories(news)


def get_response():
    response = requests.get('https://news.ycombinator.com/')
    response2 = requests.get('https://news.ycombinator.com/news?p=2')
    soup = BeautifulSoup(response.text, 'html.parser')
    soup2 = BeautifulSoup(response2.text, 'html.parser')
    votes = soup.select(".score") + soup2.select(".score")
    links = soup.select(".titleline") + soup2.select(".titleline")

    result = create_custom_news(links, votes)
    pprint(result)


get_response()

